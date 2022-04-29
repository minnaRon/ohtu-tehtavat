from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly

class Kayttoliittyma:

    def tulosta_ohje(self):
        print("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
                )
    
    def suorita(self):

        pelit = {'a': KPSPelaajaVsPelaaja.luo_kaksinpeli(),
                 'b': KPSTekoaly.luo_yksinpeli(),
                 'c': KPSParempiTekoaly.luo_haastava_yksinpeli()
        }

        while True:
            self.tulosta_ohje()
            vastaus = input()
            
            if vastaus in pelit:
                print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )
                peli = pelit[vastaus]
                peli.pelaa()

            else:
                break

