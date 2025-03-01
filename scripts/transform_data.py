import __main__
from pymongo.mongo_client import MongoClient
import pandas  as pd
import extract_and_save_data 







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
def transform_list_to_data_frame(list_data):
    data_frame = pd.DataFrame(list_data)
    return data_frame



#Pegando apenas os dados do municipio do rio

def retrive_data_municipios_rj(collection):
    query = {"municipio" : "RIO DE JANEIRO"}
    
    lista_dados_eleitorais_rj = []

    for docs in collection.find(query):
        
        lista_dados_eleitorais_rj.append(docs)

    return lista_dados_eleitorais_rj



def drop_columns(data_frame):
    data_frame = data_frame.drop(["numLocal","numZona","secoes"],axis=1)
    return data_frame



# Transformando em csv
def data_frame_to_csv(path,data_frame):
    data_frame.to_csv(path)



if __name__ == "__main__":
    client = extract_and_save_data.connect_mongo_db("mongodb://localhost:27017/")
    db = retrieve_data_db(client,"db_dados_eleitorais")
    collection = retrieve_collection(db,"locais_votacoes")
    list_data = read_collection_to_list(collection)
    data_frame = transform_list_to_data_frame(list_data)
    list_municipios_rj = retrive_data_municipios_rj(collection)
    df_municipios_rj = transform_list_to_data_frame(list_municipios_rj)
    df_municipios_rj = drop_columns(df_municipios_rj)
    data_csv = data_frame_to_csv("../data/dados_eleitorais_rj2.csv",df_municipios_rj)
    client.close()


