resource "aws_lambda_function" "dynamodb" {
  function_name = var.application_name
  handler       = var.lambda_handler_name
  runtime       = var.lambda_runtime
  role          = aws_iam_role.lambda_execution_role.arn
  timeout       = var.lambda_timeout

  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = filebase64sha256(data.archive_file.lambda_zip.output_path)

  environment {
    variables = {
      DYNAMODB_TABLE_NAME = var.application_name
    }
  }
}
