
variable "aws_region" {
  description = "AWS region for the infrastructure"
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "vpc_id" {
  description = "Existing VPC ID"
  type        = string
  default     = "vpc-0c76a5d1b244eb866"
}

variable "subnet_id" {
  description = "Existing subnet ID"
  type        = string
  default     = "subnet-0251c0dd207bae320"
}

variable "key_name" {
  description = "Existing EC2 key pair name"
  type        = string
  default     = "Mumbai"
}

variable "iam_instance_profile" {
  description = "Existing EC2 IAM instance profile"
  type        = string
  default     = "devops-task-ssm-role"
}
