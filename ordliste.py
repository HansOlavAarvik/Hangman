from random import choice
from spelord import Spelord
class Ordliste:
    def __init__ (self):

        self._ordliste = []
        self._brukt = []
        # leser inn orda
        tekst=open("ordlisten.txt", "r")
        for linje in tekst:

            termer = linje.split()
            for term in termer:
                self._ordliste.append(Spelord(term))



    def hent_tilfeldig(self):
        tilfeldig = "0"
        # om alle ordene er oppbrukt blir ordene lagt tilbake i ordlista
        if len(self._ordliste) == 0:
            for ordet in self._brukt:
                self._ordliste.append (ordet)
                self._brukt.remove (ordet)
        # velger eit tilfeldig ord med choice og legger den til i liste over
        # brukte ord
        tilfeldig = choice(self._ordliste)
        self._ordliste.remove (tilfeldig)
        self._brukt.append (tilfeldig)
        return tilfeldig
