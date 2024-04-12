print("Welcome to the Tip Calculator!")
amount = float(input("What was the total bill amount? ₹"))
tip = int(input("How much tip would you like to give? 0, 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

amount_with_tip = amount + tip/100 * amount
bill = round(amount_with_tip / people, 2)

print(f"Each person should pay {bill} ₹")