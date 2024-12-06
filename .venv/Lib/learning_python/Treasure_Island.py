print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Thanmai]
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
enter_a=input("You're at a cross road. Where do you want to go?\n  Type \"left\" or \"right\"\n")#.lower
if enter_a == "left" or enter_a == "Left" or enter_a == "LEFT":
    enter_b=input("You've come to a lake. There is an island in the middle of the lake.\n  Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if enter_b == "wait" or enter_b == "Wait" or enter_b == "WAIT":
        enter_c=input("You arrive at the island unharmed. There is a house with 3 doors. \nOne red, one yellow and one blue. Which colour do you choose?\n")
        if enter_c == "red" or enter_c == "Red" or enter_c == "RED":
            print("It's a room full of fire. Game Over.")
        elif enter_c == "yellow" or enter_c == "Yellow" or enter_c == "YELLOW":
            print("You found the treasure! You Win!")
        elif enter_c == "blue" or enter_c == "Blue" or enter_c == "BLUE":
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")



