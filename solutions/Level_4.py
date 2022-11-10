def run(PW_Len):
    from random import randint
    from string import punctuation
    
    def PW_Generator(PW_Len):
        word = ""
        for _ in range(0, int(PW_Len)+1):
            word += chr(randint(33,126))
        return word

    def PW_Check(Pass):
        l, u, p, d = 0, 0, 0, 0
        symbols = punctuation
        for _ in Pass:
            if (_.islower()):
                l+=1

            elif (_.isupper()):
                u+=1

            elif (_.isdigit()):
                d+=1

            elif(_ in symbols):
                p+=1

        if (l > 1 and u > 1 and p > 1 and d > 1):
            return True

    Hilf = ""
    while True:
        Pass = PW_Generator(PW_Len)

        if (PW_Check(Pass) == True):
            Hilf = "Valides Passwort"
            break

    return Hilf
