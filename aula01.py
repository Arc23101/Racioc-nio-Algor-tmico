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
print (Idade)

print ("quantos dias você ficou com o carro")
Dias = int(input())
ValorSerPago = (Dias * 100)
print ("isso é quanto voce deve pagar: " + ValorSerPago)


print ("temp atual")
TempAtual = int(input())
TempEmFarhenheit = (TempAtual * 9/5) + 32
print (f"{TempEmFarhenheit}" + "F")



print ("Digite suas notas")
print ("Nota 1")
Nota1 = int(input())
print ("Nota 2")
Nota2 = int(input())
print ("Nota 3")
Nota3 = int(input())
print ("Nota 4")
Nota4 = int(input())
MediaSua = str((Nota1 + Nota2 + Nota3 + Nota4)/4)
print (MediaSua)


IdadeMeses = Idade * 12
print ("sua idade é: " + f"{IdadeMeses}" + " Meses")



