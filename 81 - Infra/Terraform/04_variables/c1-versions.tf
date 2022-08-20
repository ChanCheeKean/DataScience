# Terraform Block
terraform {
  required_version = "~> 0.14" # which means any version equal & above 0.14 like 0.15, 0.16 etc and < 1.xx
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }

  # save the statefile in remote location
  backend "s3" {
    bucket = "terraform-state"
    key    = "dev/terraform.tfstate"
    region = "us-east-1" 

    # For State Locking
    dynamodb_table = "terraform-dev-state-table"    
  
  }

}

# Provider Block
provider "aws" {
  region  = var.aws_region
  profile = "default"
}