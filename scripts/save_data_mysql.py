import mysql.connector
import pandas as pd

def connect_mysql(host, user, password):
    cnx = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    print(cnx)
    return cnx


def create_cursor(cnx):
    cursor = cnx.cursor()
    return cursor


def create_db(db_name, cursor):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
    print(f"\nBase de dados {db_name} criada")


def show_databases(cursor):
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)


def create_table(db_name, table_name, cursor):
    # Primeiramente, use o banco de dados correto
    cursor.execute(f"USE {db_name}")
    
    # Criação da tabela
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            ID VARCHAR(255),
            LOCAL VARCHAR(255),
            MUNICIPIO VARCHAR(20),
            BAIRRO VARCHAR(50),
            ENDERECO VARCHAR(255),
            CEP VARCHAR(20),
            PRIMARY KEY (ID)
        )
    """)
    print(f"Tabela {table_name} criada")


def show_tables(cursor, db_name):
    cursor.execute(f"USE {db_name}")
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)


def read_csv(path):
    df = pd.read_csv(path)
    return df


def insert_table(cnx, cursor, df, db_name, table_name):
    # Converte o DataFrame em uma lista de tuplas
    data_list = [tuple(row) for _, row in df.iterrows()]
    
    # Ajustando o SQL para refletir o nome da tabela e banco de dados corretos
    sql = f"INSERT INTO {db_name}.{table_name} (ID, LOCAL, MUNICIPIO, BAIRRO, ENDERECO, CEP) VALUES (%s, %s, %s, %s, %s, %s)"
    
    cursor.executemany(sql, data_list)
    cnx.commit()
    print(f"{cursor.rowcount} registros inseridos na tabela {table_name}")


if __name__ == "__main__":
    # Realizando a conexão com MySQL
    cnx = connect_mysql("localhost", "root", "123456")
    cursor = create_cursor(cnx)

    # Criando a base de dados
    create_db("db_eleicao_teste", cursor)
    show_databases(cursor)

    # Criando a tabela
    create_table("db_eleicao_teste", "tb_eleicao_teste", cursor)
    show_tables(cursor, "db_eleicao_teste")

  

    # Lendo e adicionando os dados
    df = read_csv("../data/dados_eleitorais_rj.csv")
    
    # retirando coluna
    df = df.drop(["Unnamed: 0"],axis=1)

    insert_table(cnx, cursor, df, "db_eleicao_teste", "tb_eleicao_teste")
