import sqlite3

# monstrando o caminho do arquivo do nosso banco de dados. Criando conexão com o banco de dados

con = sqlite3.connect("my_banco_de_dados.db")

# criando um cursor para executar instruções SQL

cursor = con.cursor()

x = cursor.execute(f"SELECT * from Pessoas")

for i in x:
    print(i) # vai trazer as linhas que foram criadas no banco de dados











