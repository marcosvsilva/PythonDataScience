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

