class Viitegeneraattori:
    def __init__(self):
        self._seuraava = 0
        #muutin alustuksen nollaksi, niin viitenumerot alkavat numerosta 1
        #self._seuraava = 1

    def uusi(self):
        self._seuraava = self._seuraava + 1

        return self._seuraava


viitegeneraattori = Viitegeneraattori()
