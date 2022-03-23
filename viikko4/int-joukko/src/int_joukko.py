KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if self. parametri_ok(kapasiteetti):
            self.kapasiteetti = kapasiteetti
        
        if self.parametri_ok(kasvatuskoko):
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, uusi_alkio): 
        return uusi_alkio in self.ljono

    def lisaa(self, uusi_alkio):
        if not self.kuuluu(uusi_alkio):
            self.ljono[self.alkioiden_lkm] = uusi_alkio
            self.alkioiden_lkm += 1
            self.tarkista_taulukon_koko()
            return True
        return False

    def poista(self, alkio):
        if self.kuuluu(alkio):
            self.ljono.remove(alkio)
            self.alkioiden_lkm -= 1
            return True 
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[0:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        return str(self.ljono[0:self.alkioiden_lkm]).replace("[", "{").replace("]", "}")
       
    def parametri_ok(self, object):
        if not isinstance(object, int) or object < 0:
            raise Exception("parametriksi annettu arvo ei ollut positiivinen kokonaisluku")  # heitin vaan jotain :D ..ei voi poistaa.. :D
        return True

    def tarkista_taulukon_koko(self):
        if self.alkioiden_lkm == len(self.ljono):
                self.ljono += [0] * self.kasvatuskoko
