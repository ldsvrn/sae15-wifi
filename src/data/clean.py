#!/usr/bin/env python3

import pandas as pd
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cleans results')
    parser.add_argument("-i", help="path of the input file", required=True)
    parser.add_argument("-o", help="path of the output file", required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.i)
    totalLines = len(df)

    # if null value, delete the row
    df.dropna(inplace=True)

    # TODO: quel résaux wifi garder? virer "P.H. EST PARMIS NOUS"?

    # pour l'instant, on garde que si le RSSI est entre 0 et -100
    for x in df.index:
        if df.loc[x, "RSSI"] < -100 or df.loc[x, "RSSI"] > 0:
            df.drop(x, inplace=True)

    # if mac address is not 12 characters, delete the row
    for x in df.index:
        if len(df.loc[x, "Addr"]) != 12:
            df.drop(x, inplace=True)

    df.to_csv(args.o, index=False)
    droppedLines = totalLines - len(df)
    print(f"{droppedLines} lignes sur {totalLines} ont été supprimées soit {round(droppedLines/totalLines*100, 3)}%")