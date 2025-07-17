terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      # keep under 6.0 so the EKS & VPC modules are happy
      version = ">= 5.95, < 6.0.0"
    }
  }
}
