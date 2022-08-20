/*adding life cycle for the resources, default lifecycle is destroy before create*/


# Create EC2 Instance
resource "aws_instance" "web" {
  ami               = "ami-0915bcb5fa77e4892" # Amazon Linux
  instance_type     = "t2.micro"
  availability_zone = "us-east-1a"
  #availability_zone = "us-east-1b"
  tags = {
    "Name" = "web-1"
  }

 /*
  lifecycle {
    create_before_destroy = true
  }
*/


 /* 
# resource will remain even terraform destrop
    lifecycle {
        prevent_destroy = true # Default is false
    }
*/

/*
  lifecycle {
    ignore_changes = [
      # Ignore changes to tags, e.g. because a management agent
      # updates these based on some ruleset managed elsewhere.
      tags,
    ]

    ignore_changes = all
  }*/



}