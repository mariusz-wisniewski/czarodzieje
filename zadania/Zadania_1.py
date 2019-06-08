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

        """ Zadanie: Ustaw kolor naszej planszy używając komendy:
            arcade.set_background_color (tłumacząc: ustaw_tlo_kolor)
            Kolor wybieramy podając go w nawiasie, zaraz po komendzie
            Możemy użyć jednego z wielu gotowych kolorów:
            arcade.color.AMAZON (używany na warsztatach) - zielony
            arcade.color.BLUE - niebieski
            arcade.color.YELLOW - żółty
            arcade.color.PINK - różowy
            to tylko przykłady. Jest ich więcej: http://arcade.academy/arcade.color.html
        """

        
        """ Zadanie: Schowaj kursor myszki tak aby nie był on w ogóle wyświetlany
        gdy skierujemy swoją myszkę na plansze. Użyj do tego celu komendy:
            self.set_mouse_visible (tłumacząc: ustaw_myszki_widzialność)
        Decyzje podejmujemy przekazując zmienną True/False (Prawda/Fałsz) w nawiasie, zaraz po komendzie
          
        """


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
