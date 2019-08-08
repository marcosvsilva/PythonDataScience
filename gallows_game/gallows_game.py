import os
from random import randint

class Gallows:
    def __init__(self, hint, word):
        self.hint = hint
        self.word = word
        self.mistakes = []
        self.hits = []

        self.password = ""
        for i in range(len(word)):
            self.password += "_ "

    def print_gallows(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--------------------------------------------------")
        print("")
        print(" HINT: %s" % self.hint)
        print("  __________  ")
        print(" |          | ")

        self.print_man()

        print(" | ")

        print("_|_          %s " % self.password)
        print("")

        mistake = ""
        for letter in self.mistakes:
            mistake += letter + " "

        hit = ""
        for letter in self.hits:
            hit += letter + " "

        print("letters incorrects: %s" % mistake)
        print("letters corrects: %s" % hit)

        print("")

    def print_man(self):
        if len(self.mistakes) == 0:
            print(" | ")
        else:
            print(" |           0 ")

        if len(self.mistakes) > 1:
            if len(self.mistakes) == 2:
                print(" |           | ")
            elif len(self.mistakes) == 3:
                print(" |          /| ")
            else:
                print(" |          /|\ ")
        else:
            print(" | ")

        if len(self.mistakes) > 4:
            if len(self.mistakes) == 5:
                print(" |          / ")
            else:
                print(" |          / \ ")
        else:
            print(" | ")

