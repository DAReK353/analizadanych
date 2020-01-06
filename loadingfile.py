from os import chdir
import GUI

dane = 0


def zaladujplik(sciezkapodzielona):
    global dane
    s = "\\"
    sciezkabezpliku = s.join(sciezkapodzielona[:-1])
    chdir(sciezkabezpliku)
    dane = open(sciezkapodzielona[-1], 'r')

    return dane


def wykryjkolumny():
    opcja = GUI.askcategory()
    if opcja == 1:
        return odczytajkolumny()
    elif opcja == 2:
        return 0
    else:
        GUI.Error()


def odczytajkolumny():
    global dane
    firstline = dane.readline()
    firstline = firstline.strip()
    kategorie = firstline.split(",")

    return kategorie


def odczytajdane():
    global dane
    danezlisty = []
    for line in dane:
        line = line.strip()
        asd = line.split(",")
        danezlisty.append(asd)

    return danezlisty
