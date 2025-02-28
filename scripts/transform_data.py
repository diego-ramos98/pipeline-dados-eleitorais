import __main__
from pymongo.mongo_client import MongoClient
import pandas  as pd
import extract_and_save_data 




#client = extract_and_save_data.connect_mongo_db()


#lendo dados do banco
def retrieve_data_db(client,db_name):
    db = client[db_name]
    
    return db



#PEGANDO AS COLLECTION

def retrieve_collection(db,collection_name):
    collection =  db[collection_name]

    return collection


#LENDO DADOS DA COLLECTION
def read_collection_to_list(collection_name):
    list_data = []

    for doc in collection_name.find():
        list_data.append(doc)
        
        return list_data
    

# DE LISTA PARA DATA FRAME
def transform_list_to_data_frame(data_frame,list_data):
    data_frame = pd.DataFrame(list_data)
    return data_frame

#Conferindo os diferentes municipios registrado
def retrive_unique_municipios(data_frame):
    return data_frame["municipio"].unique


#Pegando apenas os dados do municipio do rio

def retrive_data_municipios_rj():
    query = {"municipio" : "RIO DE JANEIRO"}
    
    lista_dados_eleitorais_rj = []

    for docs in collection.find(query):
        lista_dados_eleitorais_rj.append(docs)
    
    return lista_dados_eleitorais_rj


# Transformando em csv
