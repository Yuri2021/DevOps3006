welcome = input("Enter your name: ")
print("Hello  and welcome to the World of Games Here you can find many cool games to play")
load_game = "1 Memory Game", " 2 Guess Game", " 3 Currency Roulette"
print(load_game)
game_enter=input( "ENTER NUMBER FROM 1 TO 3")

game_enter = int(game_enter)


def raw_input(param):
    pass


number = raw_input("> ")

if number in range(1, 3):
    print ("You entered a number in the range of 1 to 3")
elif number in range(6, 10):
    print ("You entered a number in the range of 4 to 10")
else:
    print ("Your number wasn't in the correct range")





import random

num = random.randint in range (1,5)
guess = None

while guess != num:
    guess = input(" Pleas shoos game difficulty from 1 to 5 ")
    guess = int(guess)

    if guess == guess:

        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")
