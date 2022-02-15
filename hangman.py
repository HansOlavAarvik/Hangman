from highscore import Highscore
from spillsekvens import Spillsekvens
import sys


# menyen
class Main:
    def __init__(self):
        #ordliste = Ordliste()
        life = 42
        highscore = Highscore()
        # den kjører heilt til bruker skrur den av
        while life == 42:
            print("""
                1. Spel ein runde
                2. Vis high score
                3. Avslutt \n""")
            i = int(input())
            if i == 1:

                spillsekvens = Spillsekvens()
                spillsekvens.start()
                sekvensen = spillsekvens.__repr__()
                highscore.sett_inn(sekvensen)

            elif i == 2:
                highscore.skriv_ut()

            else:
                sys.exit()

main = Main()
main
