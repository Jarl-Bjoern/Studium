def run(Text):
    Word = ""
    Temp_Array = []

    for Text_Char in Text:
        if (Text_Char.isupper()): Word += Text_Char
    for View in range(0, len(Word)):
        if (f'{View+1} - {Word[View]}' not in Temp_Array):
            Temp_Array.append(f'{View+1} - {Word[View]}')

    return Temp_Array
