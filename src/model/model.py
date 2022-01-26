#!/usr/bin/env python3

import pandas as pd
import statistics as stats


class Model:
    def __init__(self, input_path):
        self.df = pd.read_csv(input_path)

        # Liste de tous les AP par leur addresse MAC
        self.ap_list = tuple(set(self.df["Addr"]))

    def mean_loc(self, location):
        return stats.mean(self.df.loc[(self.df["ExpId"] >= location) & (self.df["ExpId"] < location + 1)]["RSSI"])

    def median_loc(self, location):
        return stats.median(self.df.loc[(self.df["ExpId"] >= location) & (self.df["ExpId"] < location + 1)]["RSSI"])

    def mean_floor(self, floor):
        return stats.mean(self.df.loc[self.df["Building"] == floor]["RSSI"])

    def median_floor(self, floor):
        return stats.median(self.df.loc[self.df["ExpId"] == floor]["RSSI"])

    def mean_mac_loc(self, mac_address, location):
        try:
            return stats.mean(self.df.loc[(self.df["ExpId"] >= location) &
                                          (self.df["ExpId"] < location + 1) &
                                          (self.df["Addr"] == mac_address)]["RSSI"])
        except stats.StatisticsError:
            return 0

    # On peut avoir la moyenne de puissance à un endroit donné avec model.mean_mac_loc(model.get_most_powerful(i), i)
    def get_most_powerful(self, location):
        return (self.df.loc[(self.df["ExpId"] >= location) & (self.df["ExpId"] < location + 1)]
                .sort_values(by=["RSSI"], ascending=False).head(1)["Addr"].values[0])

    def get_ap_list(self):
        return self.ap_list
