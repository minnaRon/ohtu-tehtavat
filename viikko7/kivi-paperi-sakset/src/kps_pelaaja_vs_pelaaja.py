from kivi_paper_sakset import KPS

class KPSPelaajaVsPelaaja(KPS):
        
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")

        return tokan_siirto

    @staticmethod
    def luo_kaksinpeli():
        return KPSPelaajaVsPelaaja()
        