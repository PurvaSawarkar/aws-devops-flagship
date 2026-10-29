output "aws_account_id" {
  description = "AWS account Terraform is connected to"
  value       = data.aws_caller_identity.current.account_id
}

output "aws_region" {
  description = "AWS region Terraform is using"
  value       = data.aws_region.current.name
}
