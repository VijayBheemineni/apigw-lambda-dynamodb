# apigw-lambda-dynamodb
This is hello world example of using 'http' API GW integrates with Lambda. And Lambda performs CRUD operations on DynamoDB.

<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | ~> 1.9.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | >= 5.72.1 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | >= 5.72.1 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_dynamodb_table.helloworld_api](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_application_name"></a> [application\_name](#input\_application\_name) | Hello World API Application Name. It should be of format '<name>-<env>'. Because '<env>' value will be used to create stages. | `string` | `"helloworld-api-test-dev"` | no |

## Outputs

No outputs.
<!-- END_TF_DOCS -->
