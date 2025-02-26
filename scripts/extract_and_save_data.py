#Fazendo conexão com o banco
from pymongo.mongo_client import MongoClient
import requests

def connect_mongo_db(uri):
    uri = uri
    client = MongoClient(uri)

    try:
        client.admin.command('ping')
        print("Pinged")
    except Exception as e:
        print(e)
    return client


#Criando banco
def create_db(name_db,client):
    db = client[name_db]

    return db

#Criando coleção
def create_collection(name_collection,db):
    collection = db[name_collection]
    return collection


#Extraindo dados da api
def extract_api(url):
    response = requests.get("https://apps.tre-rj.jus.br/api-dados-abertos/locaisvotacao")
    data = response.json()
    
    return data;


#Salvando dados no banco
def salve_data_mongo_db(data,collection):
    docs = collection.insert_many(data)
    count_data_inserted = docs.insertd_ids

    return f'Quantidade de dados inseridos: {count_data_inserted}'




