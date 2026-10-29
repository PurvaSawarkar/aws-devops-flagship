# Terraform Infrastructure

## Overview

This directory manages the AWS infrastructure for TaskForge using Terraform.

## AWS Configuration

- **Region:** `ap-south-1` (Mumbai)
- **Compute:** Amazon EC2
- **Networking:** Existing VPC, subnet, and security group
- **State Backend:** Amazon S3
- **State Locking:** S3 native lockfile
- **State Encryption:** Enabled
- **Bucket Versioning:** Enabled

## Common Commands

Initialize Terraform:

```bash
terraform init
```

Check formatting:

```bash
terraform fmt -check -recursive
```

Validate configuration:

```bash
terraform validate
```

Review infrastructure changes:

```bash
terraform plan
```

## Safety

- Review every plan before applying changes.
- Never commit Terraform state, plan files, credentials, or `.tfvars` files.
- Keep state backups in a secure location.
- Do not run `terraform apply` without reviewing the proposed changes.
