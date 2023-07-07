# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

yearsLeft = 90 - int(age)
days = yearsLeft * 365
weeks = yearsLeft * 52
months = yearsLeft * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left")
