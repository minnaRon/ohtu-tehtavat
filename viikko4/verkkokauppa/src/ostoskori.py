class Ostoskori:
    def __init__(self):
        self._tuotteet = []
    
    def lisaa(self, tuote):
        self._tuotteet.append(tuote)
    
    def poista(self, tuote):
        #self._tuotteet = list(
        #    filter(lambda t: t.id != tuote.id, self._tuotteet)
        #)
        
        #poistetaan vain yksi tuote -ei kaikkia samoja tuotteita
        item = list(filter(lambda t: t.id == tuote.id, self._tuotteet))[0]
        self._tuotteet.remove(item)

    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
