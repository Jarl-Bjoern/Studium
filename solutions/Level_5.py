def run(Path):
    from re import split as rsplit
    
    Temp_Array = []
    with open(Path, 'r') as f:
            for line in f.read().splitlines():
                Datum = rsplit(r':|\s', line)

                if (Datum[3][1:].split('/')[1] == 'Mar' and Datum[3][1:].split('/')[0] == '07' and 'POST' in Datum[8]):
                    Ausgabe = f'{Datum[0]} {Datum[3][1:]} {Datum[4]}:{Datum[5]}:{Datum[6]} {Datum[7][1:3]}:{Datum[7][3:-1]} {Datum[8]} {Datum[9]} {Datum[10]}'
                    if (Ausgabe not in Temp_Array):
                        Temp_Array.append(Ausgabe)
    return Temp_Array
