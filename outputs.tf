/**
  Dynamo DB
*/
output "dynamodb_table_name" {
  description = "Dynamo DB table name"
  value       = aws_dynamodb_table.helloworld_api.name
}
