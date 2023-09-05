arquivo = open('crescente.txt','w') 

for elemento in range (1,101):
        arquivo.write (str(elemento) + ';')
arquivo.close