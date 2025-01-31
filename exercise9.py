# A simple python program for pizza delivery
print("Welcome to the python pizza Delivery ")
size = input("What size do you want? S, M or L ?")
bill = 0
if size == "S":
    bill = 12
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
pepperoni = input("If you want pepperoni type y:")
if pepperoni == "y":
    if pepperoni == "S":
        bill += 2
    else:
        bill += 3
cheese = int(input("If you want cheese type 1"))
if cheese == 1:
    bill += 1

print(f"The total bill for the pizza is {bill}")



