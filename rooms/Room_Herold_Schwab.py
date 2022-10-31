from EscapeRoom import EscapeRoom
from os import walk
from os.path import join
from random import choice, randint
from requests import get, post
from string import ascii_uppercase

class Room_Herold_Schwab(EscapeRoom):
    def __init__(self):
        super().__init__()
        self.set_metadata("Rainer Herold", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())

    ### LEVELS ###
    def create_level1(self):
        mysterious_letters = self.random_letters()

        task_messages = ["Du wachst in einem Raum auf und siehst einen Laptop. Du setzt dich auf den Stuhl und schaust auf den Display.",
            "Auf dem Display steht, dass du 5 Minuten Zeit hast, in der vorgegebenen URL eine moegliche Remote Code Execution anzuhaengen",
            "http://localhost:8000/index.html"
            f"Schreibe eine Methode <code>run('{mysterious_letters}')</code>, die aus den Buchstaben den richtigen Code erzeugt."]
        hints = ["Es gibt verschiedene Module um Webrequests zu nutzen.",
            "Überlege dir einen Systembefehl aus Linux und versuche ihn sinnvoll in die URL einzubauen."]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.RCE, "data": mysterious_letters}

    def create_level2(self):
        task_messages = ["Nach der korrekten Eingabe des Codes hoerst du einen alarmieren Ton, auf dem Display erscheint eine neue Nachricht.",
                        "Du hast maximal 5 Minuten Zeit, einen Sortier Algorithmus zu folgendem String zu generieren!"
                        "H134E23589L34563L23333222244L23335555112334O"
                        "Gebe danach den sortierten String nach folgendem Beispiel aus."
                        "1. A","2. B", "3. C"]
        hints = ["Wie kann am effizientesten ein Sortieralgorithmus generiert werden?", 
                "Probiere es mit einer Hilfsvariable"]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.remove_vowels, "data": "Vokale verboten"}

    def create_level3(self):
        mysterious_letters = self.random_letters()

        task_messages = ["Du hast den zweiten Teil bestanden. Nun bemerkst du, dass auf dem Display ein neuer Dialog erscheint."
            "Auf dem Display steht, dass du nun 10 Minuten Zeit hast, ein Passwort anhand der vorliegenden Dateien zu generieren",
            "Hinter einem an der Wand aufgehängten Bild siehst du nun ein Eingabepanel für einen 6-ziffrigen Code.",
            f"Schreibe eine Methode <code>run('{mysterious_letters}')</code>, die aus den Buchstaben den richtigen Code erzeugt."]
        hints = ["Es gibt ein bestimmtes Modul in Python, mit dem man auf Betriebssystemebene arbeiten kann.",
            "Versuche die englische Variante des Wortes Betriebssystem."]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.List_Files_Build_Pass, "data": mysterious_letters}

    def random_letters(self):
        letters = ""
        for _ in range(3):
            letters = letters + choice(ascii_uppercase)
        return letters

    ### SOLUTIONS ###
    # Level 1
    def RCE(self):
        URL = "http://localhost:8000/index.html"
        r = get(f'{URL}?cmd=ls')
        return r

    # Level 2
    def Sort_Chars_In_Text(self):
        Text, Word = "H134E23589L34563L23333222244L23335555112334O", ""
        for Text_Char in Text:
            if (Text_Char.isupper()): Word += Text_Char
        for View in range(0, len(Word)): print (f{View+1} - {Word[View]})

    # Level 3
    def List_Files_Build_Pass(self):
        word = ""
        for root, _, files in walk('./Level_2', topdown=False):
            for file in files:
                with open(join(root, file), 'r') as f:
                    for line in f.read().splitlines():
                        for line_char in line:
                            if (line_char.isupper()): word += line_char
                            elif (line_char.islower()): word += line_char
        return word

    def get_number_from_letters(self, letters):
        numberstring = ""
        for c in letters:
            numberstring = numberstring + str(ord(c))
        return numberstring

    def remove_vowels(self, word):
        result = ""
        vowels = ["a", "e", "i", "o", "u"]
        for c in word:
            if not c in vowels:
                result = result + c
        return result

    # Level 4

    # Level 5

    # Level 6
