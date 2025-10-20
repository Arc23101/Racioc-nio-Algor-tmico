##Funções
import random
##1
    
x = 1
def Even(x):
    while x < 100:
        print(x)
        x+= 2
Even(x)

##2
hoursDay = 24
Seconds = 0
def calucularHoras ():
    global hoursDay, Seconds
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