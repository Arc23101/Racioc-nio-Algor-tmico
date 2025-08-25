##Aula5
contador = 0
while contador < 10:
    print (contador)
    contador += 1


numTimes = 1
num1 = float(input("write a number to see its multiplications: "))
while numTimes <= 10:
    print (f"{num1} x {numTimes} = {num1 * numTimes}")
    numTimes +=1

score = float(input("Put your score: "))
while score < 7:
    score= int(input("Score to low, put another score: "))
print (f"Your score is: {score}")

num2 = float(input("write a number diferent than -1: "))
num3 = 0
repeatedTimes = 0
while num2 != -1:
    num3 = num3 + num2
    repeatedTimes += 1
    num2 = float(input("write a number again: "))
if repeatedTimes <= 0:
    repeatedTimes = 1
print (f"This is the average of your numbers: {num3/repeatedTimes}")

num4 = int(input("Enter a number to see the value of all the number from 1 to your number added to each other: "))
multiplier = 1
numSoma = 0
while multiplier <= num4:
    numSoma = numSoma + multiplier
    multiplier += 1
print(f"This is the value of all the number from 1 to {num4} added to each other: {numSoma}")

num5 = int(input("Enter 10 numbers: "))
numTotalTimes = 0
numEven = 0
numOdd = 0
while numTotalTimes <= 9:
    numTotalTimes += 1
    testNum = num5 % 2
    if testNum != 1:
        numEven += 1
    else:
        numOdd += 1
    if numTotalTimes < 10:
        num5 = int(input("Enter a number again: "))
print(f"This is the number of even numbers: {numEven}\nAnd this is the number of odd numbers: {numOdd}")
