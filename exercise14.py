# using python program create a simple password generator
import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbol = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';',  '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to the password generator")
letters = int(input("How many letters would you like to use in the password? \n"))
numerical = int(input(f"How many number would you like to use in the password? \n"))
special = int(input(f"How many symbol would you like to use in the password? \n"))

# Easy level:
password =""

# for char in range(0, letters):
#     password += random.choice(alphabets)
#
# for char in range(0, numerical):
#     password += random.choice(str(numbers))
#
# for char in range(0, special):
#     password += random.choice(symbol)
#
# print(password)

# Hard level:
password_list =[]
for char in range(0, letters):
    password_list.append(random.choice(alphabets))

for char in range(0, numerical):
    password_list.append(random.choice(str(numbers)))

for char in range(0, special):
    password_list.append(random.choice(symbol))

random.shuffle(password_list)


password =""

for char in password_list:
    password += char
print(f"The password is : {password} ")





