#!/usr/bin/env python3

import pandas as pd


class Model:
    def __init__(self, input_path):
        self.df = pd.read_csv(input_path)

    def mean_loc(self, location):
        return self.df.loc[(self.df["ExpId"] >= location) & (self.df["ExpId"] < location + 1)]["RSSI"].mean()

    def median_loc(self, location):
        return self.df.loc[(self.df["ExpId"] >= location) & (self.df["ExpId"] < location + 1)]["RSSI"].median()

    def mean_floor(self, floor):
        return self.df.loc[self.df["Building"] == floor]["RSSI"].mean()

    def median_floor(self, floor):
        return self.df.loc[self.df["Building"] == floor]["RSSI"].median()

    def mean_mac_loc(self, mac_address, location):
        try:
            return (self.df.loc[(self.df["ExpId"] >= location) &
                                (self.df["ExpId"] < location + 1) &
                                (self.df["Addr"] == mac_address)]["RSSI"].mean())
        except Exception:
            return 0

    # On peut avoir la moyenne de puissance à un endroit donné avec model.mean_mac_loc(model.get_most_powerful(i), i)
    def get_most_powerful(self, location):
        return (self.df.loc[(self.df["ExpId"] >= location) & (self.df["ExpId"] < location + 1)]
                .sort_values(by=["RSSI"], ascending=False)  # On trie par RSSI
                .head(1)["Addr"]  # On prend seulement la permière ligne, on récupère la valeur de Addr
                .values[0])  # On recupère la valeur en string et pas en objet pandas

    def get_ap_list(self):
        # Liste de tous les AP par leur addresse MAC
        return tuple(set(self.df["Addr"]))