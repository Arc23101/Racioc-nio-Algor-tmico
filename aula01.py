Nome = str(input("Digite seu nome: "))
print ("Digite sua CPF:")
Cpf = str(input())
print ("Digite seu telefone:")
Telefone = str(input())
print ("Digite seu ano de nascimento:")
Nascimento = int(input())
print("Seus dados:")
print("Nome: " + Nome)
print("Cpf: " + Cpf)
print("Telefone: " + Telefone)
print("Nascido em:"+ f"{Nascimento}")
print ("Digite seu peso:")
Peso = float(input())
print ("Digite sua altura:")
Altura = float(input())
Imc = str(Peso/(Altura * Altura))
print ( Nome + " seu IMC é:", Imc )

print ("Digite qual ano estamos:")
NossoAno = int(input())
Idade = NossoAno - Nascimento
print (f"Sua idade até o fim do ano é: {Idade}")

Dias = int(input("quantos dias você ficou com o carro"))
ValorSerPago = (Dias * 100)
print ("isso é quanto voce deve pagar: " + f"{ValorSerPago}")


TempAtualCelsius = float(input("temperatura atual em celsius: ")))
Tempfahrenheit = (TempAtualCelsius * 9/5) + 32
print (f"Sua temperatura em fahrenheit é: {Tempfahrenheit} F")



print ("Digite suas notas")
Nota1 = int(input("Nota 1: "))
Nota2 = int(input("Nota 2: "))
Nota3 = int(input("Nota 3: "))
Nota4 = int(input("Nota 4: "))
MediaSua = str((Nota1 + Nota2 + Nota3 + Nota4)/4)
print (f"Sua média é: {MediaSua}")


IdadeMeses = Idade * 12
print ("sua idade é: " + f"{IdadeMeses}" + " Meses")



