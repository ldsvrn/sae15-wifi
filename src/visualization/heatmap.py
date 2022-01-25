#!/usr/bin/env python3

import pandas as pd
import argparse
import matplotlib.pyplot as plt

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cleans results')
    parser.add_argument("-i", help="path of the input file", required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.i)

    descWr = open(args.o, "w")
    descWr.write("Location,Date,ExpId,SSID,Addr,RSSI\n")
    df.plot()
    plt.show()