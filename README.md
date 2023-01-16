# Gale

## Informacje o projekcie

Celem projektu było stworzenie gry Shannon Switching w wariancie Gale między człowiekiem a graczem komputerowym o dwóch poziomach trudności.

Gra została wykonana przy użyciu interfejsu okienkowego.

# Ogólne informacje

Sterowanie w całej grze odbywa się za pomocą myszki i jej lewego przycisku.

Grę włącza się poprzez uruchomienie pliku `gale.py`, a po kilku sekundach ukazuje się okienko powitalne wraz z menu.

W menu do wyboru są cztery tryby gry:
+ 2 graczy
+ Gracz vs Komputer poziom łatwy - całkowicie losowe ruchy
+ Gracz vs Komputer poziom trudny - wybiera najlepszy znany botowi ruch
+ Komputer poziom trudny vs Komputer poziom trudny

Oraz cztery rozmiary planszy:
+ 7x7
+ 9x9
+ 11x11
+ 13x13

Następnie rozpoczyna się rozgrywka na planszy, każdy gracz wybiera pole do umieszczenia swojego pionka. Grę rozpoczyna gracz Czerwony, którego zadaniem jest połączyć lewy i prawy bok kwadratu, natomiast Niebieskiego - górny i dolny.

Na pasku tytułowym wyświetlane jest kto wykonuje teraz ruch, a w przypadku ruchów graczy komputerowych widoczna jest również procentowa informacja o postępie procesu myślenia.

Gra toczy się do momentu zwycięstwa któregoś z graczy, gdyż ten wariant gry nie może zakończyć się remisem. W momencie zakończenia gry wyświetli się komunikat przedstawiający zwycięzcę aktualnej rozgrywki. Kliknięcie myszką w oknie spowoduje powrót do menu i ponownego wyboru trybu gry.

Grę można opuścić poprzez klknięcie czerwonego X w prawym górnym rogu okna.


## Podział projektu na następujące moduły

 `gale.py` - główny plik uruchamiający rozgrywkę

 `logic.py` - odpowiada za przeprowadzenie rozgrywki w odpowiedniej sekwencji

 `grid.py` - odpowiada za generowanie i modyfikację siatki oraz sprawdzanie, czy któryś z graczy zwyciężył

 `interface.py` - odpowiada za wyświetlanie menu oraz rozgrywki, a także za pobieranie informacji o decyzji gracza. Został tu wykorzystany PyGame.

 `bot.py` - zawiera w sobie algorytmy decydujące o ruchu gracza komputerowego

`test_grid.py` - odpowiada za testowanie metod klasy Grid

`grid_test.py` - zawiera w sobie zapis przykładowych siatek stworzonych do testów

## Opis klas użytych w projekcie

@TODO

# Refleksje na temat projektu

Projekt uważam za udany. Oczywiście można by go rozbudować o funkcje i wybory, np. jaki kolor rozpoczyna grę albo usprawnić działanie trudnego bota, ale to już są zabiegi kosmetyczne, które można zmienić w razie potrzeby. Pewnie udałoby się jakoś zoptymalizować metodę do sprawdzania warunku zwycięstwa.

Najbardziej jestem zadowolony z działania bota trudnego (AI), który przebył sporą drogę jeśli chodzi o sposób działania, a co ważniejsze o prędkość podejmowania decyzji. Początkowo AI vs AI na planszy 13x13 zajmowało zbyt sporo czasu, potem przez zastosowanie algorytmu `monte_carlo_tree_search` i `multiprocessingu` udało się skrócić rozgrywkę do około 3 minut. Następnie poprzez zmienienie `deepcopy()` na `my_copy()`, które znajduje się w pliku bot.py osiągnąłem czas rozgrywki około minuty, który utrzymuje się do tej pory. Trudność AI można zmieniać w kodzie porzez zmianę zmiennej `simulations` - im jest większa tym lepsze będzie AI, ale też więcej czasu będzie jej zajmować podejmowanie decyzji.

Mam też mały problem. Mianowicie podczas wyświetlania w PyGame rozgrywki AI-AI w funkcji `monte_carlo_tree_search()` program się czasami zawiesza w funkcji `pool.map()` z oczekiwaniem na zsynchronizowanie wszystkich dzieci. Co ciekawe dzieje się to tylko podczas jednoczesnego korzystania z PyGame i `multiprocessingu`, ponieważ w testach nie występują żadne błędy wskazujące na błędny algorytm sprawdzania wygranej `check_win_connection()`. Problem ten brutalnie rozwiązałem przy użyciu dekoratora `timeout()` który poprzez rzucenie wyjątku `TimeoutError` ponownie inicjalizuje `multiprocessing` w `monte_carlo_tree_search()` po przekroczeniu wyznaczonego czasu, aż do momentu gdy nie uda się pomyślnie zakończyć wszystich symulacji i ich zsynchronizować. U mnie już działa : )

Jednakże czasami po wywołaniu wyjątku `TimeoutError` jest problem z zamknięciem gry przez czerwonego X i trzeba wyłączyć program w terminalu. Menu i dalsza gra wciąż jednak działa, problem jest tylko z zamknięciem.

Na pewno ten projekt rozbudził moje zainteresowine w zakresie programowania w Pythonie i w przyszłości planuję zająć się jakimiś podstawami sztucznej inteligencji.