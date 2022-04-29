from kivi_paper_sakset import KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def __init__(self):
        super().__init__()
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto

    @staticmethod
    def luo_yksinpeli():
        return KPSTekoaly()
