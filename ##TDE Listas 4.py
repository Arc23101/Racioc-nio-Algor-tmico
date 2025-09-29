##TDE Listas 4
#1
'''
for num in range (1, 11):
    for numMultiplicado in range(1, 11):
        print(f"{num} X {numMultiplicado} = {num*numMultiplicado}")
'''
#2
for num in range (1, 11):
    numMultiplicado = 1
    if numMultiplicado <= 10:
        print(f"{num} X {numMultiplicado} = {num*numMultiplicado}")
        numMultiplicado += 1

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
    if numVerificado




