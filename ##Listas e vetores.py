##Listas e vetores
import random


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
media = total / (len(numParaMedia))
print(f"Media dos numeros {media}")


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


##Desafio
timesValorant = ['loud', 'furia', '2g', 'mibr']
indice = 0 
vidas = 4
letrasErradas = []
letrasAcertadas = []
palavraSorteada = timesValorant[random.randint(0,3)]
letrasCertas = list(palavraSorteada)
revelarLetras = []
acertosNecessarios = 0
resultadoDaRodada = (f"Você tem {vidas} Vidas \nVocê acertou essas letras {letrasAcertadas} \nE usou essas erradas {letrasErradas} \n{revelarLetras}")

while indice < len(palavraSorteada):
    revelarLetras.append("_")
    indice += 1
    acertosNecessarios += 1

while vidas > 0 and acertosNecessarios > 0:
    letraEscolhida = str(input("Digite uma letra minuscula ou numero para tentar acerta qual time do valorant foi escolhido: "))
    if letraEscolhida in letrasCertas and letraEscolhida not in letrasAcertadas:
        for i, letra in enumerate(palavraSorteada):
            if letra == letraEscolhida and revelarLetras[i] == "_":
                revelarLetras[i] = letraEscolhida
                acertosNecessarios -= 1
    else:
       if letraEscolhida not in letrasErradas: 
            letrasErradas.append(letraEscolhida)
            vidas -= 1
    resultadoDaRodada = (f"Você tem {vidas} Vidas \nVocê acertou essas letras {letrasAcertadas} \nE usou essas erradas {letrasErradas} \n{revelarLetras}")
    print(resultadoDaRodada)

if vidas > 0:
    print(F"Você ganho: {resultadoDaRodada} \n{palavraSorteada}")
else: 
    print(F"Você perdeu: {resultadoDaRodada} \n{palavraSorteada}")







