##Recursividade
'''
listaNum = [1,2,3,4,5,6,7,8]
posição = 0
def imprimirNumeros(lista,indice):
    if indice <len(lista):
        print(lista[indice])
        imprimirNumeros(lista,indice+1)
imprimirNumeros(listaNum,posição)
'''
def interativos(n):
    i = n
    if i < 10:
        print(i)
        interativos(n+1)
    else:
        return 0
interativos(10)