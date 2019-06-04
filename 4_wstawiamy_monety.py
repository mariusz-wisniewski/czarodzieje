"""
    Cześć! Witajcie Czarodzieje Kodu!
    Oto piersze linijki kodu naszej gry.
    Poznamy podstawowe tajniki Arcade oraz pierwszy uruchomimy nasz własny program z jego użyciem!
"""
import arcade
import random

WIELKOSC_GRACZA = 1
WIELKOSC_MONET = 0.2
LICZBA_MONET = 50

EKRAN_DLUGOSC = 800
EKRAN_WYSOKOSC = 600


class GraPoszukiwaczaSkarbu(arcade.Window):
    """ Tutaj będziemy konfigurować okno naszej gry.
    Co rozumiemy poprzez konfigurację? Otóż:
        - określenie wielkości ekranu (długość/szerokość)
        - kolory ekranu
        - dodanie naszego gracza (wygląg, zachowanie)
        - dodanie skarbów/monet (wygląd, zachowanie, punkty)
        - tablice wyników"""

    def __init__(self):
        """ Tworzenie naszego okna """
        # Wywołanie mechanizmu tworzącego okno gry
        super().__init__(EKRAN_DLUGOSC, EKRAN_WYSOKOSC, "W poszukiwaniu skarbu")

        """ Część 2 """
        # Zmienna do przechowywania listy graczy oraz ich wyników
        self.lista_graczy = None
        self.lista_monet = None

        # Utworzenie gracza i wyniku
        self.gracz = None
        self.wynik = 0

        # Ukrycie kursora
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    """ Część 3 """
    def setup(self):
        """ Setup i inicjalizacja zmiennych """

        # Ustawienie typu list jako listy obiektów
        self.lista_graczy = arcade.SpriteList()
        self.lista_monet = arcade.SpriteList()

        # Ustawiamy początkowy wynik
        self.wynik = 0

        # Ustawiamy gracza: Zdjęcie, początkowe umieszczenie gracza na planszy
        self.gracz = arcade.Sprite("character.png", WIELKOSC_GRACZA)
        self.gracz.center_x = 50
        self.gracz.center_y = 50
        self.lista_graczy.append(self.gracz)

        """ Część 4 - tworzymy monety """
        for i in range(LICZBA_MONET):

            moneta = arcade.Sprite("grosik.png", WIELKOSC_MONET)

            # Ustawiamy pozycje
            moneta.center_x = random.randrange(EKRAN_DLUGOSC)
            moneta.center_y = random.randrange(EKRAN_WYSOKOSC)

            # Dodajemy monetę do listy, która następnie jest rysowana
            self.lista_monet.append(moneta)

    def on_draw(self):
        """ Komendy których zadaniem jest otworzenie okna z naszą grą
        oraz narysowanie na ekranie wszystkich elementów"""
        arcade.start_render()

        """ Część 3 """
        # Rysujemy nasze obiekty na planszy za pomocą gotowej komendy
        self.lista_monet.draw()
        self.lista_graczy.draw()


def main():
    """ Tworzymy zmienną, która będzie przewowywała naszą grę."""
    window = GraPoszukiwaczaSkarbu()
    """ Część 3 """
    window.setup()
    """ Mamy już wszystko ustawione! 
    Startujemy grę z użyciem komendy 'run'
    """
    arcade.run()


if __name__ == "__main__":
    main()
