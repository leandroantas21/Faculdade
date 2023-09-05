import sqlite3 as conector #apelido
def conectar_banco():
#abertura da conexão
    conexao = conector.connect('meu_banco.db')
#aquisição de um cursor
    cursor = conexao.cursor()
#execução de comandos SQL
#cursor.execute("instrução SQL")
    cursor.fetchall() #todos os registros retornados
#efetivação do comando (para atualizar)
    conexao.commit()
#fechamento do ponteiro e da conexão
    cursor.close()
    conexao.close()
#chamada da função
print('Abrindo uma conexão de BD')
conectar_banco()
#encerrando
print('Encerrando a conexão')