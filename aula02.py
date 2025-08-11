
weight = float(input("Digite o peso em KG do lutador para descobrir sua categoria: "))
if peso < 50:
    print("Categoria palha")
elif 50 <= weight < 60:
    print("Categoria pluma")
elif 60 <= weight < 76:
    print("Categoria leve")
elif 76 <= weight < 88:
    print("Categoria pesado")
else:
    print("Categoria super pesado")


num1 = float(input("Digite 3 números aleatórios e eles serão ordenado do maior para o menor: \nPrimeiro numero: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Terceiro número: "))
if num1 > num2 and  num1> num3:
    first = num1
elif num2 > num1 and  num2 > num3:
    first = num2
else:
    first = num3
if num2 > num1 > num3 or num3 > num1 > num2:
    second = num1
elif num1 > num2 > num3 or num3 > num2 > num1:
    second = num2
else:
    second = num3
if num1 < num2 and num1 < num3:
    third = num1
elif num2 < num1 and num2 < num3:
    third = num2
else:
    terceiro = num3
print(f"Primeiro: {first}, segundo: {second}, terceiro: {third}")


studentScore = float(input("Digite a sua nota: "))
presence = int(input("Agora digite sua presença de 0 a 100: "))
if presence >= 70:
    print("Presença atingida: ")
    presencaAtingida = True
else:
    print("Presença insulficiente. Reprovado")
    presencaAtingida = False
if presencaAtingida and studentScore <= 4:
    print("Conceito: F \nRecuperação")
elif presencaAtingida and 4 < studentScore <= 6:
    print("Conceito: E \nRecuperação")
elif presencaAtingida and 6 < studentScore <= 7:
    print("Conceito: D \nAprovado")
elif presencaAtingida and 7 < studentScore <= 8:
    print("Conceito: C \nAprovado")
elif presencaAtingida and 8 < studentScore <= 9:
    print("Conceito: B \nAprovado")
elif presencaAtingida and 9 < studentScore:
    print("Conceito: A \nAprovado")


currentTimeH = int(input("Digite as horas atuais: "))
currentTimeM = int(input("Agora digite os minutos: "))
pucOpenH = 7
pucOpenM = 30
pucCloseH = 23
pucCloseM = 10
if (8 < currentTimeH < 23):
    print("Puc esta aberta")
elif pucOpenH == currentTimeH and pucOpenM < currentTimeM:
    print("Puc esta aberta")
elif currentTimeH == pucCloseH and currentTimeM < pucCloseM:
    print("Puc esta aberta")
else:
    print("Puc esta fechada")