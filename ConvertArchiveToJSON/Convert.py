'''
Software in python for study
Convert archives text to JSON
'''

import pandas as pd
import json

acceptedFormats = ('.txt', '.csv')


def printMenu():
    print("|--------------------------|")
    print("|   Welcome to converter   |")
    print("|--------------------------|")


def inputArchive():
    return str(input("| Insert directory and name of archive for conversion: "))


def inputExitDirectory():
    return str(input("| Insert directory you like save archive JSON: "))


def validTypeOfArchive(type):
    return bool(type in acceptedFormats)


def strTrim(string):
    return str(string).replace(" ", "")


def converTextToDictonary(data):
    dict = {}
    lines = data.split('\n')
    for line in lines:
        elemets = line.split(':')
        dict.update({elemets[0]: elemets[1]})
    return dict


printMenu()

directoryArchive = inputArchive()
directoryExit = inputExitDirectory()
directoryExit = directoryExit + 'conversionJSON.json'

directoryArchive = strTrim(directoryArchive)
directoryExit = strTrim(directoryExit)

type = directoryArchive[len(directoryArchive) - 4:]

if validTypeOfArchive(type):
    data = open(directoryArchive, 'r').read()
    with open(directoryExit, 'w', ) as archiveWriter:
        archiveWriter.write(json.dumps(converTextToDictonary(data)))
else:
    print("Archive invalid!")
