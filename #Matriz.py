#Matriz
import random
'''
matrizPrincipal = []
linhaColuna = 0
for n in range (4):
    matrizSecundaria = []
    for i in range (4):
        matrizSecundaria.append(random.randint(0, 10))
    matrizPrincipal.append(matrizSecundaria)
for p in range(len(matrizPrincipal)):
    print(F"{linhaColuna} e {linhaColuna} numero {matrizPrincipal[linhaColuna] [linhaColuna]}")
    linhaColuna +=1
print(matrizPrincipal)
'''

matriz3x3 = []
soma = 0
controleLinha = 0
controleColuna = 0
for n in range (3):
    matrizSecundaria = []
    for i in range (3):
        matrizSecundaria.append(random.randint(0, 10))
    matriz3x3.append(matrizSecundaria)
print(matriz3x3)
for i in range (9):
    soma +=matriz3x3[controleLinha][controleColuna]
    controleColuna += 1
    if controleColuna == 3:
        controleColuna = 0
        controleLinha += 1
print(soma)

