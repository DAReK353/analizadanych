from os import chdir

dane = 0


def loadfile(pathpodzielony):
    global dane
    s = "\\"
    pathbezpliku = s.join(pathpodzielony[:-1])
    chdir(pathbezpliku)
    dane = open(pathpodzielony[-1], 'r')
    print(dane.read())

    return dane
