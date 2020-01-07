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
    try:
        GUI.askcategory()
    except:
        GUI.Error()


def odczytajkolumny():
    global dane
    firstline = dane.readline()
    firstline = firstline.strip()
    kategorie = firstline.split(",")

    return kategorie


def odczytajilosckolumn():
    global dane
    firstline = dane.readline()
    firstline = firstline.strip()
    ilosckolumn = firstline.split(",")
    ilosckolumn = len(ilosckolumn)
    dane.seek(0)

    return ilosckolumn


def odczytajdane():
    global dane
    danezlisty = []
    for line in dane:
        line = line.strip()
        asd = line.split(",")
        danezlisty.append(asd)

    return danezlisty
