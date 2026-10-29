
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

resource "aws_security_group" "server" {
  name        = "devops-task-server-sg"
  description = "launch-wizard-12 created 2026-10-27T13:02:10.420Z"
  vpc_id      = "vpc-0c76a5d1b244eb866"

  lifecycle {
    ignore_changes = all
  }
}

resource "aws_instance" "server" {
  ami                    = "ami-094adff9b24048c5c"
  instance_type          = "t3.micro"
  subnet_id              = "subnet-0251c0dd207bae320"
  key_name               = "Mumbai"
  iam_instance_profile   = "devops-task-ssm-role"
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

output "aws_account_id" {
  description = "AWS account Terraform is connected to"
  value       = data.aws_caller_identity.current.account_id
}

output "aws_region" {
  description = "AWS region Terraform is using"
  value       = data.aws_region.current.name
}
