#from  hangman import Ordliste e
import re
# Bruker attrgetter for å få ta i nøkkel attributten
from operator import attrgetter


class Spelord:
    def __init__(self, ordet):

        self._ordet = ordet

    def spel(self):

        # lengde er ganske sentral i spel(), siden det er lik poenget for ordet
        lengde = len(self._ordet)

        # her blir hintet blir lagd, ved å legge til _ som bokstaver som ikkje
        # er brukt
        hint = []
        for ord in self._ordet:
            hint.append("_ ")
        strint=''.join(hint)
        print (strint)

        # her blir tap og vinn parametrene satt
        # når riktig eller taper er 0, er spelet over
        riktig = lengde
        taper = 10


        #her er input løkken, den er ganske komplisert siden det berre er single
        # bokstavar som ikkje er brukt blir lagd
        brukte_abc = []
        while riktig > 0 and taper > 0:


            feil = "ja"
            while feil == "ja":
                bruker_input = input("Gjett ein bokstav\n")
                if not re.match("[a-å,ø,æ,è]", bruker_input):
                    print ("Berre a-å gyldig\n")

                elif len(bruker_input) > 1:
                    print ("Kun ein bokstav om gangen!\n")

                elif bruker_input in brukte_abc:
                    print("Den har du allerede brukt.\n")

                else:
                    feil = "nei"
                    brukte_abc.append(bruker_input)
                    print("du gjetta",bruker_input)

            # her blir bokstaven analysert, og samanlikna med spelordet
            bokstaver = []
            bokstaver = [pos for pos, char in enumerate(self._ordet) if char\
             == bruker_input]
             # if not bokstaver, dvs det er ingen bokstavar til felles
            if not bokstaver:
                print("Den er ikkje her...")
                taper  -= 1
                print("Du har {} forsøk igjen\n".format(taper))
                print(strint,"\n")

            else:
                print("Du traff")
                riktig -= len(bokstaver)
                # Skal bytte ut _ med den riktige bokstaven, ved å bruke
                # bokstaver som index
                #for (index, nytt_ord) in zip(bokstaver, bruker_input):
                #    hint[index] = nytt_ord
                for index in bokstaver:
                    hint[index] = bruker_input
                #string = string + hint
                strint=''.join(hint)
                print(strint,"\n")

            # om man bruker opp alle forsøk
            if taper == 0:
                print("Game over!\n")

                print("""
      (/)
       (/)
        (/)
       (/)
        (/)
       (/)
       (/))
      (/)(/)
     (/)'`(/)
    (/)    (/)
    (/)    (/)
    (/)    (/)
    (/)    (/)
     (/)  (/)
      (/)(/)
       `""`
                """)
                print("Ordet var,", self._ordet)
                return 0
            elif riktig == 0:
                print ("""

______                          _     _
|  _  \                        | |   | |
| | | |_   _  __   ____ _ _ __ | |_  | |
| | | | | | | \ \ / / _` | '_ \| __| | |
| |/ /| |_| |  \ V / (_| | | | | |_  |_|
|___/  \__,_|   \_/ \__,_|_| |_|\__| (_)


                """)
                return lengde




