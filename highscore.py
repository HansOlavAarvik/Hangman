from operator import attrgetter
class Highscore:
    def __init__(self):
        self.liste_sekvensar = []
    def sett_inn(self, sekvens):
        self.liste_sekvensar.append(sekvens)
    def skriv_ut(self):
        print("""

         _  _  __  ___  _  _    ____   ___  __  ____  ____
        / )( \(  )/ __)/ )( \  / ___) / __)/  \(  _ \(  __)
        ) __ ( )(( (_ \) __ (  \___ \( (__(  O ))   / ) _)
        \_)(_/(__)\___/\_)(_/  (____/ \___)\__/(__\_)(____)


 """)
        #bruker sortet og posisjon nummer to i sekvensen for å lage ein sortering
        liste = self.liste_sekvensar
        listen = sorted(liste, key=lambda _poengsum: _poengsum[1], reverse=True)
        plassering = 0

        #tekstformatering av representasjonen
        for sekvens in listen:

            plassering += 1
            print("{}. Poengsum:{} Antal spel: {} Namn: {}".format(plassering, sekvens[1],\
             sekvens[2], sekvens[0]))
            print("__________________________________________________________")
