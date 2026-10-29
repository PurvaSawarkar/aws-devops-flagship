# AWS DevOps Flagship Project

An end-to-end DevOps portfolio project demonstrating a containerized Task Management API deployed on AWS EC2.

## Project Overview

A REST API built with FastAPI to create, retrieve, update, and delete tasks. The application uses PostgreSQL for persistent storage and Docker Compose to run the API and database together.

## Tech Stack

- **Language:** Python
- **API Framework:** FastAPI
- **Database:** PostgreSQL
- **Containers:** Docker, Docker Compose
- **Cloud:** AWS EC2 (Ubuntu)
- **Testing:** pytest
- **Version Control:** Git and GitHub

## Features

- CRUD endpoints for task management
- Health, readiness, and application version endpoints
- Interactive API documentation with Swagger UI
- Containerized API and PostgreSQL database
- Database health checks and service dependency management
- Persistent PostgreSQL data using a Docker volume
- Non-root user in the API container
- Automated tests and code quality checks

## Run Locally

1. Create a `.env` file using `.env.example` as a reference.
2. Set a strong `POSTGRES_PASSWORD` in `.env`.
3. Start the application:

   ```bash
   docker compose up --build -d
   ```

4. Open the API documentation:

   `http://127.0.0.1:8000/docs`

5. Check application health:

   `http://127.0.0.1:8000/health`

## Deployment

The application has been deployed on an AWS EC2 Ubuntu instance using Docker Compose.

- The API and PostgreSQL run in separate containers.
- PostgreSQL data is stored in a named Docker volume.
- The database port is not published publicly.
- The API is accessed through an SSH tunnel for testing.
- The EC2 security group restricts SSH access to an authorized source IP.

## Testing and Quality

- Six automated tests passed during project validation.
- API endpoints were tested through Swagger UI.
- Code quality and dependency security checks passed during project validation.
- PostgreSQL connectivity and data persistence were verified.

## Planned Improvements

- Add a GitHub Actions CI pipeline.
- Provision AWS infrastructure using Terraform.
- Improve deployment automation and monitoring.

## Security Notes

- Keep `.env`, private SSH keys, and credentials out of Git.
- Use strong database passwords and restrict inbound network access.
- Do not expose the PostgreSQL port publicly.

## Project Status

**Completed:** API implementation, Docker Compose setup, AWS EC2 deployment, endpoint validation, and PostgreSQL persistence verification.

**Planned:** CI/CD automation and Terraform infrastructure provisioning.
