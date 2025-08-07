print("Digite um numero: ")
Num1 = int(input())
Num2 = (Num1 - 1)
Num3 = (Num1 + 1)
print ("anterior = " + F"{Num2}", "Seu numero = " + F"{Num1}", "Próximo numero = " + F"{Num3}")

print ("Digite seu ano de nascimento: ")
Nascimento = int(input())
print ("Digite qual ano estamos: ")
NossoAno = int(input())
Idade = NossoAno - Nascimento
print ("Sua idade até o final do ano é: " + f"{Idade}")

print ("Digite seu salário professor: ")
Salario = int(input())
SalariosMinímos = Salario/1412
print ("Seu salário em salários minímos de 2024 é: " + f"{SalariosMinímos}")

print("Digite o valor do produto: ")
vProduto = int(input())
vVista = (vProduto - (vProduto/20))
vDuasVezes = (vProduto/2)
vTresVezes = ((vProduto + (vProduto/20))/3)
print("A vista o valor é: " + f"{vVista}", "O valor em 2 parcelas é: " + f"{vDuasVezes}", "cada. E o valor em 3 vezes é: " + f"{vTresVezes}" + "cada parcela")

print("Quanto KM você andou? ")
Km = int(input())
print("Quantos litros foram consumidos? ")
Litros = int(input())
Media = (Km/Litros)
print("Sua média é de: " + f"{Media}")

import math 
vLata = 50
print("Qual o raio do cilindro(metros): ")
Raio = float(input())
print("Qual a altura(metros): ")
Altura = float(input())
areaEmMetros = ((3.14 * (Raio * Raio) * 2) + (2 * 3.14 * Raio * Altura))
LitrosLata = 5
LitroMetro = 3
NumLatas = ((areaEmMetros/3)/5)
NumLatasArredondado = (math.ceil(NumLatas))
vGastoLatas = (NumLatasArredondado) * 50
print("Aqui esta o numero de latas arredondando para cima: " + f"{NumLatasArredondado}" + " e este é o valor a ser gasto em reais: "  + f"{vGastoLatas}")


