import random as rd
import time
print("WELCOME TO DICE GAME\n")

while True:
    guess = int(input("Guess a number in range 1-6 (enter 0 to exit) : \n"))
    randomNumber = rd.randint(1,6)
    if 1 <= guess <= 6:
        if (guess == randomNumber):
            print("\nRandom number = ",randomNumber)
            print("Congrats ! Right guess . ")
        else:
            print("\nRandom number = ",randomNumber)
            print("Wrong guess . Try again ")
    elif ( guess == 0):
        print("exit .. ")
        time.sleep(2)
        break
    else:
        print("Wrong enty !")