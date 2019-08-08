import os
import random


class Gallows:
    def __init__(self, hint, word):
        self.hint = hint
        self.word = word
        self.mistakes = []
        self.hits = []

        word_not_repeat_letter = []
        for letter in word:
            if letter not in word_not_repeat_letter:
                word_not_repeat_letter.append(letter)

        self.number_of_letter_correct = len(word_not_repeat_letter)

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
            print(" |          0 ")

        if len(self.mistakes) > 1:
            if len(self.mistakes) == 2:
                print(" |          | ")
            elif len(self.mistakes) == 3:
                print(" |         /| ")
            else:
                print(" |         /|\ ")
        else:
            print(" | ")

        if len(self.mistakes) > 4:
            if len(self.mistakes) == 5:
                print(" |         / ")
            else:
                print(" |         / \ ")
        else:
            print(" | ")

    def attempt(self, letter):
        if letter not in self.hits and letter not in self.mistakes:
            if letter in self.word:
                self.hits.append(letter)

                self.password = ""
                for letter in self.word:
                    if letter in self.hits:
                        self.password += letter + " "
                    else:
                        self.password += "_ "
            else:
                self.mistakes.append(letter)

            self.print_gallows()

    def validate_win(self):
        if len(self.hits) == self.number_of_letter_correct:
            print("Congratulations great master! You are the lord of the gallows game...")
            return False
        elif len(self.mistakes) >= 6:
            print("Unfortunately it was not now! Try again beginner...")
            return False
        else:
            return True


words = {"Comida": ["chocolate", "pizza", "strogonoff", "cochinha", "quibe", "arroz", "batata-frita", "torta", "bolo"],
         "Animal": ["jorges", "cachorro", "macaco", "baleia", "preguica", "cobra", "leao", "elefante", "girafa", "lhama"],
         "Bebida": ["cafe", "caipirinha", "refrigerante", "cerveja", "vinho", "whiskey", "vodka", "suco", "agua"]}

list_random = list(words.keys())
random.shuffle(list_random)

hint = list_random[0]
password_list = words.get(hint)

random.shuffle(password_list)
password = password_list[0]

game = Gallows(hint, password)
game.print_gallows()

while game.validate_win():
    letter = str(input("Insert one letter: "))
    game.attempt(letter)
