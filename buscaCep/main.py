import requests
import json

cep = '49200000'
cep =cep.replace("-","").replace(".","").replace(" ","")

if(len(cep)==8):
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)

    print(requisicao)
    dic_requisicao = requisicao.json()

    uf=dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    print(uf,cidade,bairro)
else:
    print("CEP INVÁLIDO")