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