
terraform {
  required_version = ">= 1.5.0"

  backend "s3" {
    bucket       = "aws-devops-tfstate-462016339360-purva"
    key          = "aws-devops-flagship/terraform.tfstate"
    region       = "ap-south-1"
    encrypt      = true
    use_lockfile = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "server" {
  name        = "devops-task-server-sg"
  description = "launch-wizard-12 created 2026-10-27T13:02:10.420Z"
  vpc_id      = var.vpc_id

  lifecycle {
    ignore_changes = all
  }
}

resource "aws_instance" "server" {
  ami                    = "ami-094adff9b24048c5c"
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  key_name               = var.key_name
  iam_instance_profile   = var.iam_instance_profile
  vpc_security_group_ids = [aws_security_group.server.id]

  tags = {
    Name = "devops-task-server"
  }

  lifecycle {
    ignore_changes = all
  }
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}


