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
