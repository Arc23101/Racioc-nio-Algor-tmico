##TDE Listas 4
import random
#1
for num in range (1, 11):
    for numMultiplicado in range(1, 11):
        print(f"{num} X {numMultiplicado} = {num*numMultiplicado}")

#2
num = 1
numMultiplicado = 1
while num <=10 and numMultiplicado <= 10:
    print(f"{num} X {numMultiplicado} = {num*numMultiplicado}")
    numMultiplicado += 1
    if numMultiplicado > 10:
        numMultiplicado = 1
        num += 1

#3
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite um numero inteiro: "))
num3 = int(input("Digite um numero inteiro: "))
somaDo2E3 = num2 + num3
if num1 > somaDo2E3:
    print(F"Primeiro numero é maior que a soma do segundo com o terceiro")
else:
    print(F"Primeiro numero não é maior que a soma do segundo com o terceiro")
    
#4
valor1 = int(input("Digite um numero: "))
valor2 = int(input("Digite um numero: "))
print(F"Essa é a soma deles: {valor1 + valor2} \nEssa é a multiplicação deles: {valor1 * valor2} \nE essa é a divisão deles: {valor1/valor2}")

#5
somaDosPares = 0
for i in range (4):
    numVerificado = int(input("Digite um numero: "))
    if numVerificado %2 == 0:
        somaDosPares += numVerificado
print(F"A soma dos pares é {somaDosPares}")

#6
numTriangular = int(input("Digite um numero inteiro não negativo: "))
comparção1 = 1
comparção2 = 2
comparção3 = 3
tentativas = 1
resultadoComparação = 6
while resultadoComparação < numTriangular:
    resultadoComparação = comparção1 * comparção2 * comparção3
    if tentativas == 1:
        tentativas += 1
        comparção1 += 3
    elif tentativas == 2:
        tentativas +=1
        comparção2 += 3

    elif tentativas == 3:
        tentativas = 1
        comparção3 += 3
if resultadoComparação == numTriangular:
    print("O numero é triangular")
else: 
    print("O numero não é triangular")

#7
listaDaAmplitude =[]
for vezes in range(10):
    listaDaAmplitude.append(random.randint(0, 100))
listaDaAmplitude.sort()
amplitude = listaDaAmplitude[9] - listaDaAmplitude[0]
print(F"Valor máximo {listaDaAmplitude[9]}, valor minímo {listaDaAmplitude[0]}, amplitude {amplitude}")

#8
listaDeNumeros = []
for vezes in range(10):
    listaDeNumeros.append(random.randint(0, 100))
listaDeNumeros.sort()
numeroEscolhidoPlayer = int(input("Digite um numero para ver se ele esta na lista, de 0 a 100: "))
if numeroEscolhidoPlayer in listaDeNumeros:
    for i, numeros in enumerate(listaDeNumeros):
        if numeros == numeroEscolhidoPlayer:
            print(F"Ele esta na lista e esta na posição {i + 1}")
    print(listaDeNumeros)
else:
    print("Ele não esta na lista")

#9
vLido = []
for i in range(10):
    vLido.append(random.randint(1,1000))
vPar = []
vImpar = []
for i, numeros in enumerate (vLido):
    if (vLido[i] % 2) == 0:
        vPar.append(vLido[i])
    else:
        vImpar.append(vLido[i])
vLido.sort()
vPar.sort()
vImpar.sort()
print(F"Numeros {vLido} \nPares {vPar} \nÍmpares {vImpar}")

#10
numerosAleatorios = []
numerosAleatoriosOrganizados = []
for i in range(10):
    numerosAleatorios.append(random.randint(1,1000))
for i, num in enumerate (numerosAleatorios):
    if (numerosAleatorios[i] % 2) == 0:
        numerosAleatoriosOrganizados.insert(0, numerosAleatorios[i])
    else: 
        numerosAleatoriosOrganizados.append(numerosAleatorios[i])
print(F"Numeros {numerosAleatorios} \nNumeros organizados em pares e ímpares {numerosAleatoriosOrganizados}")

#11
numMegasena = [100,100,100,100,100,100]
numMegaUsados = [110,110,110,101,110,101]
indice = 0
while indice < len(numMegasena):
    numMegasena[indice] = random.randint(1,60)
    while numMegasena[indice] in numMegaUsados:
        numMegasena[indice] = random.randint(1,60)
    numMegaUsados[indice] = numMegasena[indice]
    indice += 1
indice = 0
meusNumeros = [0,0,0,0,0,0]
while indice < len(meusNumeros):
    meusNumeros[indice] = int(input("Digite seus numeros da megasena: "))
    while meusNumeros[indice] < 0 and meusNumeros[indice] > 60:
        meusNumeros[indice] = int(input("Erro \nDigite seus numeros da megasena novamente: "))
    indice += 1
acertos = 0
indice = 0
while indice < 6:
    if meusNumeros[indice] in numMegasena:
        acertos += 1
    indice += 1
print(F"Esses foram os numeros sorteados: {numMegasena} \nVocê jogou {meusNumeros} \nVocê acertou {acertos}")

#12
vetor20Desorganizado = []
vetor20Organizado = []
numeroVerificado = 0
localSerColocado = 0
for i in range(20):
    vetor20Desorganizado.append(random.randint(1, 1000))
for numero in vetor20Desorganizado:
    pos = 0
    while pos < len(vetor20Organizado) and numero > vetor20Organizado[pos]:
        pos += 1
    vetor20Organizado.insert(pos, numero)
print(F"{vetor20Desorganizado} \n{vetor20Organizado}")



    
