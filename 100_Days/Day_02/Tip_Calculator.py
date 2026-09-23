print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? RS "))

tip = int(input("What percentage tip would you like to give? 5, 10, or 15? "))

people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
split_bill = total_bill / people

print(f"Each person should pay: ₹{split_bill:.2f}")