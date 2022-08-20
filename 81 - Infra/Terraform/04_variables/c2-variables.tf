# Input Variables
# terraform will prompt for the values is default is undefined

# App Name S3 Bucket used for
variable "app_name" {
  description = "Application Name"
  type = string
}

# Environment Name
variable "environment_name" {
  description = "Environment Name"
  type = string
}

variable "aws_region" {
  description = "Region in which AWS resources to be created"
  type        = string
  default     = "us-east-1"
}

variable "ec2_ami_id" {
  description = "AMI ID"
  type        = string
  default     = "ami-0915bcb5fa77e4892" # Amazon2 Linux AMI ID.

  # to ensure correct id name
  validation {
      condition = length(var.ec2_ami_id) > 4 && substr(var.ec2_ami_id, 0, 4) == "ami-"
      error_message = "The ec2_ami_id value must be a valid AMI id, starting with \"ami-\"."
    }
}

variable "ec2_instance_count" {
  description = "EC2 Instance Count"
  type        = number
  default     = 1
}

# list type, var.ec2_instance_type[1]
variable "ec2_instance_type" {
  description = "EC2 Instance Type"
  type = list(string)
  default = ["t3.micro", "t3.small", "t3.large"]
}

# map type
variable "ec2_instance_tags" {
  description = "EC2 Instance Tags"
  type = map(string)
  default = {
    "Name" = "ec2-web"
    "Tier" = "Web"
  }
}

# var.ec2_instance_type_map['small-apps']
variable "ec2_instance_type_map" {
  description = "EC2 Instance Type"
  type = map(string)
  default = {
    "small-apps" = "t3.micro"
    "medium-apps" = "t3.medium" 
    "big-apps" = "t3.large"    
  }
}


/* 
To override the default value:

terraform plan -var "ec2_instance_count=5"
terraform apply -var "ec2_instance_count=5"

override with env variable
export ec2_instance_count=5

assigning tf.vars
terraform plan -var-file='terraform.tfvars'
.auto.tfvars, the variables in the file name will be loaded without assignment
*/
