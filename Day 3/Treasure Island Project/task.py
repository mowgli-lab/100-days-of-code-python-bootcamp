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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
import time
print(time.time())
#testing full github link

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn = input('You are at a fork in the road, do you want to turn left or right? ').strip().lower()

if turn == 'left':
    swim_wait = input('You have reached the water, do you want to wait for a boat or swim across. Enter wait or swim? ')

    if swim_wait == 'wait':
        door = input('You have reached three doors, red, blue and yellow, which door do you want to enter? Enter Red, Blue, Yellow: ').lower()

        if door == 'red':
            print('You have been burned by fire, Game Over!')

        elif door == 'blue':
            print('There was a beast on the other side that ate you, Game Over!')

        elif door == 'yellow':
            print('You have won the Treasure Congratulations! You Win!')
    elif swim_wait == 'swim':
        print('You were eaten by a shark, Game Over!')
    else:
        print('Game Over!')
elif turn == 'right':
    print('You were attacked by pirates, Game Over!')
