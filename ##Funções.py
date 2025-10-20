##Funções
import random
##1
'''
x = 0
maxNum = 100
def Even(x, maxNum):
    while x < maxNum:
        if  x % 2 == 1:
             print(x)

Even(x, maxNum)

##2

hoursDay = 24
Seconds = 0
def calucularHoras ():
    global Seconds
    if hoursDay > 0:
        Seconds += 60 * 60
        hoursDay -= 1
while hoursDay > 0:
    calucularHoras()
print(Seconds)

##3
fuel = int(input("how many liters were consumed? "))
kilometers = int(input("how many kilometers did you travel? "))
averageConsume = 0
def kilometersPerLiter(distance, gasoline):
    global averageConsume
    averageConsume = distance/gasoline
kilometersPerLiter(kilometers, fuel)
print(F"You're average consume was {averageConsume}")

##4
randomList = []
for i in range(4):
        randomList.append(random.randint(0,100))
randomNumber = random.randint(0,100)
isIn = False
def isInlist(number, lists):
    global isIn
    if number in lists:
          isIn = True
    else:
          isIn = False
isInlist(randomNumber, randomList)
if isIn  == True: 
    print(F"{randomList}, {randomNumber}, is in list")
elif isIn  == False:
    print(F"{randomList}, {randomNumber}, is not in list")
'''
##Calculadora:
inicialNum = 0
secondNum = 0
firstTime = 1
def getOperation():
    global inicialNum
    operation = int(input("What  do you wish to do: to add write 1, to subtract write 2, to multipli write 3, to divide write 4: "))
    if operation == 1:
          inicialNum = inicialNum + secondNum
    elif operation == 2:
          inicialNum = inicialNum - secondNum
    elif operation == 3:
          inicialNum = inicialNum * secondNum
    elif operation == 4:
          inicialNum = inicialNum / secondNum
def getNum():
     global inicialNum, secondNum, firstTime
     inicialNum = int(input("write a number to use: "))
     firstTime = 0
def secondOperation():
     global secondNum
     secondNum = int(input("write a new number to use: "))
while True:
    if firstTime == 1:
        getNum()
    elif firstTime == 0:
        secondOperation()
    getOperation()
    print(F"Result = {inicialNum}")
    firstTime = int(input("Do you wish to reset? 1 to yes, 0 to no(continue with the result of the previous operation): "))