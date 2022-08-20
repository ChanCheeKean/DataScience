# Define Local Values using local variable so that we dont repeat multiple times
locals {
  bucket-name = "${var.app_name}-${var.environment_name}-bucket" # Complex expression
}

resource "aws_s3_bucket" "mys3bucket" {
  bucket = local.bucket-name
  acl = "private"
  tags = {
    Name = local.bucket-name
    Environment = var.environment_name
  }
}