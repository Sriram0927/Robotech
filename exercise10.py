# simple python program using random function
import random
friends = ["Alice","Bob","Charlie","David","Emanuel"]

choice = random.randint(1,5)

if choice == 1:
    print("Alice")
elif choice == 2:
    print("Bob")
elif choice == 3:
    print("Charlie")
elif choice == 4:
    print("David")
elif choice == 5:
    print("Emanuel")
else:
    print("Enter correct value")