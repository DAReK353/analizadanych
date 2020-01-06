from os import chdir
import GUI

dane = 0


def loadfile(pathpodzielony):
    global dane
    s = "\\"
    pathbezpliku = s.join(pathpodzielony[:-1])
    chdir(pathbezpliku)
    dane = open(pathpodzielony[-1], 'r')
    #print(dane.read())

    return dane


def detectcolumns():
    opcja = GUI.askcategory()
    if opcja == 1:
        print("Opcja 1")
        return odczytajkolumny()
    elif opcja == 2:
        print("Opcja 2")
    else:
        GUI.Error()

    #for line in tekst:
    #   nazwazpliku, liczbazpliku = line.split(";")
    #   liczbazpliku = liczbazpliku.strip()


def odczytajkolumny():
    global dane
    firstline = dane.readline()
    firstline = firstline.strip()
    #print(firstline)
    #ilosckategorii = firstline.count(",") + 1
    #print(ilosckategorii)
    kategorie = firstline.split(",")

    return kategorie
