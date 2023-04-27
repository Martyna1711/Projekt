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

            tablica_wynikow[ix] = np.hstack([fi_lam_h[ix], XY_00[ix], XY_92[ix], n_e_u[ix]])