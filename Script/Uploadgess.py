# O primeiro passo é fazer a conexão com o BOTO3 pra isso o caminho correto é:
import boto3
from botocore.client import Config

import getpass #Getpass é importante para manter a Key oculta enquanto você digita

#Aqui é onde damos os primeiros comandos, assim o sript fica disponivel para todos usarem somente inserindo suas credenciais.
ACCESS_KEY_ID=getpass.getpass("Digite sua key ID: ") #A Key é retirada na IAM user no site do AWS.
ACCESS_SECRET_KEY=getpass.getpass("Digite sua secret key: ") #Secret key o mesmo procedimento, o usuario tem que tomar cuidado porque as duas são keys isso pode confundir.
BUCKET_NAME=input("Digite o nome do bucket ao qual quer acesso: ") #O Nome do bucket em que você quer fazer o upload do arquivo.
FILE_NAME=input("Digite o nome do arquivo que quer fazer o upload: ") #O Nome do arquivo que vai fazer o upload, Lembrando que o nome tem que estar correto.

# Conexão com S3
s3 = boto3.resource(
    's3',
    aws_access_key_id= ACCESS_KEY_ID, #Não necessita digitar porque ele vai perguntar quando iniciar o script.
    aws_secret_access_key= ACCESS_SECRET_KEY, #Mesmo caso do de cima.
    config=Config(signature_version='s3v4')
)

# Upload do arquivo

s3 = boto3.resource('s3')

s3.Bucket(BUCKET_NAME).upload_file("/mnt/c/Users/AlexP/Desktop/" +FILE_NAME, FILE_NAME ) #Sempre colocar o caminho de onde esta o seu arquivo

print ("Upload realizado")





