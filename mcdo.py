# Bot that asks for fries

answer = input("Thanks for giving your order! Do you want fries with that?")

# Verify the answer
if answer.lower() == "yes":
    print("I will add fries to your order.")

elif answer.lower() == "no":
    print("Ok, no fries for you.")

else:
    print("Yes or no only...")
