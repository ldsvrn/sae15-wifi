#!/usr/bin/env python3
import pandas as pd


class Cleaner:
    def __init__(self, input_path, networks="uha", drop_duplicates=False):
        self.networks = networks.split(",")
        self.drop_duplicates = drop_duplicates
        self.df = pd.read_csv(input_path)
        self.totalLines = len(self.df)

        # delete reasons
        self.deleted_null = 0
        self.deleted_duplicates = 0
        self.deleted_SSID = 0
        self.deleted_RSSI = 0
        self.deleted_MAC = 0

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
        for x in self.df.index:
            if self.df.loc[x, "SSID"] not in networks:
                self.df.drop(x, inplace=True)
        self.deleted_SSID = temp - len(self.df)

        temp = len(self.df)
        for x in self.df.index:
            if self.df.loc[x, "RSSI"] < -100 or self.df.loc[x, "RSSI"] > -10:
                self.df.drop(x, inplace=True)
        self.deleted_RSSI = temp - len(self.df)

        # if mac address is not 12 characters, delete the row
        temp = len(self.df)
        for x in self.df.index:
            if len(self.df.loc[x, "Addr"]) != 12:
                self.df.drop(x, inplace=True)
        self.deleted_MAC = temp - len(self.df)

    def to_csv(self, output_path):
        self.df.to_csv(output_path, index=False)

    def get_delete_reason(self):
        return {
            "null": self.deleted_null,
            "duplicates": self.deleted_duplicates,
            "SSID": self.deleted_SSID,
            "RSSI": self.deleted_RSSI,
            "MAC": self.deleted_MAC
        }

    def get_lines(self):
        return len(self.df)

    def get_original_lines(self):
        return self.totalLines