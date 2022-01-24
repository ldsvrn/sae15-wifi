#!/usr/bin/env python3

import os
import argparse
from glob import glob
import pandas as pd

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge and sort csv')
    parser.add_argument("-i", help="path of the input folder", required=True)
    parser.add_argument("-o", help="path of te output file", default="wifi-merged.csv")
    args = parser.parse_args()

    files = glob(os.path.join(args.i, "wifi*.csv"))
    print(files)

    df = pd.concat(map(pd.read_csv, files), ignore_index=True).sort_values(by=["ExpId"], ascending=True)
    df.to_csv(args.o, index=False)
