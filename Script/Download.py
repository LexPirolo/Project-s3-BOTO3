#Começando com a inicialização do BOTO3
import boto3
from botocore.client import Config

#Aqui é onde damos os primeiros comandos, assim o sript fica disponivel para todos usarem somente inserindo suas credenciais.
ACCESS_KEY_ID=input("Digite sua key ID: ") #A Key é retirada na IAM user no site do AWS.
ACCESS_SECRET_KEY=input("Digite sua secret key: ") #Secret key o mesmo procedimento, o usuario tem que tomar cuidado porque as duas são keys isso pode confundir.
BUCKET_NAME=input("Digite o nome do bucket ao qual quer acesso: ") #O Nome do bucket em que você quer fazer o download do arquivo.
FILE_NAME=input("Digite o nome do arquivo que quer fazer o download: ")  #O Nome do arquivo que vai fazer o download, Lembrando que o nome tem que estar correto e com extensão.

#Conexão com o S3
s3 = boto3.resource(
    's3',
    aws_access_key_id= ACCESS_KEY_ID, #Não necessita digitar porque ele vai perguntar quando iniciar o script.
    aws_secret_access_key= ACCESS_SECRET_KEY,  #Mesmo caso do de cima.
    config=Config(signature_version='s3v4')
)

# Download do arquivo
s3.Bucket(BUCKET_NAME).download_file(FILE_NAME, '/mnt/c/Users/AlexP/Desktop/'+FILE_NAME); #Coloque o diretorio onde quer fazer o donwload do arquivo

# Agora só esperar baixar o arquivo.
print("Arquivo baixado")




