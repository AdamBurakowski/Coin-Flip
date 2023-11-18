import os


flips = [] # list of all flips
folder = os.listdir("C:\\Users\\PC\\Desktop\\Python\\coin flip\\Data") # folder with data
print(folder)

# opening every txt file in data folder and adding flips to the list

iteration = 1
for file in folder:
    with open (f"C:\\Users\\PC\\Desktop\\Python\\coin flip\\Data\\{file}", "r") as x:
        for line in x.readlines():
            flips.append(line)
# reformating the data to make everything look cleaner
data = []
for outcome in flips:
    WhatWeNeed = outcome.replace("\n","")
    data.append(WhatWeNeed)
heads = data.count("0")
hstreak = 0
hhstreak = 0
tails = data.count("1")
tstreak = 0
htstreak = 0

numofthrows = len(data)

# counting highest streak of both heads and tails

for record in data:
    if record == "0":
        tstreak = 0
        hstreak += 1
        if hstreak > hhstreak:
            hhstreak = hstreak
    else:
        hstreak = 0
        tstreak += 1
        if tstreak > htstreak:
            htstreak = tstreak

print("Number of times coin was flipped: " + str(numofthrows))
print("Number of Heads: " + str(heads) + ", Number of Tails: " + str(tails))
print("Percent of Heads: " + str(heads/numofthrows*100) + "%, Percent of Tails: " + str(tails/numofthrows*100) + "%")
print("Highest consequtives Heads throws in a row: " + str(hhstreak) + ", Highest consequtives Heads throws in a row: " + str(htstreak))