import logging
from contextlib import asynccontextmanager
from time import perf_counter

from fastapi import Depends, FastAPI, HTTPException, Query, Request, Response
from sqlalchemy import select, text
from sqlalchemy.orm import Session

from app.config import settings
from app.database import Base, engine, get_db
from app.logging_config import setup_logging
from app.models import Task
from app.schemas import TaskCreate, TaskRead, TaskUpdate

setup_logging(settings.log_level)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title='DevOps Task API',
    version=settings.app_version,
    description='A portfolio API deployed with Docker and AWS.',
    lifespan=lifespan,
)


@app.middleware('http')
async def log_requests(request: Request, call_next):
    start = perf_counter()
    status_code = 500

    try:
        response = await call_next(request)
        status_code = response.status_code
        return response
    finally:
        duration_ms = round((perf_counter() - start) * 1000, 2)
        logger.info(
            'request completed',
            extra={
                'method': request.method,
                'path': request.url.path,
                'status': status_code,
                'duration_ms': duration_ms,
            },
        )


@app.get('/')
def root():
    return {'message': 'DevOps Task API', 'docs': '/docs'}


@app.get('/health')
def health():
    return {'status': 'healthy'}


@app.get('/version')
def version():
    return {'version': settings.app_version}


@app.get('/ready')
def ready(db: Session = Depends(get_db)):  # noqa: B008
    try:
        db.execute(text('SELECT 1'))
        return {'status': 'ready'}
    except Exception as exc:
        logger.exception('database readiness check failed')
        raise HTTPException(
            status_code=503,
            detail='Database unavailable',
        ) from exc


@app.post('/tasks', response_model=TaskRead, status_code=201)
def create_task(
    payload: TaskCreate,
    db: Session = Depends(get_db),  # noqa: B008
):
    task = Task(**payload.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@app.get('/tasks', response_model=list[TaskRead])
def list_tasks(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),  # noqa: B008
):
    statement = select(Task).order_by(Task.id).limit(limit).offset(offset)
    return db.scalars(statement).all()


@app.get('/tasks/{task_id}', response_model=TaskRead)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),  # noqa: B008
):
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return task


@app.patch('/tasks/{task_id}', response_model=TaskRead)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    db: Session = Depends(get_db),  # noqa: B008
):
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')

    updates = payload.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


@app.delete('/tasks/{task_id}', status_code=204)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),  # noqa: B008
):
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')

    db.delete(task)
    db.commit()
    return Response(status_code=204)