"""
    Cześć! Witajcie Czarodzieje Kodu!
    Oto piersze linijki kodu naszej gry.
    Poznamy podstawowe tajniki Arcade oraz pierwszy uruchomimy nasz własny program z jego użyciem!
"""
import arcade

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

    def on_draw(self):
        """ Komendy których zadaniem jest otworzenie okna z naszą grą
        oraz narysowanie na ekranie wszystkich elementów"""
        arcade.start_render()


def main():
    """ Tworzymy zmienną, która będzie przewowywała naszą grę."""
    window = GraPoszukiwaczaSkarbu()

    """ Mamy już wszystko ustawione! 
    Startujemy grę z użyciem komendy 'run'
    """
    arcade.run()


if __name__ == "__main__":
    main()
