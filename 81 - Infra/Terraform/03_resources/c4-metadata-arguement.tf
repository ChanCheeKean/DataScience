/*meta arguement - depends_on, count, for_each*/

# Resource-9: Create Elastic IP
resource "aws_eip" "my-eip" {
  instance = aws_instance.my-ec2-vm.id
  vpc      = true
  # Meta-Argument, only start when vpc-dev-igw is created
  depends_on = [aws_internet_gateway.vpc-dev-igw]
}

##############################################################################################################################
# Create multi EC2 Instance with count
# aws_instance.web[0]
resource "aws_instance" "web" {
  ami           = "ami-047a51fa27710816e" # Amazon Linux
  instance_type = "t2.micro"
  count         = 5
  tags = {
    "Name" = "web-${count.index}"
  }
}

# Create multiple s3 buckets with for_each (map key)
# aws_s3_bucket.mys3bucket["dev"]
esource "aws_s3_bucket" "mys3bucket" {

  # for_each Meta-Argument
  for_each = {
    dev  = "my-dapp-bucket"
    qa   = "my-qapp-bucket"
    stag = "my-sapp-bucket"
    prod = "my-papp-bucket"
  }

  bucket = "${each.key}-${each.value}"
  acl    = "private"

  tags = {
    Environment = each.key
    bucketname  = "${each.key}-${each.value}"
    eachvalue   = each.value
  }
}

# Create fole with for_each (list)
# each.key == each,value
resource "aws_iam_user" "myuser" {
  for_each = toset(["TJack", "TJames", "TMadhu", "TDave"])
  name     = each.key
}
