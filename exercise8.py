# A simple python program for ticketing in roller coaster
height= int(input("Enter a number:"))

if height >= 120:

      print("you can run the roller coaster")
      age = int(input("Enter the age of a person:"))
      if(age<12):
          bill = 5
          print("the amount is $5")
      elif(age>12 and age<18):
          bill = 7
          print("the amount is $7")
      elif age >= 45 and age <= 55:
          print(f"The amount is {0}")
      else:
          bill = 12
          print("The amount is$12")
      photo = input("Do you want photo copy. if yes type Y or N")


      if(photo == 1):
          bill = bill + 3


          print(f"The total bill is {bill}")
else:

      print("You cannot ride the roller coaster")
