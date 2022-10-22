import random
import string
from EscapeRoom import EscapeRoom

class MyRoom(EscapeRoom):
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
            "Ueberlege dir einen Systembefehl aus Linux und versuche ihn sinnvoll in die URL einzubauen."]
        
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.get_number_from_letters, "data": mysterious_letters}
    
    def create_level2(self):
        mysterious_letters = self.random_letters()

        task_messages = ["Du wachst in einem Raum auf und siehst einen Laptop. Du setzt dich auf den Stuhl und schaust auf den Display."
            "Auf dem Display steht, dass du 10 Minuten Zeit hast, ein Passwort anhand der vorliegenden Dateien zu generieren",
            "Hinter einem an der Wand aufgehängten Bild siehst du nun ein Eingabepanel für einen 6-ziffrigen Code.",
            f"Schreibe eine Methode <code>run('{mysterious_letters}')</code>, die aus den Buchstaben den richtigen Code erzeugt."]
        hints = ["Es gibt ein bestimmtes Modul in Python, mit dem man auf Betriebssystemebene arbeiten kann.",
            "Versuche die englische Variante des Wortes Betriebssystem."]
        
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.get_number_from_letters, "data": mysterious_letters}

    def create_level3(self):
        task_messages = ["Nach der korrekten Eingabe des Codes wird nun geheimnisvolle Musik abgespielt und eine Stimme sagt mehrfach: 'Vokale verboten'"]
        hints = ["Wie lautet der Spruch 'Vokale verboten' wenn Vokale verboten sind?"]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.remove_vowels, "data": "Vokale verboten"}

    def random_letters(self):
        letters = ""
        for _ in range(3):
            letters = letters + random.choice(string.ascii_uppercase)
        return letters

    ### SOLUTIONS ###
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
