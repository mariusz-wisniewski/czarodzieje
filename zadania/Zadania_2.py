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


class Moneta(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.ruch_poziomy = 0
        self.ruch_pionowy = 0
        self.liczba_odbic = 0

    def update(self):

        # Przesuwamy monety
        self.center_x += self.ruch_poziomy
        self.center_y += self.ruch_pionowy

        # Spradzamy czy dotarliśmy do ściany
        # Jeśli tak to się obracamy i idziemy w drugą stronę

        """ Zadanie 5: Czy monety powinny uciekać?
        Jeśli tak to należy usunąć znaki "x". Monety zostaną usunięte z planszy pod warunkiem,
        że odbiją się więcej razy niż będzie na to wskazywała zmienna MAKSYMALNA_LICZA_ODBIC"""
        #if self.liczba_odbic > MAKSYMALNA_LICZA_ODBIC:
        #    self.kill()

        if self.center_x <= 0:
            self.ruch_poziomy *= -1
            self.liczba_odbic += 1

        if self.center_x >= EKRAN_DLUGOSC:
            self.ruch_poziomy *= -1
            self.liczba_odbic += 1

        if self.center_y < 0:
            self.ruch_pionowy *= -1
            self.liczba_odbic += 1

        if self.center_y >= EKRAN_WYSOKOSC:
            self.ruch_pionowy *= -1
            self.liczba_odbic += 1


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
        self.gracz.center_x = 400
        self.gracz.center_y = 300
        self.lista_graczy.append(self.gracz)

        """ Część 4 - tworzymy monety """
        for i in range(LICZBA_MONET):

            """ Zadanie 3: Dlaczego nie widzimy monet?"""
            moneta = Moneta("grosik.png", WIELKOSC_MONET/100)

            # Ustawiamy pozycje
            moneta.center_x = random.randrange(EKRAN_DLUGOSC)
            moneta.center_y = random.randrange(EKRAN_WYSOKOSC)
            moneta.ruch_poziomy = random.randrange(-3, 3, 2)
            moneta.ruch_pionowy = random.randrange(-3, 3, 2)

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

        """ Część 5 - tworzymy monety """
        """ Zadanie 1: Wyświetlmy na ekranie informacje o liczbie zebranych monet"""
        # tablica_wyniku = f"Wynik: {self.wynik}"
        # arcade.draw_text(tablica_wyniku, 10, 20, arcade.color.WHITE, 14)

    """ Część 5 - ruch monet """
    def on_mouse_motion(self, x, y, dx, dy):
        """ Zadanie 2: Nauczmy naszego pirata chodzić.
        Zmienne "x" oraz "y" przechowują informacje o położeniu naszej myszki na ekranie
        Dlatego możemy ich użyć aby zmusić naszego pirata do ruszania.
        Aby to zrobić musimy pirata poinformować o zmienie zmiennych: center_x oraz center_y
        Pirat będzie wtedy wiedział, że musi się przesunać
        """
        # self.gracz.center_x =
        # self.gracz.center_y =


    """ Część 7 - Wykrywanie kolizji """
    # Komenda zajmująca się aktualizacja naszego poszukiwacza skarbów,
    # wszystkich monet czy wykryciem kolizji
    def update(self, delta_time):
        """ Zadanie 4: Ruch monet oraz wykrycie znalezienia monety przez pirata"""
        #self.lista_monet.update()

        """ Utworzenie zmiennej która będzie zawierała liste moment,
            które znalazł nasz poszukiwacz """
        #lista_znalezionych_monet = arcade.check_for_collision_with_list(self.gracz,
        #                                                      self.lista_monet)

        """ Sprawdzamy czy poszukiwacz znalazł monetę """
        #for moneta in lista_znalezionych_monet:
        #    self.wynik = self.wynik + 0


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
