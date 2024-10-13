import random
from random import randrange

spelerNaam = input('Welkom bij de App store! Wat is je naam? ')
print(f'{spelerNaam} wat een mooie naam!')


# Random number spel
def randomNum():
    maxNum = 10

    while True:
        computerNumber = random.randint(1, maxNum)
        lifes = 3
        tries = 0

        print("Typ 'stop' om terug te gaan naar het menu of speel verder door een nummer te raden.")

        while lifes > 0:
            userInput = input("Raad het nummer tussen de 1 en 10:  ")

            if userInput.lower() == 'stop':
                print("Je hebt ervoor gekozen om te stoppen. Terug naar het hoofdmenu.")
                spelKeuze()
                return

            try:
                userInput = int(userInput)

                if userInput < 1 or userInput > maxNum:
                    print(f"Onjuiste invoer. Kies een nummer tussen 1 en {maxNum}.")
                    continue
            except ValueError:
                print("Ongeldige invoer. Voer een getal in.")
                continue

            tries += 1

            if userInput < computerNumber:
                lifes -= 1
                print(f"Sorry {spelerNaam}, dat is te klein. Je hebt nog {lifes} levens over!")
            elif userInput > computerNumber:
                lifes -= 1
                print(f"Sorry {spelerNaam}, dat is te groot. Je hebt nog {lifes} levens over!")
            else:
                print(f"Gefeliciteerd {spelerNaam} je hebt gewonnen! Je hebt het er {tries} pogingen over gedaan!")
                break

        if lifes == 0:
            print(f'Game Over, Je hebt geen levens meer over {spelerNaam}.')

        opnieuw = input(
            "Wil je opnieuw spelen? Typ 'ja' om opnieuw te spelen of 'stop' om terug te gaan naar het menu: ").lower()
        if opnieuw != 'ja':
            spelKeuze()
            return

            # Steen Papier Schaar spel


def Complay():
    randNum = randrange(13)
    if randNum <= 4:
        return 'steen'
    elif randNum > 4 and randNum <= 8:
        return 'papier'
    elif randNum > 8 and randNum <= 12:
        return 'schaar'


def spsSpel(speler, computer):
    computer = Complay()

    if speler == 'steen':
        if computer == 'papier':
            return f'Je hebt verloren, de computer speelde {computer}!'
        if computer == 'steen':
            return f'Je hebt gelijk gespeeld, de computer speelde {computer}!'
        if computer == 'schaar':
            return f'Je hebt gewonnen, de computer speelde {computer}!'

    if speler == 'papier':
        if computer == 'papier':
            return f'Je hebt gelijk gespeeld, de computer speelde {computer}!'
        if computer == 'steen':
            return f'Je hebt gewonnen, de computer speelde {computer}!'
        if computer == 'schaar':
            return f'Je hebt verloren, de computer speelde {computer}!'

    if speler == 'schaar':
        if computer == 'papier':
            return f'Je hebt gewonnen, de computer speelde {computer}!'
        if computer == 'steen':
            return f'Je hebt verloren, de computer speelde {computer}!'
        if computer == 'schaar':
            return f'Je hebt gelijkgespeeld, de computer speelde {computer}!'
    else:
        return 'ongeldige move! typ Steen, Papier of Schaar'


def SteenPapierSchaar():
    win = 0
    loss = 0
    draw = 0
    while True:

        userMove = input(
            "Welke move maak je? Steen, Papier of Schaar (typ 'stop' om te stoppen en terug te gaan naar het keuze menu): ").lower()
        computerMove = ''
        if userMove == 'stop':
            spelKeuze()
            break
        result = spsSpel(userMove, computerMove)

        if 'verloren' in result:
            loss += 1
        elif 'gelijk' in result:
            draw += 1
        elif 'gewonnen' in result:
            win += 1

        print(f'{result} De stand is nu Win: {win}, Losses: {loss}, Draw: {draw}')

        # Galgje spel


def woordKiezer():
    userChoice = input(
        f'Dag {spelerNaam}, Welkom bij galgje! Welk niveau wil je proberen?\nType: Makkelijk, Gemiddeld of Moeilijk: ').lower()

    while True:
        try:
            with open(f'TXT/{userChoice}.txt') as f:
                woorden = f.readlines()
                print(f"Je hebt het {userChoice} niveau gekozen. Succes met galgje!")
                return woorden

        except FileNotFoundError:
            userChoice = input('Ongeldige keuze. Kies opnieuw: Makkelijk, Gemiddeld of Moeilijk: ').lower()


def galgje():
    while True:

        woorden = [s.strip('\n') for s in woordKiezer()]
        woord = random.choice(woorden)
        censWoord = ['-'] * len(woord)
        used = []
        levens = 10

        while levens > 0:
            print(" ".join(censWoord))
            userGuess = input('Welke letter denk je dat erin zit? ').lower()

            if userGuess in used:
                print(f'Je hebt de letter "{userGuess}" al gebruikt.')
            else:
                used.append(userGuess)
                if userGuess in woord:
                    for i, letter in enumerate(woord):
                        if letter == userGuess:
                            censWoord[i] = userGuess

                    if '-' not in censWoord:
                        print(
                            f'Gefeliciteerd {spelerNaam}! Je hebt het woord geraden: {woord} met nog {levens} levens over!')
                        break
                else:
                    levens -= 1
                    print(f'De letter "{userGuess}" zit niet in het woord. Je hebt nog {levens} levens over!')

        if levens == 0:
            print(f'Helaas {spelerNaam}, je hebt geen levens meer! Het woord was: {woord}')

        opnieuw = input(
            "Wil je nog een keer Galgje spelen? Typ 'ja' om opnieuw te spelen of 'nee' om te stoppen: ").lower()
        if opnieuw != 'ja':
            print("Bedankt voor het spelen van Galgje!")
            spelKeuze()


def spelKeuze():
    while True:
        spel = int(input(
            f'In de appstore hebben we verschillende spellen! Welk spel wil je spelen? \ntype "1" voor Raad het getal\ntype "2" voor Steen Papier Schaar\ntype "3" voor galgje '))

        if spel <= 0 or spel > 3:
            spel = int(input('type "1" voor Raad het getal\ntype "2" voor Steen Papier Schaar\ntype "3" voor galgje '))
        else:
            if spel == 1:
                randomNum()
            elif spel == 2:
                SteenPapierSchaar()
            elif spel == 3:
                galgje()


spelKeuze()