Kalkulator Geodezyjny 

Wersja 1.1

Czerwiec 2023

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

Instalacja bibliotek na systemie windows wygląda następująco:
Otwieramy folder, w którmy znajduje się nasz program. 
W pasku zawierającym ścieżkę dostępu wpisujemy cmd i wciskamy enter.
W odpalonej konsoli windowsa należy wpisać komendę:
python -m pip install [options]
zamiast options wpisać nazwę biblioteki

=======================

4. Instalacja i uruchomienie 

Aby poprawnie uruchomić program należy:
- Umieścić pliki main.py i transformacje.py w jednym folderze.
- W pasku zawierającym ścieżkę dostępu wpisujemy cmd i wciskamy enter.
- W konsoli wpisać polecenie main.py
- Jeżeli wszystko jest poprawnie, to powinna pojawić się informacja o braku podanych ścieżek. 
Natomiast jeżeli będzie brakowało jednej z bibliotek, to patrz punkt wyżej
- Jak już biblioteki są zainstalowane, to należy podać ścieżki do pliku wejściowego i wyjściowego. Przykład całej komendy:
main.py --input C:\Users\Axus\Desktop\proj_infa_1\Projekt-2\Projekt\Dane\In\wsp.inp.txt --output C:\Users\Axus\Desktop\proj_infa_1\Projekt-2\Projekt\Dane\Out\test.txt
(wsp.inp.txt - plik wejściowy o rozszerzeniu txt, test.txt - plik wyjściowy o rozszerzeniu txt)


=======================

5. Opis działania programu


Program składa się z czterech plików:
- skrypt2.py - plik główny 
- transformacje.py - plik posiadający klasę i funkcje, które posłużą do robienia transformacji.
- wsp.txt - jest to plik tekstowy zawierający współrzędne wejściowe w układzie geocentrycznym. Plik powinien składać się z 4 linijkowego nagłówka i dowolnej ilości wierszy będących punktami (punkty powinny być ułożone następująco X,Y,Z, separatorem między nimi to ",", a znak oddzielający liczby całkowite od części dziesiętnych to "."
- wynik.txt - jest to pusty plik tekstowy, w którym zapiszą się wyniki w następującej kolejności (fi,lam,h,n,e,u,x00,y00,x92,y92)

Program odczytuje punkty z pliku wejściowego, a następnie wykonuje wszystkie transformacje z punktu pierwszego. 
Na konsoli pojawia się zapytanie, który wynik chcemy na niej zobaczyć (wyniki na konsoli są podane z większą dokładnością).
Następnie wszystkie wyniki są zapisywane w pliku wyjściowym w kolejności podanej powyżej.

=======================

6. Wady programu

-Program zapisuje wszystkie wyniki do pliku wyjściowego, a nie tylko transformacje, o którą zostanie poproszony.

-Plik wejściowy musi mieć konkretną formę aby program zadziałał poprawnie.

-Z niewiadomych przyczyn wyniki w pliku wyjściowym zawsze mają dokładność do szóstego miejsca po przecinku.
