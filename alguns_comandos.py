import sqlite3

# monstrando o caminho do arquivo do nosso banco de dados. Criando conexão com o banco de dados

con = sqlite3.connect("my_banco_de_dados.db")

# criando um cursor para executar instruções SQL

cursor = con.cursor()

nome = input("Digite seu nome:  ")
idade = int(input("Digite a sua idade:  "))

# existe algumas alterações para fazer no banco de dados

cursor.execute(f"INSERT INTO Pessoas VALUES ('{nome}', {idade})")

con.commit() # confirmando a mudança, alteração em nosso banco de dados



# ('''CREATE TABLE "Pessoas" (
                    "nome" TEXT,
                    "idade" INTEGER
                    );''')


