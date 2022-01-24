#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse


def ExtractFolderName(path):
    return os.path.dirname(path)


def ExtractFileName(path):
    return os.path.basename(path)


def ExtractPlace(folderName):
    return folderName.split("-")[1]


def ExtractDate(folderName):
    temp = folderName.split("-")[2]
    return f"{temp.split('_')[2]}-{temp.split('_')[1]}-{temp.split('_')[0]}" # ISO8601 date format


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
    parser.add_argument("-i", help="path of the input file", required=True)
    parser.add_argument("-o", help="path of the output file", default="../../data/processed/wifi.csv")
    args = parser.parse_args()

    if os.path.isfile(args.i):
        result = ExtractInfo(args.i)
        descWr = open(args.o, "w")
        descWr.write("Location,Date,ExpId,SSID,Addr,RSSI\n")
        descWr.write(result)
        descWr.close()
    elif os.path.isdir(args.i):
        listFiles = os.listdir(args.i)
        for fichier in listFiles:
            if isFileCreated == False:
                descWr = open(args.o, "w")
                descWr.write("Building,Date,ExpId,SSID,Addr,RSSI\n")
                descWr.close()
                isFileCreated = True
            result = ExtractInfo(args.i + fichier)
            descWr = open(args.o, "a")
            descWr.write(result)
            descWr.close()
            result = ""
    else:
        print("Erreur : le fichier ou le dossier n'existe pas")
