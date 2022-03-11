class LvLUpException(Exception):
    def __init__(selfself, hibauzenet):
        super().__init__(hibauzenet)


class Tarsas:

    def __init__(self, nev, db, allapot="Jó", ar=1):
        self._nev = nev
        self.db = db
        self.allapot = allapot
        self.ar = ar

    @property
    def nev(self):
        return self._nev

    @nev.setter
    def nev(self, ertek):
        self._nev = ertek

    def __str__(self):
        return f"{self.nev} (Darab: {self.db}) Állapot: {self.allapot}, Ár: {self.ar}"

    def __eq__(self, tarsas):
        if not isinstance(tarsas, Tarsas):
            return False

        return self.nev.lower() == tarsas.nev.lower() and self.db == tarsas.db and self.allapot == tarsas.allapot and self.ar == tarsas.ar

class Szekreny:

    def __init__(self):
        self.tarsasok = []

    def __str__(self):
        if len(self.tarsasok) ==0:
            return "Üres a szekrény!"

    def __add__(self, szekreny):
        if not isinstance(szekreny, Szekreny):
            raise TypeError("Nem szekrény!")

        uj_szekreny = Szekreny()
        uj_szekreny.tarsasok = self.tarsasok + szekreny.tarsasok

    def get_tarsas(self, n):
        if n < 0 or n >= len(self.tarsasok):
            raise LvLUpException("Nono!")

    def atlag_ar(self):
        if len(self.tarsasok) == 0:
            raise LvLUpException("Nincs társas a szekrényben!")

        osszeg = 0
        darabszam = len(self.tarsasok)

        for tarsas in self.tarsasok:
            osszeg += tarsas.ar

        return osszeg / darabszam

    def megvettek(self, tarsas):
        if not isinstance(tarsas, Tarsas):
            raise TypeError("Nem társas!")

        if tarsas not in self.tarsasok:
            raise LvLUpException("Társas nem található!")

        self.tarsasok.remove(tarsas)

if __name__ == "__main__":
    pass

doom = Tarsas("Doom", 1, "Jó", 10000)

print(doom)