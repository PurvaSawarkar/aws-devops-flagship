# TaskForge

TaskForge is a task management application I'm building while learning how to design, deploy, and manage applications using AWS and modern DevOps tools.

The goal is to build more than just an API. I want to understand the complete workflow—from writing and testing the application to containerizing it, managing cloud infrastructure, and automating checks through CI/CD.

## What I'm building

The application currently has a FastAPI backend that supports task management operations, with PostgreSQL handling data storage.

The project uses:

- **Python and FastAPI** for the API
- **PostgreSQL** for the database
- **Docker and Docker Compose** to run the application and database
- **AWS EC2** to host the application
- **Terraform** to manage AWS infrastructure
- **Amazon S3** to store Terraform state remotely
- **GitHub Actions** to run tests and validate Terraform configuration

## How it works

The API handles task requests and communicates with PostgreSQL to store and retrieve data. Docker Compose runs the application and database together.

The application is hosted on an AWS EC2 instance. Terraform tracks the existing infrastructure, while its state is stored in an S3 backend with versioning, encryption, and state locking enabled.

GitHub Actions runs the Python test and code-quality checks, along with a separate Terraform formatting and validation workflow.

## Running locally

You'll need Python and Docker with Docker Compose installed.

Clone the repository:

```bash
git clone https://github.com/PurvaSawarkar/aws-devops-flagship.git
cd aws-devops-flagship
```

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

Start the application and database:

```bash
docker compose up --build
```

Check the health endpoint at `http://localhost:8000/health`, provided the Compose configuration exposes port 8000 and the health route is configured at that path.

## Terraform

Terraform files are located in `infra/terraform/`.

Initialize Terraform:

```bash
terraform -chdir=infra/terraform init
```

Format and validate the configuration:

```bash
terraform -chdir=infra/terraform fmt -check -recursive
terraform -chdir=infra/terraform validate
```

Review infrastructure changes before applying them:

```bash
terraform -chdir=infra/terraform plan
```

I don't apply infrastructure changes without reviewing the plan first.

## Current progress

The backend, database integration, Docker setup, AWS hosting, Terraform state migration, and basic CI workflows are in place.

I'm continuing to improve the project in stages, with deployment automation, monitoring, security, and a frontend as future milestones.

This repository is a practical learning project, and I'll keep documenting the decisions and improvements as it grows.
