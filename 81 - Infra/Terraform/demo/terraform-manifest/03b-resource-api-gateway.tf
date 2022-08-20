
resource "aws_api_gateway_rest_api" "api_lambda" {
  depends_on = [aws_lambda_function.lambda_func]
  name       = "${var.project_name}-dash-${local.deploy-env}"
}

resource "aws_api_gateway_resource" "gw_resource" {
  for_each    = var.lambda_dir_map
  rest_api_id = aws_api_gateway_rest_api.api_lambda.id
  parent_id   = aws_api_gateway_rest_api.api_lambda.root_resource_id
  path_part   = each.key
}

resource "aws_api_gateway_method" "proxyMethod" {
  for_each      = var.lambda_dir_map
  rest_api_id   = aws_api_gateway_rest_api.api_lambda.id
  resource_id   = aws_api_gateway_resource.gw_resource["${each.key}"].id
  http_method   = "ANY"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda" {
  for_each                = var.lambda_dir_map
  rest_api_id             = aws_api_gateway_rest_api.api_lambda.id
  resource_id             = aws_api_gateway_method.proxyMethod["${each.key}"].resource_id
  http_method             = aws_api_gateway_method.proxyMethod["${each.key}"].http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.lambda_func["${each.key}"].invoke_arn
}

resource "aws_api_gateway_deployment" "apideploy" {
  depends_on = [
    aws_api_gateway_integration.lambda,
  ]

  triggers = {
    always_run = "${timestamp()}"
  }

  rest_api_id = aws_api_gateway_rest_api.api_lambda.id
  stage_name  = local.deploy-env
}

resource "aws_lambda_permission" "apigw" {
  for_each      = var.lambda_dir_map
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_func["${each.key}"].id
  principal     = "apigateway.amazonaws.com"
  # The "/*/*" portion grants access from any method on any resource within the API Gateway REST API.
  source_arn = "${aws_api_gateway_rest_api.api_lambda.execution_arn}/*/*"
}