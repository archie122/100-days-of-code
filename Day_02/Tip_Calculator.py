print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
totalPeople = int(input("How many people to split the bill? "))

tip = round((totalBill / totalPeople) * ((percentage / 100) + 1), 2)
tip = "{:.2f}".format(tip)

print(f"Each person should pay: ${tip}")