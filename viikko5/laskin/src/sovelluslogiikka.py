class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos_vanha = tulos
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos_vanha = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos_vanha = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos_vanha = self.tulos
        self.tulos = 0

    def kumoa(self):
        self.tulos = self.tulos_vanha

    def aseta_arvo(self, arvo):
        self.tulos = arvo
