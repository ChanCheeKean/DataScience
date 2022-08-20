### retrieve secret manager
data "aws_secretsmanager_secret" "secrets" {
  arn = "arn:aws:secretsmanager:us-east-1:852288348919:secret:dash_postgres_secret-YJoDCf"
}

data "aws_secretsmanager_secret_version" "current" {
  secret_id = data.aws_secretsmanager_secret.secrets.id
}

resource "aws_db_instance" "rds_instance" {
  allocated_storage      = 20
  identifier             = "${var.project_name}-db"
  storage_type           = "gp2"
  engine                 = "postgres"
  engine_version         = "13.4"
  instance_class         = "db.m5.large"
  db_name                = "EeDashdb"
  username               = jsondecode(data.aws_secretsmanager_secret_version.current.secret_string)["username"]
  password               = jsondecode(data.aws_secretsmanager_secret_version.current.secret_string)["password"]
  vpc_security_group_ids = ["sg-08963f7da7758f6f5"]
  db_subnet_group_name   = "compass-api-integration"
  publicly_accessible    = true
  skip_final_snapshot    = true
  tags                   = { Name = "${var.project_name}-db" }
}