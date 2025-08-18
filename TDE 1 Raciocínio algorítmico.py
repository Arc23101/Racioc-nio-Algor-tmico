print("Digite um numero: ")
Num1 = int(input())
Num2 = (Num1 - 1)
Num3 = (Num1 + 1)
print (f"anterior = {Num2}, Seu numero = {Num1}, Próximo numero =  {Num3}")

Nascimento = int(input("Digite seu ano de nascimento: "))
NossoAno = int(input("Digite qual ano estamos: "))
Idade = NossoAno - Nascimento
print ("Sua idade até o final do ano é: " + f"{Idade}")

Salario = int(input("Digite seu salário professor: "))
SalariosMinímos = Salario/1412
print ("Seu salário em salários minímos de 2024 é: " + f"{SalariosMinímos}")

vProduto = int(input("Digite o valor do produto: "))
vVista = (vProduto - (vProduto/20))
vDuasVezes = (vProduto/2)
vTresVezes = ((vProduto + (vProduto/20))/3)
print("A vista o valor é: " + f"{vVista}", "O valor em 2 parcelas é: " + f"{vDuasVezes}", "cada. E o valor em 3 vezes é: " + f"{vTresVezes}" + "cada parcela")

Km = int(input("Quanto KM você andou? "))
Litros = int(input("Quantos litros foram consumidos? "))
Media = (Km/Litros)
print("Sua média é de: " + f"{Media}")

import math 
vLata = 50
Raio = float(input("Qual o raio do cilindro(metros): "))
Altura = float(input("Qual a altura(metros): "))
areaEmMetros = ((3.14 * (Raio * Raio) * 2) + (2 * 3.14 * Raio * Altura))
LitrosLata = 5
LitroMetro = 3
NumLatas = ((areaEmMetros/LitroMetro)/LitrosLata)
NumLatasArredondado = (math.ceil(NumLatas))
vGastoLatas = (NumLatasArredondado) * vLata
print("Aqui esta o numero de latas arredondando para cima: " + f"{NumLatasArredondado}" + " e este é o valor a ser gasto em reais: "  + f"{vGastoLatas}")


