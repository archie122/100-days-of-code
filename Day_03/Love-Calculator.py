# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = (name1 + name2).lower()

num1 = names.count("t") + names.count("r") + names.count("u") + names.count("e")

num2 = names.count("l")+ names.count("o")+ names.count("v") + names.count("e")

total = int(str(num1) + str(num2))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")