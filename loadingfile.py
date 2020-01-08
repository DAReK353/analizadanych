from os import chdir
import GUI

dane = 0
danezlisty = 0
kategorie = 0
sredniadanych = []
maxliczba = []
minliczba = []


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
    global dane, kategorie
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
    global dane, danezlisty
    danezlisty = []
    for line in dane:
        line = line.strip()
        asd = line.split(",")
        danezlisty.append(asd)

    #return danezlisty


def obliczenia():
    global danezlisty, kategorie
    global sredniadanych, maxliczba, minliczba
    if type(kategorie) == list:
        ilosckategorii = len(kategorie)
        for u in range(ilosckategorii):
            temp = []
            for p in danezlisty:
                teme1 = p[u]
                try:
                    tem1 = int(teme1)
                    temp.append(tem1)
                except ValueError:
                    pass

            try:
                maxliczb = max(temp)
                maxliczba.append(maxliczb)
            except ValueError:
                maxliczba.append(0)
            try:
                minliczb = min(temp)
                minliczba.append(minliczb)
            except ValueError:
                minliczba.append(0)

            temp1 = sum(temp)
            temp2 = len(temp)
            try:
                srednia = temp1 / temp2
            except ZeroDivisionError:
                srednia = 0
            sredniadanych.append(srednia)
        print(len(sredniadanych), sredniadanych)
        print(len(maxliczba), maxliczba)
        print(len(minliczba), minliczba)
