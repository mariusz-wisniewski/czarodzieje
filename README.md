# Czarodzieje Kodu 2019 - Poznań 
Podczas warszatów "Czarodzieje Kodu" w Poznaniu przygotowaliśmy swoją pierwszą grę 2D napisaną w Pythonie z użyciem biblioteki Arcade (na podstawie https://arcade-book.readthedocs.io/en/latest/chapters/18_sprites_and_collisions/sprites.html)! Poniżej prezentuje kilka informacji, które mogą być użyteczne w przypadku chęci kontynuowania zabawy w domowym zaciszu. 

## Wymagania
**Python** w wersji 3.7+
```
https://www.python.org/downloads/release/python-373/
```
**Arcade** - Biblioteka do tworzenia gier 2D 
```
http://arcade.academy
```

## Przebieg zajęć
Po kilku słowach wstępu dotyczących programowania, wraz z uczestnikami, ruszyliśmy do boju i rozpoczęliśmy tworzenie naszej gry "Poszukiwacze skarbów". 

Podczas zajęć udało nam się zrealizować zakres pokryty przez pierwsze 7 plików:\
[1_poczatek.py](1_poczatek.py) - "Suchy" kod, którego zadaniem jest uruchomienie i wyświetlenie pustego (czarnego) okna gry\
[2_przygotowanie_okna.py](2_przygotowanie_okna.py) - W tej części pojawia się kod odpowiedzialny na kolorowanie okna oraz przygotowanie zmiennych do przechowywania gracza oraz monet \
[3_wstawiamy_swojego_gracza.py](3_wstawiamy_swojego_gracza.py) - Dodajemy naszego gracza, jeszcze nie potrafi się ruszać\
[4_wstawiamy_monety.py](4_wstawiamy_monety.py) - Dodajemy monety, jeszcze nie potrafią się ruszać\
[5_ruch_wynik.py](5_ruch_wynik.py) - Uczymy chodzić naszego pirata oraz dajemy tablice wyniku\
[6_kolizje.py	Add](6_kolizje.py) - Zaczynamy wykrywać kontakt z monetami\
[7_ruch_monet.py](7_ruch_monet.py) - Dodajemy ruch monet


## Bonus
Poniżej znajdą Państwo dwa pliku ze zbiorem różnych zadań:
[Zadania_1.py](zadania/Zadania_1.py) - W pierwszej części uczestnicy dowiedzą się jak, w prosty sposób, można zmienić tło naszej gry oraz ukryć kursor myszki./
[Zadania_2.py](zadania/Zadania_2.py) - Plik posiada już gotowy kod, który rysuje pirata, monety. Zadaniem uczestiników będzie dopisanie kodu, który umożliwi ruchanie pirata/monet czy wykrywanie trafienia monety. Uwaga: Niektóre punkty zawierają błędy, pomijają niektóre fragmenty kodu. Zadaniem uczestników było ich wykrycie - z zadania wywiązali się znakomicie!/

Odpowiedzi znajdują się w plikach:\
[Zadania_1_Odpowiedzi.py](zadania/Zadania_1_Odpowiedzi.py)\
[Zadania_2_Odpowiedzi.py](zadania/Zadania_2_Odpowiedzi.py)


## Co dalej?
Bilbioteka Arcade daje wiele więcej możliwości! W związku z ograniczonym czasem nie udało nam się przejść przez wszystkie przygotowane zadania - w związku z czym gorąco zachęcam do nadrobienia "zaległości". Do zrealizowania pozostało nam:
1. Monety o różnej wielkości i różnej punktacji ([8_rozne_rozmiary.py](8_rozne_rozmiary.py)). 
2. "Złe" monety, które zabierają nam punkty gdy je złapiemy ([9_zle_monety.py](9_zle_monety)). Te złe monety, w przeciwieństwie do złotych, nie odbijają się od krawędzi mapy tylko z niej uciekają. 
3. Sterowanie za pomocą klawiatury ([10_ruch_klawiatura.py](10_ruch_klawiatura.py)). Prezentujemy tutaj najprostszą, aczkolwiek nie najpłynniejszą metodę, sterowania.
4. Wyświelenie ekranu końca gry kiedy już wszystkie monety zostaną przez nas wyłapane.
