from EscapeRoom import EscapeRoom
from os import listdir
from os.path import dirname, join, realpath
from random import randint

class Room_Schwab(EscapeRoom):
    def __init__(self):
        super().__init__()
        self.set_metadata("Julia Schwab-Di Benedetto", __name__)
        self.add_level(self.create_level4())
        self.add_level(self.create_level5())

    ### LEVELS ###
    def create_level4(self):
        PW_Len = 8
        
        task_messages = ["Der erste Raum wurde erfolgreich durchlaufen, aber die Challenge ist noch nicht vorbei. Folgendes erscheint auf dem Display:",
                        "Nicht schlecht! Aber das geht noch besser!",
                        "Um sicherzustellen, dass dein Aufnahmetest nicht hier endet, generiere ein Passwort mit 8 Zeichen, das Kleinbuchstaben, Großbuchstaben, Zahlen und Sonderzeichen enthält.",
                        "Validiere dein Ergebnis!"]
                        
        hints = ["Versuche die PW-Generierung und PW-Validierung in 2 Methoden aufzuteilen.",
                 "Du musst nicht unbedingt alle benötigten Zeichen einzeln aufschreiben.",
                 "Informiere dich was random bewirkt."]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.Passwort, "data": PW_Len}

    
    def create_level5(self):
        Work_Path, Script_Path = "rooms/Level_5", dirname(realpath(__file__))
        Directory = join(Script_Path, Work_Path)

        task_messages = ["Nur noch ein Rätsel trennt dich von der Aufnahme in die Hackergruppe. Es lautet:."
                        "Um zu zeigen, dass du alle notwendigen Fähigkeiten besitzt, musst du zeigen,",
                        "dass du in der Lage bist, Informationen aus Log Files herauszulesen.",
                        'Schreibe eine Methode <code>run(Directory)</code>, die alle Lines ausgibt vom "07/Mar" und die eine "POST"-Request-Methode enthalten.',
                        "Sollten sich in der Liste leere Felder befinden, gebe diese nicht aus."]
        
        hints = ["Recherchiere wie du Strings auftrennen und zusammenfügen kannst.",
                "Vielleicht macht es Sinn den String nicht nur nach Leerzeichen zu trennen.",
                "Stelle sicher, dass beim Aufsplitten jedes List Item in einer neuen Zeile dargestellt wird."]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.Log_File_Search, "data": Directory}

    ### SOLUTIONS ###
    # Level 1
    def Passwort(self):
        def PW_Generator(PW_Len):
            word = ""
            for _ in range(0, int(PW_Len)+1):
                word += chr(randint(33,126))
            return word

        #Von hier ab Validierung des Passworts
        def PW_Check(Pass):
            l, u, p, d = 0, 0, 0, 0
            symbols = string.punctuation
            for i in Pass:
                # Zaehlen Kleinbuchstaben
                if (i.islower()):
                    l+=1

                # Zaehlen Grossbuchstaben
                elif (i.isupper()):
                    u+=1

                # Zaehlen Zahlen
                elif (i.isdigit()):
                    d+=1

                # Zaehlen Sonderzeichen
                elif(i in symbols):
                    p+=1

            if (l > 1 and u > 1 and p > 1 and d > 1):
                return True

        Hilf = ""
        while True:
            Pass = PW_Generator(8)
            Vorgang = PW_Check(Pass)

            if (Vorgang == True):
                Hilf = "Valides Passwort"
                break

        return Hilf 

    # Level 5
    def Log_File_Search(Path):
        with open(Path, 'r') as f:
                for line in f.read().splitlines():
                    Datum = rsplit(r':|\s', line)

                    if (Datum[3][1:].split('/')[1] == 'Mar' and Datum[3][1:].split('/')[0] == '07' and 'POST' in Datum[8]):
                         Ausgabe = f'{Datum[0]} {Datum[3][1:]} {Datum[4]}:{Datum[5]}:{Datum[6]} {Datum[7][1:3]}:{Datum[7][3:-1]} {Datum[8]} {Datum[9]} {Datum[10]}'

        return Ausgabe
