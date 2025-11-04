# 1. Greet the user
greeting = "Hello! I am MeGPT."

# 1a. Print the greeting
print(greeting)

# 2. Find the name of the uer and remember it
user_name = input("What's your name? ")
print(f"It's nice to meet you, {user_name}!")

# 3. Ask them 3 questions
food = input(f"{user_name}, what is your favorite food?")
print(f"I like eating {food} too!")

country = input(f"{user_name}, which country do you live in? Just asking...")
print(f"{country} is a beautiful place!")

print(f"Thanks {user_name}! I'll keep this is mind next time we chat.")
