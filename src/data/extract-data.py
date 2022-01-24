#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse


def ExtractFolderName(path):
    return path.split("/")[4]


def ExtractFileName(path):
    return path.split("/")[5]


def ExtractPlace(folderName):
    return folderName.split("-")[1]


def ExtractDate(folderName):
    return folderName.split("-")[2]


def ExtractIdExp(fileName):
    return fileName.split("-")[-1]


def ExtractSsid(content):
    return content.split("'")[0][:-1]


def ExtractMacAddr(content):
    return content.split("'")[1]


def ExtractRssi(content):
    return content.split("'")[2]


def ExtractInfo(path):
    folderName = ExtractFolderName(path)  # Extract folder name
    fileName = ExtractFileName(path)  # Extract filename
    result = ""
    descRd = None
    descRd = open(path, "r")
    content = descRd.readlines()
    for idx in content:
        result += f"{ExtractPlace(folderName)},{ExtractDate(folderName)},{ExtractIdExp(fileName)}," \
                  f"{ExtractSsid(idx)},{ExtractMacAddr(idx)},{ExtractRssi(idx)}"
    descRd.close()
    return result


if __name__ == '__main__':
    # declare variables
    isFileCreated = False
    descWr = None
    result = ""
    folderName = ""
    fileName = ""

    # define arguments
    parser = argparse.ArgumentParser(description='Extract information from Wi-Fi logs')
    parser.add_argument("-input", help="path of the input file", required=True)
    args = parser.parse_args()

    if os.path.isfile(args.input):
        result = ExtractInfo(args.input)
        descWr = open("../../data/processed/wifi.csv", "w")
        descWr.write("Location,Date,ExpId,SSID,Addr,RSSI\n")
        descWr.write(result)
        descWr.close()
    elif os.path.isdir(args.input):
        listFiles = os.listdir(args.input)
        for fichier in listFiles:
            if isFileCreated == False:
                descWr = open("../../data/processed/wifi.csv", "w")
                descWr.write("Building,Date,ExpId,SSID,Addr,RSSI\n")
                descWr.close()
                isFileCreated = True
            result = ExtractInfo(args.input + fichier)
            descWr = open("../../data/processed/wifi.csv", "a")
            descWr.write(result)
            descWr.close()
            result = ""
    else:
        print("Erreur : le fichier ou le dossier n'existe pas")
