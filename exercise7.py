# A simple Treasure game using python
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
direction = input("You're at a cross road. where do you want to go (left or right) ?")
if direction == "left":
    print("swim or wait")
elif direction == "right":
    print("you have fallen into a hole and the game is over")
inform = input()
if inform == "swim":
    print("The game is over")
elif inform == "wait":
    door = input("which door?")
    if door =="red":
        print("Burned by fire. Game Over")
    elif door =="blue":
        print("you have eaten by the beast. Game over")
    elif door =="yellow":
        print("you Won!")
    elif door == "anything else":
        print("Game Over")

