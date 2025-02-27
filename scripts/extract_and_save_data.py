#Fazendo conexão com o banco
import __main__
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
    response = requests.get(url)
    data = response.json()
    
    return data;


#Salvando dados no banco
def salve_data_mongo_db(data,collection):
    docs = collection.insert_many(data)
    


if __name__ == "__main__":
    client  = connect_mongo_db("mongodb://localhost:27017/")
    db = create_db("db_eleicao_pe",client)
    collection = create_collection("locais-pe-votacao",db)
    data = extract_api("https://apps.tre-pe.jus.br/locaisVotacao/locais")   
    docs = salve_data_mongo_db(data,collection)
    client.close()

