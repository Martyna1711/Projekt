# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 08:14:29 2023

@author: Martyna 
"""

import argparse
import numpy as np
from transformacje import Transformacje


def main():
    elipsoida_grs80 = Transformacje(model="grs80")

    parser = argparse.ArgumentParser(description="Program do transformacji współrzędnych.")
    parser.add_argument("--input", help="ścieżka do pliku wejściowego z danymi")
    parser.add_argument("--output", help="ścieżka do pliku wyjściowego z wynikami")

    args = parser.parse_args()

    if args.input and args.output:
        input_data = np.genfromtxt(args.input, delimiter=',', skip_header=4)
        output_path = args.output

        w, k = np.shape(input_data)

        fi_lam_h = np.zeros((w, k))
        XYZ = np.zeros((w, k))
        XY_00 = np.zeros((w, 2))
        XY_92 = np.zeros((w, 2))
        n_e_u = np.zeros((w, k))

        tablica_wynikow = np.zeros((w, 10))

        for ix in range(w):
            fi_lam_h[ix] = elipsoida_grs80.hirvonen(input_data[ix, 0], input_data[ix, 1], input_data[ix, 2])
            XYZ[ix] = elipsoida_grs80.geodezyjne2XYZ(fi_lam_h[ix, 0], fi_lam_h[ix, 1], fi_lam_h[ix, 2])
            XY_00[ix] = elipsoida_grs80.u2000(fi_lam_h[ix, 0], fi_lam_h[ix, 1])
            XY_92[ix] = elipsoida_grs80.u1992(fi_lam_h[ix, 0], fi_lam_h[ix, 1])
            n_e_u[ix] = elipsoida_grs80.neu(input_data[ix, 0], input_data[ix, 1], input_data[ix, 2],
                                            input_data[ix, 0] + 1, input_data[ix, 1] + 1, input_data[ix, 2] + 1)

            tablica_wynikow[ix] = np.hstack([(fi_lam_h[ix,0]/np.pi)*180,(fi_lam_h[ix,1]/np.pi)*180,fi_lam_h[ix,2],n_e_u[ix], XY_00[ix], XY_92[ix]])

        while True:
            print("\nOpcje:")
            print("1 | Transformacja współrzędnych geocentrycznych na współrzędne geodezyjne")
            print("2 | Transformacja współrzędnych geodezyjnych na współrzędne geocentryczne")
            print("3 | Obliczenie współrzędnych topocentrycznych E,N,U")
            print("4 | Transformacja współrzędnych geodezyjnych do układu płaskiego 2000")
            print("5 | Transformacja współrzędnych geodezyjnych do układu płaskiego 1992")
            print("6 | Zakończ")

            choice = input("\nWybierz opcję (1-6): ")

            if choice == '1':
                print('Szerokość geodezyjna | Długość geodezyjna | Wysokość na elipsoidzie')
                for ix in range(w):
                    fi_lam_h[ix] = elipsoida_grs80.hirvonen(input_data[ix, 0], input_data[ix, 1], input_data[ix, 2])
                    fi=(fi_lam_h[ix,0]/np.pi)*180
                    lam=(fi_lam_h[ix,1]/np.pi)*180
                    print(f'{fi} | {lam} | {fi_lam_h[ix][2]}')
            elif choice == '2':
                print('X | Y | Z')
                for ix in range(w):
                    XYZ[ix] = elipsoida_grs80.geodezyjne2XYZ(fi_lam_h[ix, 0], fi_lam_h[ix, 1], fi_lam_h[ix, 2])
                    print(f'{XYZ[ix][0]} | {XYZ[ix][1]} | {XYZ[ix][2]}')
            elif choice == '3':
                print('N | E | U')
                for ix in range(w):
                    n_e_u[ix] = elipsoida_grs80.neu(input_data[ix, 0], input_data[ix, 1], input_data[ix, 2],
                                                    input_data[ix, 0] + 1, input_data[ix, 1] + 1, input_data[ix, 2] + 1)
                print(f'{n_e_u[ix][0]} | {n_e_u[ix][1]} | {n_e_u[ix][2]}')
                for ix in range(w):
                    n_e_u[ix] = elipsoida_grs80.neu(input_data[ix, 0], input_data[ix, 1], input_data[ix, 2],
                                                    input_data[ix, 0] + 1, input_data[ix, 1] + 1, input_data[ix, 2] + 1)
                    print(f'{n_e_u[ix][0]}|{n_e_u[ix][1]}|{n_e_u[ix][2]}')
            elif choice == '4':
                print('X_układ_2000 | Y_układ_2000')
                for ix in range(w):
                    XY_00[ix] = elipsoida_grs80.u2000(fi_lam_h[ix, 0], fi_lam_h[ix, 1])
                    print(f'{XY_00[ix][0]} | {XY_00[ix][1]}')
            elif choice == '5':
                print('X_układ_1992 | Y_układ_1992')
                for ix in range(w):
                    XY_92[ix] = elipsoida_grs80.u1992(fi_lam_h[ix, 0], fi_lam_h[ix, 1])
                    print(f'{XY_92[ix][0]} | {XY_92[ix][1]}')
            elif choice == '6':
                print("Zakończono program.")
                break
            else:
                print("Niepoprawny wybór, spróbuj ponownie.")

            np.savetxt(output_path, tablica_wynikow, delimiter=',   ', fmt='%f')
            print("Transformacja zakończona pomyślnie. Wyniki zapisano w pliku wyjściowym.")
            break
    else:
        print("Brak pliku wejściowego lub wyjściowego. Spróbuj ponownie z poprawnymi argumentami.")


if __name__ == "__main__":
    main()
