#lista 5
import random
'''
#1
matriz4x4 =[]
maioresNumeros = []
linhas = 4
colunas = 4
x = 0
y = -1
soma = 0
for n in range (linhas):
    matrizSecundaria = []
    for i in range (colunas):
        matrizSecundaria.append(random.randint(0, 10))
    matriz4x4.append(matrizSecundaria)
for b in range(linhas):
    numColunas = []
    y += 1
    for r in range(colunas):
        numColunas.append(matriz4x4[x][y])
        x += 1
    x = 0
    numColunas.sort()
    maioresNumeros.append(numColunas[colunas-1])
for o in range(linhas):
    soma += maioresNumeros[o]
soma = soma/linhas

print(F"Matriz: {matriz4x4} \nMaiores numeros de cada coluna: {maioresNumeros} \nMédia: {soma}")

#2
matriz3x3 =[]
linhas = 3
colunas = 3
x = 0
y = 0
for n in range (linhas):
    matrizSecundaria = []
    for i in range (colunas):
        matrizSecundaria.append(random.randint(0, 10))
    matriz3x3.append(matrizSecundaria)
for r in range(linhas*colunas):
    matriz3x3[x][y] = int(input("Digite um numero: "))
    y += 1
    if y > 2:
        y = 0
        x += 1
numMultiplicador = int(input("Digite um numero para servir de multiplicador: "))
x = 0
y = 0
print(matriz3x3)
for r in range(linhas*colunas):
    multiplicado = matriz3x3[x][y] 
    matriz3x3[x][y] = multiplicado * numMultiplicador
    y += 1
    if y > 2:
        y = 0
        x += 1
print(matriz3x3)

#3
matriz4x4 =[]
linhas = 4
colunas = 4
numUsados = (linhas*colunas)
todosNumeros = []
maior = 0
menor = 0
menorVetor =[]
while numUsados > 0:
    matrizSecundaria = []
    for i in range (colunas):
        teste = (random.randint(100, 999))
        if teste not in matriz4x4:
            matrizSecundaria.append(teste)
            numUsados -= 1
            todosNumeros.append(teste)
    matriz4x4.append(matrizSecundaria)
todosNumeros.sort()
maior = todosNumeros[15]

for i in range(linhas):
    for j in range(colunas):
        if matriz4x4[i][j] == maior:
            menor = matriz4x4[i][0]
            for k in range(1,colunas):
                if menor > matriz4x4[i][k]:
                    menor = matriz4x4[i][k]
print (F"Matriz: {matriz4x4} \nMaior elemento: {maior} \nMenor elemento da linha do maior: {menor}")
'''
#4
matriz5x5 =[]
linhas = 5
colunas = 5
versões = ["A", "B", "C", "D"]
for n in range (linhas):
    matrizSecundaria = []
    for i in range (colunas):
        matrizSecundaria.append(random.randint(10, 99))
    matriz5x5.append(matrizSecundaria)
versão = input("Digite a versão, A,B,C,D: ")
while versão not in versões:
    versão = input("Inválida, digite a versão, A,B,C,D: ")
if versão == "A":
    for n in range(linhas):
        for j in range(colunas):
            if not n == 2 and not j == 2:
                matriz5x5[n][j] = "x"

elif versão == "B":
    for n in range(linhas):
        for j in range(colunas):
            if n!= 0 and n != 4:
                    if j !=0 and j!= 4:
                        matriz5x5[n][j] = "x"
elif versão == "C":
    for n in range(linhas):
        for j in range(colunas):




            
elif versão == "D":
    usado = 0
    for n in range(linhas):
        for j in range(colunas):
            if usado == 0:
                matriz5x5[n][j] = "x"
                usado = 1
            else:
                usado = 0






for i in range(linhas):
    print(matriz5x5[i])





