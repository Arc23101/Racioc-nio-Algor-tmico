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

#4
matriz5x5 =[]
linhas = 5
colunas = 5
versões = ["A", "B", "C", "D"]
primeiro = 1
segundo = -1
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
            if not j == primeiro and  not j == segundo:
                        matriz5x5[n][j] = "x"
        primeiro += 1
        segundo += 1
        if primeiro > 4:
            primeiro = -1
        if segundo > 4:
            primeiro = -1  
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

#5
matriz15x7 =[]
matriz15x7Original =[]
linhas = 15
colunas = 7
matrizPar = []
matrizImpar = []
controleColunaPar = 0
controleColunaImpar = 0
for n in range (linhas):
    matrizSecundaria = []
    for i in range (colunas):
        matrizSecundaria.append(random.randint(10, 99))
    matriz15x7.append(matrizSecundaria)
matriz15x7Original = [linha[:] for linha in matriz15x7]
matriz15x7.clear()
for n in range (linhas):
    for i in range (colunas):
        if matriz15x7Original[n][i] % 2 == 0:
            matrizPar.append(matriz15x7Original[n][i])
        else:
            matrizImpar.append(matriz15x7Original[n][i])

for n in range (linhas):
    matrizSecundaria = []
    for i in range (colunas):
        if controleColunaPar < len(matrizPar):
            matrizSecundaria.append(matrizPar[controleColunaPar])
            controleColunaPar += 1
        else:
            matrizSecundaria.append(matrizImpar[controleColunaImpar])
            controleColunaImpar += 1
    matriz15x7.append(matrizSecundaria)
for i in range(linhas):
    print(F"Original: {matriz15x7Original[i]}")
print()
for i in range(linhas):
    print(F"Modificada: {matriz15x7[i]}")

#6
listaCidades = ["Curitiba", "Florianópolia", "Porto Alegre", "São Paulo", "Rio de Janeiro"]
distancia= [
    [0,   310, 716, 408, 852],
    [310, 0,   470, 705, 1144],
    [716, 470, 0,   1119, 1553],
    [408, 705, 1119, 0,   429],
    [852, 1144, 1553, 429, 0]
]
distanciaViagem = 0
velocidade = 100
cidadeInicio = int(input("Digite qual cidade você vai sair, de 0 a 4, Curitiba, Florianópolis, Porto Alegre, São Paulo, Rio de Janeiro: "))
while cidadeInicio > 4 or cidadeInicio < 0:
    cidadeInicio = int(input("Erro,tente novamente. \nDigite qual cidade você vai sair, de 0 a 4, Curitiba, Florianópolis, Porto Alegre, São Paulo, Rio de Janeiro: "))
cidadeDestino = int(input("Digite qual cidade você deseja ir, de 0 a 4, Curitiba, Florianópolis, Porto Alegre, São Paulo, Rio de Janeiro: "))
while cidadeDestino > 4 or cidadeDestino < 0:
    cidadeDestino = int(input("Erro,tente novamente. \nDigite qual cidade você deseja ir, de 0 a 4, Curitiba, Florianópolis, Porto Alegre, São Paulo, Rio de Janeiro: "))
distanciaViagem = distancia[cidadeInicio][cidadeDestino]
if distanciaViagem == 0:
    print(F"Essa será a distancia total da viagem: {distanciaViagem} \nVocê não mudou de cidade")
else:
    print(F"Essa será a distancia total da viagem: {distanciaViagem} \nA 100 km/H(Limite das rodovias federais de pista simples ) você vai levar {distanciaViagem/velocidade} horas")
'''


