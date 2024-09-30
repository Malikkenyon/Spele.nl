import random

userName = input("Enter your name: ")
maxNum = 10
computerNumber = random.randint(0, maxNum)
lifes = 3
tries = 0

while True:
        userInput = int(input("Enter a number between 1 and 10: "))
        if userInput >= maxNum:
                userInput = int(input("Enter a number between 1 and 10: "))

        if userInput < computerNumber:
            lifes -= 1
            tries += 0
            print(f"Sorry {userName}, that's too small. You only have {lifes} lifes left!")
        if userInput > computerNumber:
            lifes -= 1
            tries += 0
            print(f"Sorry {userName}, that's too big. You only have {lifes} lifes left!")

        if userInput == computerNumber:
            print(f"Congrats {userName} +you win! it took you {str(tries)} tries!")
            break
        if lifes == 0:
            print(f'Game Over, you have no lifes left {userName}. Try again')
            break


