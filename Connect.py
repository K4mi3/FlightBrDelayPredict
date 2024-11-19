import os
import pandas as pd
from pymongo import MongoClient
from unidecode import unidecode

#Pasta de input:
pasta_2023 = 'Input/Voos/2023'
pasta_2024 = 'Input/Voos/2024'

#Instanciar dataframe:
df_voos = []

#####
def ler_arquivos_da_pasta(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(pasta, arquivo)
            df = pd.read_csv(caminho_arquivo, delimiter=";")
            df_voos.append(df)
            
ler_arquivos_da_pasta(pasta_2023)
ler_arquivos_da_pasta(pasta_2024)
df_final = pd.concat(df_voos, ignore_index=True)            

# Função para normalizar os nomes das colunas
def normalize_column_name(col_name):
    col_name = unidecode(col_name)  # Remove acentos
    col_name = col_name.replace(" ", "_")  # Substitui espaços por underscores
    return col_name.lower()  # Deixa em letras minúsculas

# Aplicando a função a cada nome de coluna
df_final.columns = [normalize_column_name(col) for col in df_final.columns]

print(df_final.columns)


# Conectando ao MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Acessando o banco de dados
db = client["voos"]
# Acessando uma coleção
colecao = db["Voos_cll"]
#collection = db["nome_da_colecao"]

for _, row in df_final.iterrows():
    documento = row.to_dict()  # Converte a linha para um dicionário
    colecao.insert_one(documento)  # Insere o dicionário como um documento na coleção



print("Documento inserido com sucesso!")
for documento in colecao.find():
    print(documento)
