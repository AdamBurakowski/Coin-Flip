import random
import os

folder = os.listdir("C:\\Users\\PC\\Desktop\\Python\\coin flip\\Data")
outcomes = []
flips = int(input("How many times do you want to flip a coin? "))
numoftimes = int(input("how many files do you want to generate? "))
for file in range(1, numoftimes+1):
    files = os.listdir("C:\\Users\\PC\\Desktop\\Python\\Coin flip\\Data")
    for add in range(0, flips):
        outcomes.append(random.randint(0,1))
    with open (f"C:\\Users\\PC\\Desktop\\Python\\Coin flip\\Data\\Flips{len(files)+1}.txt", "x") as x:
        for number in outcomes:
            x.write(str(number))
            x.write("\n")
    outcomes.clear()