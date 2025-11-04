
# Tyson's choose your own adventure
# The Lemonade stand

import os
import time

# Part 1: Intro from Landlord

print("Hello user! It appears the rent is due today, and you owe me money. And the 20$ you have is NOT enough...")
time.sleep(10)
print("So, with that 20 dollars, if you set up a lemonade stand, you can turn 20$ into 40, 50, 100... who knows.")
time.sleep(10)
print("So get to it! At the local Food-Mart, I hear they have your ingredients for sale.")
time.sleep(10)
print("One more thing... You only have 20 dollars. So spend it wisely. And by the end of the day, I want 50.")
time.sleep(20)
# User goes to Food-Mart
os.system("clear")

# Part 2: The Store

print("It seems that each lemon is 1 dollar, a bag of sugar is 5 dollars, and 25 cups are 5 dollars... but I'm selling my lemonade for 2 dollars?")
time.sleep(1)
print("Press 1 for sugar, 2 for lemons, 3 for cups, and 4 to leave.")
choice = input

store = {
    "sugar": 1,
    "lemons": 1,
    "cups": 20
}

inventory = {
    "sugar": 0
}

if choice == "1":
    print("You got one lemon.")
    inventory["lemon"] += 1

elif choice == "2":
    print("You got 1 bag of sugar.")
    inventory["sugar"] += 1

elif choice == "3":
    print("You got 25 cups.")
    inventory["cups"] += 1

else:
    print("Looks like I've bought enough...")

# Part 3: Money Talks

# Ask user to set up the stand

print("Enough shopping. Time to sell!")
if inventory == ("lemon" <= 6):
    print("You did not make enough money because your lemonade was not sour enough! You must restart.")
elif inventory == ("lemon" >= 10):
    print("You did not make enough money because your lemonade was too sour! You must restart.")
else inventory == ("lemon")
    print("The lemonade was just sour enough!")

if inventory == ("sugar" >= 2):
    print("You did not make enough money because your lemonade was too sweet! You must restart.")
elif inventory == ("sugar" <= 0):
    print("You did not make enough money because your lemonade was not sweet enough! You must restart.")
else inventory == ("sugar")
    print("The lemonade was just sweet enough.")

if inventory == ("cups" <= 1):
    print("You did not make enough money because you did not have enough cups! You must restart.")
else inventory == ("cups")
    print("You had enough cups for the lemonade.")
