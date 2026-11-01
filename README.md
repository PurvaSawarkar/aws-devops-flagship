# TaskForge – AWS DevOps Flagship Project

TaskForge is a task management application built as a hands-on project to learn and demonstrate modern DevOps practices, cloud infrastructure management, containerization, and CI/CD automation using AWS.

The project covers the complete application delivery lifecycle—from developing and testing a FastAPI backend to deploying it on AWS EC2 through an automated GitHub Actions pipeline.

## Project Overview

TaskForge currently provides a FastAPI backend with PostgreSQL for persistent data storage. The application and database run in Docker containers using Docker Compose.

The infrastructure is hosted on AWS and managed using Terraform. GitHub Actions automates application checks, Terraform validation, and deployment.

## Technology Stack

| Category | Technologies |
|---|---|
| Backend | Python, FastAPI |
| Database | PostgreSQL 16 |
| Containerization | Docker, Docker Compose |
| Cloud Platform | AWS |
| Compute | Amazon EC2 |
| Infrastructure as Code | Terraform |
| Remote Terraform State | Amazon S3 |
| CI/CD | GitHub Actions |
| Deployment Automation | AWS IAM OIDC, AWS Systems Manager (SSM) |

## Architecture

```text
                 Developer
                     |
                     v
               GitHub Repository
                     |
                     v
              GitHub Actions
                     |
          +----------+----------+
          |                     |
          v                     v
      CI Pipeline          Terraform CI
      Tests & Checks       Format & Validate
          |
          v
    GitHub OIDC
          |
          v
       AWS IAM Role
          |
          v
    AWS Systems Manager
          |
          v
       AWS EC2
          |
          v
      Docker Compose
          |
       +--+---------+
       |            |
       v            v
    FastAPI      PostgreSQL
       |
       v
    Health API
```

## Key Features and Implementation

### 1. FastAPI Backend

- REST API built using FastAPI.
- Task management operations.
- PostgreSQL database integration.
- Health endpoint for application monitoring.

### 2. Docker and Docker Compose

- Containerized FastAPI application.
- PostgreSQL 16 Alpine database container.
- Docker Compose manages application and database services.

### 3. AWS Infrastructure

- Application hosted on AWS EC2.
- Infrastructure configuration managed using Terraform.
- Remote Terraform state stored in Amazon S3.
- S3 versioning and encryption enabled.
- Terraform state locking configured using S3 lockfiles.

### 4. Continuous Integration

GitHub Actions automates application and infrastructure checks.

The CI workflows include:

- Python tests.
- Code-quality checks.
- Terraform formatting checks.
- Terraform validation.

### 5. Automated Deployment using GitHub Actions

TaskForge uses GitHub Actions to deploy application updates to EC2 through AWS Systems Manager.

Deployment workflow:

1. Developer pushes changes to the GitHub repository.
2. GitHub Actions starts the deployment workflow.
3. GitHub authenticates with AWS using OIDC.
4. AWS IAM validates the GitHub identity and grants the deployment role.
5. GitHub Actions sends a deployment command through AWS Systems Manager.
6. EC2 pulls the latest code from the `master` branch.
7. Docker Compose rebuilds and starts the application.
8. A health check verifies the deployment.

**Security practices:**

- OIDC-based authentication instead of long-lived AWS access keys.
- IAM role with restricted deployment permissions.
- AWS Systems Manager for remote command execution.
- Application port bound to localhost rather than exposed publicly.

## Deployment Verification

The automated deployment workflow has been successfully executed.

| Verification | Result |
|---|---|
| GitHub Actions deployment workflow | Successful |
| AWS OIDC authentication | Successful |
| AWS Systems Manager command | Successful |
| Docker Compose deployment | Successful |
| PostgreSQL container health | Healthy |
| FastAPI health endpoint | HTTP 200 OK |

Health check:

```bash
curl -i http://localhost:8000/health
```

Expected response:

```http
HTTP/1.1 200 OK
```

```json
{
  "status": "healthy"
}
```

## Running Locally

### Prerequisites

- Python
- Docker
- Docker Compose

Clone the repository:

```bash
git clone https://github.com/PurvaSawarkar/aws-devops-flagship.git
cd aws-devops-flagship
```

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it using Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Start the application and database:

```bash
docker compose up --build
```

Check the health endpoint:

```text
http://localhost:8000/health
```

This assumes the Compose configuration exposes port 8000 locally.

## Terraform

Terraform configuration files are located in:

```text
infra/terraform/
```

Initialize Terraform:

```bash
terraform -chdir=infra/terraform init
```

Check formatting:

```bash
terraform -chdir=infra/terraform fmt -check -recursive
```

Validate configuration:

```bash
terraform -chdir=infra/terraform validate
```

Review infrastructure changes:

```bash
terraform -chdir=infra/terraform plan
```

Infrastructure changes should always be reviewed before applying them.

## Project Status

### Completed

- [x] FastAPI backend
- [x] PostgreSQL integration
- [x] Docker and Docker Compose setup
- [x] AWS EC2 application hosting
- [x] Terraform infrastructure configuration
- [x] Remote Terraform state using Amazon S3
- [x] GitHub Actions CI pipeline
- [x] Terraform CI workflow
- [x] GitHub OIDC authentication with AWS IAM
- [x] Automated deployment using AWS Systems Manager
- [x] Post-deployment health verification

### Future Improvements

- [ ] Monitoring and observability
- [ ] Centralized application logging
- [ ] Frontend development
- [ ] Additional security improvements
- [ ] More comprehensive automated tests

## Repository

GitHub: https://github.com/PurvaSawarkar/aws-devops-flagship

---

**TaskForge is a practical DevOps learning project focused on building, deploying, securing, and automating a cloud-hosted application using modern AWS and DevOps tools.**
