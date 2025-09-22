##Listas e vetores
import random
'''
listaNumeros = [0,0,0,0,0,0,0,0,0,0]
indice = 0
while indice < 10:
    listaNumeros[indice] = int(input("Digite um numero: "))
    indice += 1
indice = 0
while indice < 10:
    print (listaNumeros[indice])
    indice += 1

indice = 0
vogais = ['A','a','E','e','I','i','O','o','U','u']
numVogais = 0
palavra = input("Digite uma palavra: ")
while indice < len(palavra):
    if palavra[indice] in vogais:
        numVogais +=1
    indice += 1
print (numVogais)

continuar = 1
numModificado = 0
while continuar > 0:
    numModificado = int(input("Qual numero da lista você gostaria de modificar: "))
    while numModificado > len(listaNumeros) or numModificado < 0:
        numModificado = int(input("Erro \nQual numero da lista você gostaria de modificar: "))
    listaNumeros[numModificado] = int(input("Digite um numero: "))
    continuar = int(input("Gostaria de modificar outro numero? Se sim digite 1, se não digite 0: "))
    while continuar > 1 or continuar < 0:
        continuar = int(input("Erro digite novamente \nGostaria de modificar outro numero? Se sim digite 1, se não digite 0: "))
indice = 0  
while indice < len(listaNumeros):
    print(listaNumeros[indice])
    indice += 1

numParaMedia = [1,2,3,4]
total = 0
indice = 0
while indice < len(numParaMedia):
    total += (numParaMedia[indice])
    indice += 1
total = total / (len(numParaMedia))
print(f"Media dos numeros {total}")

indice = 0
listaNumAleatorios = [0,0,0,0,0]
somaPar = 0
somaImpar = 0
while indice < len(listaNumAleatorios):
    listaNumAleatorios[indice] = random.randint(0,9)
    if listaNumAleatorios[indice]% 2 == 0:
        somaPar += listaNumAleatorios[indice]
    else:
        somaImpar += listaNumAleatorios[indice]
    indice += 1
indice = 0
while indice < len(listaNumAleatorios):
    print (listaNumAleatorios[indice])
    indice += 1
print (f"{somaPar} soma do pares")
print (f"{somaImpar} soma do ímpares")

lista100 = []
indice = 0
while indice < 100:
    lista100.append(random.randint(0, 100))
    indice += 1
lista100.sort()
indice = 0
while indice < 100:
    print (lista100[indice])
    indice += 1
'''
numMegasena = [100,100,100,100,100,100]
indice = 0
while indice < len(numMegasena):
    numMegasena[indice] = random.randint(1,60)
    indice += 1
indice = 0
meusNumeros = [0,0,0,0,0,0]
while indice < len(meusNumeros):
    meusNumeros[indice] = int(input("Digite seus numeros da megasena: "))
    while meusNumeros[indice] < 0 or meusNumeros[indice] > 60:
        meusNumeros[indice] = int(input("Erro \nDigite seus numeros da megasena novamente: "))
    indice += 1
acertos = 0
indice = 0
while indice < 6:
    if meusNumeros[indice] in numMegasena:
        acertos += 1
    indice += 1
print(F"Esses foram os numeros sorteados: {numMegasena} \nVocê jogou {meusNumeros} \nVocê acertou {acertos}")

