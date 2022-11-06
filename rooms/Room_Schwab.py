from EscapeRoom import EscapeRoom
from os.path import dirname, join, realpath
from random import randint

class Room_Schwab(EscapeRoom):
    def __init__(self):
        super().__init__()
        self.set_metadata("Julia Schwab-Di Benedetto", __name__)
        self.add_level(self.create_level4())
        self.add_level(self.create_level5())

    ### LEVELS ###
    def create_level1(self):
        URL = "http://localhost:5000/index.html"

        task_messages = ["Du wachst in einem Raum auf und siehst einen Laptop, welcher einen Akkustand von 45% hat."
            "Du setzt dich auf den Stuhl und schaust auf den Display.",
            "Auf dem Display steht, dass du 5 Minuten Zeit hast, aus der vorgegebenen URL den HTTP-Header 'server' herauszufiltern",
            f"{URL}",
            "Schreibe eine Methode <code>run(URL)</code>, um den Header zu ermitteln."]
        hints = ["Es gibt verschiedene Module, um Webrequests zu prüfen.",
                 "Verwende pip oder pip3 install requests, sofern das Package noch fehlt.",
                 "Nutze Google, um nach einer Anleitung zu suchen."]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.Header_Request, "data": URL}

    ### SOLUTIONS ###
    # Level 1
    def Header_Request(self, URL):
        from requests import get
        r = get(f'{URL}')
        return r.headers['server']

    # Level 4

    # Level 5
    def Log_File_Search(Path):
        with open(Path, 'r') as f:
                for line in f.read().splitlines():
                    Datum = rsplit(r':|\s', line)

                    if (Datum[3][1:].split('/')[1] == 'Mar' and Datum[3][1:].split('/')[0] == '07' and 'POST' in Datum[8]):
                         Ausgabe = f'{Datum[0]} {Datum[3][1:]} {Datum[4]}:{Datum[5]}:{Datum[6]} {Datum[7][1:3]}:{Datum[7][3:-1]} {Datum[8]} {Datum[9]} {Datum[10]}'

        return Ausgabe
