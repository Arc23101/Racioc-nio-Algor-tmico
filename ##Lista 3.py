##Lista 3
##1
num1 = 1
while num1 <= 99:
    print(num1)
    num1 += 2
print("End")
##2
num2 = 50
while num2 >= 0:
    print(num2)
    num2 -= 5
print("End")

##3
num3 = -100
while num3 <= 100:
    print (num3)
    num3 += 10
print("End")

##4
num4 = 4
numMultipli = 0
numResult = 0
while numResult < 100:
    numResult = num4 * numMultipli
    print (numResult)
    numMultipli += 1
print("End")

##5
num5 = int(input("Write a limit number: "))
numStart = 1
while numStart <= num5:
    print(numStart)
    numStart += 2
print("End")

##6 
num6 = 2.54
cmPolegada = 1
while cmPolegada <=20:
    print(f"{cmPolegada} Cm = {num6*cmPolegada} Polegadas:")
    cmPolegada += 1
print("End")

##7
milhasMetro = 1609.344
metros = 20000
milhas = 1
while metros <= 160000:
    print(f"{milhas} milhas = {metros * milhasMetro} metros")
    milhas += 1
    metros += 10000
print("End")

##8
num8 = int(input("Write 10 numbers: "))
num8Soma = 0
num8Times = 0
while num8Times <= 9:
    num8Soma += num8
    num8Times += 1
    if num8Times < 10:
        num8 = int(input("Write a number again: "))
print (f"This is what all the numbers combine add to: {num8Soma} \nAnd this is what their average is: {num8Soma/num8Times}")

##9
num9Min = int(input("Write a inicial limit: "))
num9Max = int(input("Write a end limit: "))
num9 = 3
while (num9Min % 3) > 0:
    num9Min -= 1
while num9Min < num9Max:
    if (num9Min + 3) < num9Max:
        print(num9Min + 3)
    num9Min += 3
print("End")

##10
num10 = 



##11
num11Primeiro = 1
num11Segundo = 1
num11SegundoMultipli = 1
while num11Primeiro <=10 and num11SegundoMultipli <= 10:
    print (f"{num11Primeiro} x {num11Segundo * num11SegundoMultipli} = {num11Primeiro * num11Segundo * num11SegundoMultipli} ")
    if num11Primeiro <=9:
        num11Primeiro += 1
    else:
        num11Primeiro = 1
        num11SegundoMultipli += 1
print ("End")


    