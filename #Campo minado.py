#Campo minado
import random
campo = []
linhas = 9
colunas = 9
minas = 10
for n in range (linhas):
    matrizSecundaria = []
    for i in range (colunas):
        matrizSecundaria.append(0)
    campo.append(matrizSecundaria)
while minas > 0:
    a = random.randint(0, linhas-1)
    b = random.randint(0, colunas-1)
    if campo [a] [b] == 0:
       campo [a] [b] = 1
       minas -= 1 
for b in range(9):
    print(campo[b])
