#!/usr/bin/env python3
import pandas as pd


class Cleaner:
    def __init__(self, input_path, networks="uha", drop_duplicates=False):
        self.networks = networks
        self.drop_duplicates = drop_duplicates
        self.df = pd.read_csv(input_path)

        # delete reasons
        self.deleted_null = 0
        self.deleted_duplicates = 0
        self.deleted_SSID = 0
        self.deleted_RSSI = 0
        # self.deleted_MAC = 0
        print("DEBUG:", self.networks)

    def clean(self):
        # if null value, delete the row
        temp = len(self.df)
        self.df.dropna(inplace=True)
        self.deleted_null = temp - len(self.df)

        # delete all duplicates
        temp = len(self.df)
        if self.drop_duplicates:
            self.df.drop_duplicates(inplace=True)
        self.deleted_duplicates = temp - len(self.df)

        temp = len(self.df)
        self.df = self.df.loc[(self.df["RSSI"] <= -10) & (self.df["RSSI"] >= -100)]
        self.deleted_RSSI = temp - len(self.df)

        # if mac address is not 12 characters, delete the row
        # temp = len(self.df)
        # for x in self.df.index:
        #     if len(self.df.loc[x, "Addr"]) != 12:
        #         self.df.drop(x, inplace=True)
        # self.deleted_MAC = temp - len(self.df)

        temp = len(self.df)
        self.df = self.df.loc[self.df["SSID"] == self.networks]
        self.deleted_SSID = temp - len(self.df)

    def to_csv(self, output_path):
        self.df.to_csv(output_path, index=False)

    def get_delete_reason(self):
        if self.drop_duplicates:
            return {
                "null": self.deleted_null,
                "RSSI": self.deleted_RSSI,
                "duplicates": self.deleted_duplicates,
                "SSID": self.deleted_SSID
                # "MAC": self.deleted_MAC
            }
        else:
            return {
                "null": self.deleted_null,
                "RSSI": self.deleted_RSSI,
                "SSID": self.deleted_SSID
                # "MAC": self.deleted_MAC
            }

    def get_total_deleted(self):
        returnval = 0
        for i in self.get_delete_reason().values():
            returnval += i
        return returnval

    def get_lines(self):
        return len(self.df)
