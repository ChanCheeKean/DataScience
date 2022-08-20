
### get account id from aws_caller
data "aws_caller_identity" "current" {}

### store variables
locals {
  prefix        = "${path.module}/../lambda_serving"
  account_id    = data.aws_caller_identity.current.account_id
  ecr_image_tag = "latest"
}

### create ecr for each lambda images
resource "aws_ecr_repository" "repo" {
  for_each     = var.lambda_dir_map
  name         = "${var.project_name}-${each.key}-${local.deploy-env}"
  force_delete = true
}

### local provisioner to run Docker File
resource "null_resource" "docker_image" {
  for_each = var.lambda_dir_map

  # trigger by main.py and dockerfile
  triggers = {
    # always-update = timestamp()
    python_file = md5(file("${local.prefix}/${each.value}/main.py"))
    docker_file = md5(file("${local.prefix}/${each.value}/Dockerfile"))
  }

  provisioner "local-exec" {
    command = <<-EOF
        aws ecr get-login-password --region ${var.region} | docker login --username AWS --password-stdin ${local.account_id}.dkr.ecr.${var.region}.amazonaws.com && cd ${local.prefix} && docker build -t ${aws_ecr_repository.repo["${each.key}"].repository_url}:${local.ecr_image_tag} -f ${each.value}/Dockerfile . && docker push ${aws_ecr_repository.repo["${each.key}"].repository_url}:${local.ecr_image_tag}
       EOF
  }
}

### extract id of each image in ECR
data "aws_ecr_image" "container_image" {
  for_each        = var.lambda_dir_map
  depends_on      = [null_resource.docker_image]
  repository_name = "${var.project_name}-${each.key}-${local.deploy-env}"
  image_tag       = local.ecr_image_tag
}

### create IAM role for lambda
resource "aws_iam_role" "lambda_role" {
  name = "${var.project_name}-lambda-role-${local.deploy-env}"
  managed_policy_arns = [
    "arn:aws:iam::aws:policy/SecretsManagerReadWrite",
    "arn:aws:iam::aws:policy/AmazonS3FullAccess",
    "arn:aws:iam::aws:policy/AWSLambda_FullAccess",
    "arn:aws:iam::aws:policy/AmazonOpenSearchServiceFullAccess"

  ]

  assume_role_policy = <<-EOF
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Effect": "Allow"
            }
        ]
    }
    EOF
}

### create IAM policy for lambda function
data "aws_iam_policy_document" "lambda_policy_statement" {
  statement {
    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    effect    = "Allow"
    resources = ["*"]
    sid       = "CreateCloudWatchLogs"
  }

  statement {
    actions = [
      "codecommit:GitPull",
      "codecommit:GitPush",
      "codecommit:GitBranch",
      "codecommit:ListBranches",
      "codecommit:CreateCommit",
      "codecommit:GetCommit",
      "codecommit:GetCommitHistory",
      "codecommit:GetDifferences",
      "codecommit:GetReferences",
      "codecommit:BatchGetCommits",
      "codecommit:GetTree",
      "codecommit:GetObjectIdentifier",
      "codecommit:GetMergeCommit"
    ]
    effect    = "Allow"
    resources = ["*"]
    sid       = "CodeCommit"
  }
}

resource "aws_iam_policy" "lambda_policy" {
  name   = "${var.project_name}-lambda-policy-${local.deploy-env}"
  path   = "/"
  policy = data.aws_iam_policy_document.lambda_policy_statement.json
}

### create lambda function
resource "aws_lambda_function" "lambda_func" {
  for_each = var.lambda_dir_map
  depends_on = [
    null_resource.docker_image
  ]

  function_name = "${var.project_name}-${each.key}-${local.deploy-env}"
  role          = aws_iam_role.lambda_role.arn
  timeout       = 300
  image_uri     = "${aws_ecr_repository.repo["${each.key}"].repository_url}@${data.aws_ecr_image.container_image["${each.key}"].id}"
  package_type  = "Image"
  memory_size   = 2048
}
