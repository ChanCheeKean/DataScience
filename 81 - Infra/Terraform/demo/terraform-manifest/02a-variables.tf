variable "project_name" {
  description = "Name of project to be created"
  type        = string
  default     = "employee-engagement"
}

variable "region" {
  description = "Region in which AWS resources to be created"
  type        = string
  default     = "us-east-1"
}

variable "lambda_dir_map" {
  description = "Directory for each lambda function"
  type        = map(string)
  default = {
    "pg2-search" = "pg2_similarity_search_lambda",
    "pg1-fig"    = "pg1_fig_output_lambda",
  }
}

locals {
  # if workspace is default then env is dev
  deploy-env = terraform.workspace == "default" ? "dev" : terraform.workspace
}



