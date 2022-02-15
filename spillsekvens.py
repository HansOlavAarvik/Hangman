from ordliste import Ordliste
class Spillsekvens:

    def __init__(self):
        self._ant_spel = 0
        self._brukar_namn = ""
        self._poengsum = 0

    def start(self):
        self._brukar_namn = input("Skriv inn namn: ")
        tap = 0
        #løkke for spelet, spelet kjører heilt til man har spelt 3 gonger
        # (10 blir for mykje), eller man taper eller velger å avslutte
        ordliste = Ordliste()

        while self._ant_spel < 3 and tap == 0:
            #starter eit spel ved å hente eit ord frå ordlista
            runde = ordliste.hent_tilfeldig()

            poengsum = runde.spel()
            self._ant_spel += 1
            # om man vinner eit spel
            if poengsum > 0:
                self._poengsum += poengsum
                # avbryt og gå tilbake til menyen om n, nei
                # kunne lagd dette valget bedre..
                if self._ant_spel < 3:
                    k = input("Vil du fortsette j/n?\n")
                    if k == "j":
                        tap == 0
                    else:
                        tap += 1
            elif poengsum == 0:
                tap += 1

            # repr er interessant, man velger korleis ein skal representere
            # ein instans av ein spelsekvens
            # tok lit tid å få denne til å gå
    def __repr__(self):
        return(self._brukar_namn, self._poengsum, self._ant_spel)
