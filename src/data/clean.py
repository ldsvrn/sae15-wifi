#!/usr/bin/env python3

import pandas as pd
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cleans results')
    parser.add_argument("-i", help="path of the input file", required=True)
    parser.add_argument("-o", help="path of the output file", required=True)
    parser.add_argument("--networks", help="comma separated lists of networks")
    parser.add_argument("--keepids", help="keep IDs that are not integers", nargs='?', const=True, type=bool)
    args = parser.parse_args()

    df = pd.read_csv(args.i)
    totalLines = len(df)

    # if null value, delete the row
    df.dropna(inplace=True)

    if args.networks != None:
        networks = args.networks.split(",")
        for x in df.index:
            if df.loc[x, "SSID"] not in networks:
                df.drop(x, inplace=True)

    # TODO: quel résaux wifi garder? ExpId avec virgules???

    if args.keepids == False:
        # pour l'instant, on ne garde pas les ExpId à virgules
        for x in df.index:
            if not df.loc[x, "ExpId"].is_integer():
                df.drop(x, inplace=True)

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