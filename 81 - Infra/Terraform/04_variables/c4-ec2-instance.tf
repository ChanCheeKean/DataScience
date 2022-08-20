
# Create EC2 Instance using variable, using data sources and variable
resource "aws_instance" "my-ec2-vm" {
  # ami                    = var.ec2_ami_id
  ami                    = data.aws_ami.amzlinux.id
  # instance_type          = var.ec2_instance_type[0]
  instance_type          = var.ec2_instance_type_map["small-apps"]
  key_name               = "terraform-key"
  count                  = var.ec2_instance_count
  user_data = file("apache-install.sh")
  vpc_security_group_ids = [aws_security_group.vpc-ssh.id, aws_security_group.vpc-web.id]
  tags = var.ec2_instance_tags
}
