Dokumentacja:
Program jest głównie przeznaczony do celów geodezyjnych, jego zdaniem jest przeliczanie współrzędnych na różne sposoby.
Posiada on następujące funkcje: Funkcja Hirvonem wykonuje transformację XYZ (geocentryczne) na BLH (elipsoidalne,lambda,h),jej działaanie jest oparte na algorytmie Hirvonena. Służy ona do transformacji podanych przez użytkownika współrzędnych ortokartezjańkich x,y,z do współrzędnych geodezyjnych fi,lambda,H. Kolejną funkcją jest Funkcja geodezyjne2XYZ, transportuje ona współrzędne geodezyjne do współrzędnych geocentrycznych. Jako argumenty przyjmuje szerokoś¢ i długość geografczną i transportuje je na współrzędne kartezjańskie x,y,z.
Zadaniem funkcji neu jest transformacja podanych przez użytkownika współrzędnych geodezyjnych do współrzędnych w układzie trójwymiarowym NEU.Funkcja u2000 jest funkcją transformującą współrzędne geodezyjne fi i lambda do współrzędnych płaskich prostokątnych w układzie 2000. W tym układzie skala długości odwzorowań na południkach osiowych wynosi m0 =0,999923
Funkcja u1992 jest to funkcja transformująca współrzędne geodezyjne fi i lambda do współrzędnych w układzie płaskim prostokątnym 1992. W tym układzie południk środkowy odwzorowuje się na linię w skali m0=0,9993.
Do prawidłowego działania programu wymagane jest:
Oprogramowanie Spyder (Python 3.8)
Zaimportowane biblioteki numpy, math oraz argparse.
