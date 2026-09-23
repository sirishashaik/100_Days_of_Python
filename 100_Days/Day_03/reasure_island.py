print(r'''
*******************************************************************************
          |                   |                  |                     
 _________|________________.=""_;=.___ _________|______________________
|                   |  ,-"_,=""     `"=.|                   |
|___________________|__"=._o`"-._        `"=.___________________________|
          |                `"=._o`"=._      _`"=._                     
 _________|_____________________:=._o " =._."_.-="'"=.___________________|
|                   |    ___.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_.-"  ,. .` ` `` ,  `"-._"-._   ". '  |
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              
 _________|___________| ;`-.o`"=._; ." "`.  "-._ /____/_________________|
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/____
/______/______/______/_"=._o--._        ; | ;        ;;/______/______/___
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/____
/______/______/______/______/____"=._o._| ;_.--"o.--"_/______/______/___
____/______/______/______/______/_____"=.o|o_.--""___/______/______/____
/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    'You\'re at a crossroad, where do you want to go? '
    'Type "left" or "right".\n'
).lower()

if choice1 == "left":

    choice2 = input(
        'You\'ve come to a lake. '
        'There is an island in the middle of the lake. '
        'Type "wait" to wait for a boat. '
        'Type "swim" to swim across.\n'
    ).lower()

    if choice2 == "wait":

        choice3 = input(
            "You arrive at the island unharmed. "
            "There is a house with 3 doors. "
            "One red, one yellow and one blue. "
            "Which colour do you choose?\n"
        ).lower()

        if choice3 == "red":
            print("It's a room full of fire. Game Over.")

        elif choice3 == "yellow":
            print("You found the treasure. You Win!")

        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")

        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")