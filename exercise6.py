# A simple python program to check the bmi weight of a person
weight = 85
height = 1.85

bmi = weight / (height ** 2)
if bmi<18.5:
    print("under weight")
elif bmi>18.5 and bmi<25:
    print("normal weight")
else:
    print("over weight")
