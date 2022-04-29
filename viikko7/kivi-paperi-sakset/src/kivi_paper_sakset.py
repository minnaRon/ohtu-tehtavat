from tuomari import (
    tuomari as default_tuomari
)

class KPS:

    def pelaa(self, tuomari = default_tuomari):
        self._tuomari = tuomari

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self._tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
