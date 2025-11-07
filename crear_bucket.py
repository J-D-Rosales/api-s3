import boto3

def lambda_handler(event, context):
    # Entrada (json desde API Gateway)
    # {"bucket": "nombre-del-bucket-nuevo"}
    nombre_bucket = event['body']['bucket']

    s3 = boto3.client('s3')

    # Para us-east-1 normalmente basta con esto
    s3.create_bucket(Bucket=nombre_bucket)

    return {
        "statusCode": 200,
        "mensaje": f"Bucket '{nombre_bucket}' creado correctamente"
    }
