import math


class Kratka:

    def __init__(self, x=0, y=0, rodzic=None):
        self.x = x
        self.y = y
        self.g = 0.0
        self.h = 0.0
        self.f = 0.0
        self.rodzic = rodzic


    def oblicz_h(self, kratka, cel):
        abs = (kratka.x - cel.x)
        abs2 = (kratka.y - cel.y)
        h = math.sqrt(abs * abs + abs2 * abs2)
        return h


class Mapa:
    def __init__(self, ):
        self.cel = Kratka(19, 19, None)
        self.start = Kratka(0, 0, None)
        self.lista_otwarta = []
        self.lista_zamknieta = [self.start]
        self.mapa = [[0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     ]

        self.aktualnaKratka = self.start
        self.ostatniElement = Kratka()

    def dodajPrzeszkode(self, x, y):
        self.mapa[x][y] = 5

    def pokazMape(self):
        self.mapa[self.start.x][self.start.y] = 1
        self.mapa[self.cel.x][self.cel.y] = 2
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                print(self.mapa[i][j], end=' ')
            print()

    def zmienStart(self, x, y):
        start = Kratka(x, y, None)
        self.lista_zamknieta.remove(self.start)
        self.start = start
        self.aktualnaKratka = start
        self.lista_zamknieta.append(self.aktualnaKratka)
        return start

    def zmienCel(self, x, y):
        cel = Kratka(x, y, None)
        self.cel = cel
        return cel

    def znajdzNajnizszyF(self, ):
        min = self.lista_otwarta[0]
        for i in range(len(self.lista_otwarta)):
            if self.lista_otwarta[i].f < min.f:
                min = self.lista_otwarta[i]
        return min

    def czyJestJuzWliscieZamknietej(self, kratka):
        flaga = False
        for k in self.lista_zamknieta:
            if k.x == kratka.x and k.y == kratka.y:
                flaga = True
                return flaga

    def czyJestJuzWliscieOtwartej(self, kratka):
        flaga = False
        for k in self.lista_otwarta:
            if k.x == kratka.x and k.y == kratka.y:
                flaga = True
                return flaga

    def dodajSasiada(self):
        kratka = Kratka()
        for i in range(1, -2, -1):
            for j in range(-1, 2):
                if (i != 0 and j != 0) or (i == 0 and j == 0):
                    continue
                if self.aktualnaKratka.x + i >= 0 and self.aktualnaKratka.x + i < len(
                        self.mapa[0]) and self.aktualnaKratka.y + j >= 0 and self.aktualnaKratka.y + j < len(
                    self.mapa[0]) and self.mapa[self.aktualnaKratka.x + i][self.aktualnaKratka.y + j] != 5:
                    kratka = Kratka(self.aktualnaKratka.x + i, self.aktualnaKratka.y + j, self.aktualnaKratka)
                    if self.czyJestJuzWliscieZamknietej(kratka):
                        continue
                    kratka.g = 1 + kratka.rodzic.g
                    kratka.f = kratka.g + kratka.oblicz_h(kratka, self.cel)
                    tempG = self.aktualnaKratka.g + 1
                    if not self.czyJestJuzWliscieOtwartej(kratka):
                        self.lista_otwarta.append(kratka)
                    elif tempG < kratka.g:
                        kratka.rodzic = self.aktualnaKratka
                        kratka.g = tempG
                        kratka.f = kratka.g + kratka.h

    def znajdzDroge(self):
        if self.ostatniElement.x != self.start.x or self.ostatniElement.y != self.start.y:
            print(self.ostatniElement.x, self.ostatniElement.y)
            self.ostatniElement = self.ostatniElement.rodzic
            self.mapa[self.ostatniElement.x][self.ostatniElement.y] = 3
            self.znajdzDroge()
        elif self.ostatniElement.x == self.start.x and self.ostatniElement.y == self.start.y:
            print(self.ostatniElement.x, self.ostatniElement.y)
            self.mapa[self.ostatniElement.x][self.ostatniElement.y] = 1

    def doCelu(self):
        self.dodajSasiada()
        while self.aktualnaKratka.x != self.cel.x or self.aktualnaKratka.y != self.cel.y:
            kratka = self.znajdzNajnizszyF()
            self.aktualnaKratka = kratka
            self.lista_otwarta.remove(kratka)
            self.lista_zamknieta.append(kratka)
            self.dodajSasiada()
        self.ostatniElement = self.lista_zamknieta[len(self.lista_zamknieta) - 1]
        print('DROGA POWROTNA:')
        self.znajdzDroge()


mapa = Mapa()
# mapa.zmienStart(0, 5)
mapa.dodajPrzeszkode(1, 1)
mapa.dodajPrzeszkode(2, 2)
mapa.dodajPrzeszkode(3, 3)
mapa.dodajPrzeszkode(4, 4)
mapa.dodajPrzeszkode(2, 5)
mapa.dodajPrzeszkode(0, 0)
# mapa.zmienCel(5, 0)
mapa.doCelu()
mapa.pokazMape()
