from EscapeRoom import EscapeRoom
from random import choice, randint
from string import ascii_uppercase

class Room_Schwab(EscapeRoom):
    def __init__(self):
        super().__init__()
        self.set_metadata("Julia Schwab-Di Benedetto", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())

    ### LEVELS ###
    def create_level1(self):
        task_messages = ["Du wachst in einem Raum auf und siehst einen Laptop. Du setzt dich auf den Stuhl und schaust auf den Display.",
            "Auf dem Display steht, dass du 5 Minuten Zeit hast, in der vorgegebenen URL eine moegliche Remote Code Execution anzuhaengen",
            "http://localhost:8000/index.html",
            f"Schreibe eine Methode <code>run()</code>, die aus den Buchstaben den richtigen Code erzeugt."]
        hints = ["Es gibt verschiedene Module um Webrequests zu nutzen.",
            "Überlege dir einen Systembefehl aus Linux und versuche ihn sinnvoll in die URL einzubauen."]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.RCE}

    ### SOLUTIONS ###
    # Level 1
    def RCE(self):
        from requests import get

        URL = "http://localhost:8000/index.html"
        r = get(f'{URL}?cmd=ls')
        return r

    # Level 4

    # Level 5

    # Level 6

