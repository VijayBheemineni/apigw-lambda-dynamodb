/**
  Dynamo DB
*/
output "dynamodb_table_name" {
  description = "Dynamo DB table name"
  value       = aws_dynamodb_table.helloworld_api.name
}

/**
  Lambda Details
*/
output "lambda_name" {
  description = "Lambda function name"
  value       = aws_lambda_function.dynamodb.function_name
}
