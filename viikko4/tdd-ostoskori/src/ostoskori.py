from tuote import Tuote
from ostos import Ostos
from functools import reduce

class Ostoskori:
    def __init__(self):
        self.__kori = []

    def tavaroita_korissa(self):
        return reduce(lambda sum, ostos : sum + ostos.lukumaara(), self.__kori, 0)

    def hinta(self):
        return reduce(lambda sum, ostos : sum + ostos.hinta(), self.__kori, 0)

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.__kori:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self.__kori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.__kori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                self._poista_ostos_jos_tuotteen_lkm_nolla(ostos)

    def tyhjenna(self):
        self.__kori = []

    def ostokset(self):
        return self.__kori

    def _poista_ostos_jos_tuotteen_lkm_nolla(self, ostos):
        if ostos.lukumaara() == 0:
            self.__kori.remove(ostos)
