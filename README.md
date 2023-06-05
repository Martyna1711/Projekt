Kalkulator Geodezyjny 

Wersja 1.0

Kwiecień 2023

Spis treści
=======================

1. Zastosowanie programu
2. Wymagania systemowe 
3. Wymagane oprogramowanie 
4. Instalacja i uruchomienie 
5. Opis działania programu
6. Wady programu

=======================

1. Zastosowanie programu


Program jest przeznaczony głównie dla geodetów.
Zadaniem Kalkuratora jest przeliczanie współrzędnych na różne sposoby.
Program posiada następujące funkcje:
- hirvonen - Wykonuje transformacje XYZ na BLH.
- geodezyjne2XYZ - Jest odwrotnością Hirvonena. 
- neu - Wykonuje transformacje z współrzędnych geodezyjnych do układu topocentrycznego NEU.
- u2000 - Wykonuje transformacje współrzędnych geodezyjnych do współrzędnych płaskich prostokątnych  w układzie 2000. 
- u1992 - Wykonuje transformacje współrzędnych geodezyjnych do współrzędnych płaskich prostokątnych  w układzie 1992.

Program obsługuje elipsoidy:
- WGS 84
- GRS 80

=======================

2. Wymagania systemowe 

Program został napisany, z myślą o pracy na komputerach lub laptopach posiadających system operacyjny Windows.

=======================

3. Wymagane oprogramowanie 


Do uruchomienia programu potrzebne będzie środowisko python w wersji 3.8 lub nowszej.

Dodatkowo potrzeba będzie posiadać zainstalowane następujące biblioteki:
- math
- numpy
- argparse

=======================

4. Instalacja i uruchomienie 


Żeby poprawnie pobrać i uruchomić program należy:
- Pobrać pliki z internetowego repozytorium i umieścić je w jednym folderze.
- Otworzyć plik o nazwie skrypt2.py za pomocą środowiska spyder.
- Do zaimportowania danych stworzyć ścieżki w oknie General setting - Command line option oraz zaznaczyć opcje Remove all variables before exetution. 
- Postępować zgodnie z instrukcją tekstową, która pokaże się na konsoli.

=======================

5. Opis działania programu


Program składa się z dwóch plików:
- skrypt2.py - plik główny 
- transformacje.py - plik posiadający klasę i funkcje, które posłużą do robienia transformacji.

Program odczytuje plik txt, który zawiera dane wejściowe, które następnie będzie transformował.
Po odczytaniu pliku program spyta się użytkownika, jaki typ działania ma wykonać.
Kiedy użytkownik wybierze jedną z pięciu możliwych opcji działań, program nadpisze plik wyjściowy o wyniki transformacji współrzędnych.
Program kończy działanie, po wybraniu opcji 6 (zakończ pracę programu).

=======================

6. Wady programu

- Podawanie za każdym razem ścieżek do plików wejściowego i wyjściowego jest uciążliwe.
- Program przedstawia współrzędne geodezyjne BLH w łukowej mierze kątowej, przez co nie są one intuicyjne w odczytywaniu.
