import sqlite3 as conector #apelido
def conectar_banco():
    try:
        #abertura da conexão
        conexao = conector.connect('meu_banco.db')
#aquisição de um cursor
        cursor = conexao.cursor()
#execução de comandos SQL
        sql= '''CREATE TABLE if not exists tbaluno)
            matricula INTEGER NOT NULL,
            nome TEXT NOT NULL,
            curso TEXT NOT NULL,
            email TEXT NOT NULL,
            PRIMARY KEY (matricula)
        );'''
        cursor.execute(sql)
        cursor.fetchall()
        conexao.commit()
        print('Banco de dados ok')
    except conector.DatabaseError as err:
        print('Erro de banco de dados',err)
    finally:
        if(conexao):
            cursor.close()
            conexao.close()

#função para incluir novos registros
   # def inserir_registros():
        
    #    criar_tabela()
     #   inserir_registros()
