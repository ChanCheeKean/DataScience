
### print list of container images in ecr
output "ecr_images" {
  description = "List of Container Images Created"
  value       = [for ele in aws_ecr_repository.repo : ele.repository_url]
}

### print list of lambda funtions created
output "lambda_name" {
  description = "List of Lambda Function created"
  value       = [for ele in aws_lambda_function.lambda_func : ele.id]
}

### print the base url of the api gateway
output "base_url" {
  description = "Url of API gateway to trigger Lambda Function"
  value       = aws_api_gateway_deployment.apideploy.invoke_url
}

