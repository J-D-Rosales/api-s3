import boto3

def lambda_handler(event, context):
    # Entrada:
    # {
    #   "bucket": "mi-bucket",
    #   "directorio": "imagenes-chicas",
    #   "archivo": "prueba.txt",
    #   "contenido": "Hola desde curl"
    # }
    bucket = event['body']['bucket']
    directorio = event['body']['directorio']
    archivo = event['body']['archivo']
    contenido = event['body']['contenido']

    if directorio and not directorio.endswith('/'):
        directorio += '/'

    key = f"{directorio}{archivo}"

    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=key, Body=contenido.encode('utf-8'))

    return {
        "statusCode": 200,
        "mensaje": f"Archivo '{key}' subido correctamente al bucket '{bucket}'"
    }
