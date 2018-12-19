'''
Software in python for study
Convert archives text to JSON
'''

import pandas as pd
import json

accepted_formats = ('.txt', '.csv')


def print_menu():
    print("|--------------------------|")
    print("|   Welcome to converter   |")
    print("|--------------------------|")


def input_archive():
    return str(input("| Insert directory and name of archive for conversion: "))


def input_exit_directory():
    return str(input("| Insert directory you like save archive JSON: "))


def valid_type_archive(type):
    return bool(type in accepted_formats)


def trim(string):
    return str(string).replace(" ", "")


def conver_text_dictonary(data):
    dict = {}
    lines = data.split('\n')
    for line in lines:
        elemets = line.split(':')
        dict.update({elemets[0]: elemets[1]})
    return dict


print_menu()

directory_archive = input_archive()
directory_exit = input_exit_directory()
directory_exit = directory_exit + '_conversion_json.json'

directory_archive = trim(directory_archive)
directory_exit = trim(directory_exit)

type = directory_archive[len(directory_archive) - 4:]

if valid_type_archive(type):
    data = open(directory_archive, 'r').read()
    with open(directory_exit, 'w') as archive_writer:
        archive_writer.write(json.dumps(conver_text_dictonary(data)))
else:
    print("Archive invalid!")
