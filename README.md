Dokumentacja:
Program jest głównie przeznaczony do celów geodezyjnych, jego zdaniem jest przeliczanie współrzędnych na różne sposoby.
Posiada on następujące funkcje:
1. Funkcja hirvonen, która wykonuje następujące transformacje:
XYZ (geocentryczne) -> BLH (elipsoidalne,lambda,h)
Jej działaanie jest oparte na algorytmie Hirvonena.
Funckja służy do transformacji podanych przez użytkownika współrzędnych ortokartezjańkich x,y,z
do współrzędnych geodezyjnych fi,lambda,H.
2.Funkcja geodezyjne2XYZ
Funkcja transportuje współrzędne geodezyjne do współrzędnych geocentrycznych. Jako argumenty przyjmuje szerokoś¢ i długość geografczną i transportuje je na współrzędne kartezjańskie x,y,z.
3.Funkcja neu
Zadaniem funkcji neu jest transformacja podanych przez użytkownika współrzędnych geodezyjnych do współrzędnych w układzie trójwymiarowym NEU.
4.Funkcja u2000
Funkcja u2000 jest funkcją transformującą współrzędne geodezyjne fi i lambda do współrzędnych płaskich prostokątnych w układzie 2000. W tym układzie skala długości odwzorowań na południkach osiowych wynosi m0 =0,999923
5.Funkcja u1992
Jest to funkcja transformująca współrzędne geodezyjne fi i lambda do współrzędnych w układzie płaskim prostokątnym 1992.
W tym ukaadzie południk środkowy odwzorowuje się na linię w skali m0=0,9993.
Do prawidłowego działania programu wymagane jest:
Oprogramowanie Spyder (Python 3.8)
Zaimportowane biblioteki numpy, math oraz argparse.
