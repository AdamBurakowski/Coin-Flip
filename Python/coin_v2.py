import random
import os
i = 0
outcomes = []
flips = input("How many times do you want to flip a coin? ")
files = os.listdir("C:\\Users\\PC\\Desktop\\Python\\Coin flip\\Data")
while(i<int(flips)):
    outcomes.append(random.randint(0,1))
    i+= 1
with open (f"C:\\Users\\PC\\Desktop\\Python\\Coin flip\\Data\\Flips{len(files)+1}.txt", "x") as x:
    for number in outcomes:
        x.write(str(number))
        x.write("\n")