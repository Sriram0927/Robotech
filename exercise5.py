# write a simple program to create a tip calculator
print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill?"))
Tip = int((input("How much tip would you like to give?")))
Number = float(input("Number of people splitting the bill?"))
tip = Tip/100
Total = Bill * tip
total = Bill / Number
result = (total + tip)
Result = round(result , 2)
print(f"Each person should pay is {Result}")

