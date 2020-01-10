from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askquestion, showerror
from tkinter.ttk import Progressbar

import loadingfile

pathpodzielony = 0
dane = 0
height = 5
width = 5
kategorie = 0
choice = 0
pathpelny = "Empty"


def askcategory():
    global choice
    choice = askquestion("Category", "Does the file contain data category names in the first line?\nCheck and select "
                                     "the appropriate option. Otherwise the file may not load correctly.")
    if choice == 'yes':
        return 1
    elif choice == 'no':
        return 2


def Error(wiadomosc):
    showerror("Error", wiadomosc)


class GUI:
    def __init__(self):
        def Clean():
            global pathpodzielony, dane, height, width, kategorie, choice, pathpelny
            pathpodzielony = 0
            dane = 0
            height = 5
            width = 5
            kategorie = 0
            choice = 0
            pathpelny = "Empty"
            textboxloadedfile.delete('1.0', END)
            textboxloadedfile.insert(END, pathpelny)

        def WybierzPlikWindow():
            global pathpodzielony, pathpelny
            rawpath = askopenfilename()
            pathpelny = rawpath.replace('/', '\\')
            pathpodzielony = pathpelny.split('\\')
            print(pathpelny)
            textboxloadedfile.delete('1.0', END)
            textboxloadedfile.insert(END, pathpelny)

        def LoadFile():
            global pathpodzielony, dane, kategorie
            try:
                dane = loadingfile.zaladujplik(pathpodzielony)
                loadingfile.wykryjkolumny()
            except:
                error1 = "No file selected."
                Error(error1)

            if choice == "yes":
                kategorie = loadingfile.odczytajkolumny()
                print("Z kategorią:", len(kategorie), kategorie)
                oknodane()
            elif choice == "no":
                kategorie = loadingfile.odczytajilosckolumn()
                print("Bez kategorii:", kategorie)
                oknodane()
            else:
                pass

        def oknodane():
            global kategorie
            danewyniki = Tk()
            danewyniki.title('Results')

            if not dane == 0:
                loadingfile.odczytajdane()
                loadingfile.obliczenia()
                if type(kategorie) == list:
                    ilosckategorii = len(kategorie)
                    for naglowek, j in zip(kategorie, range(ilosckategorii)):
                        g = 3
                        h = 1 + j
                        b = Label(danewyniki, text=naglowek, height=1, width=10)
                        b.grid(row=g, column=h)

                elif type(kategorie) == int:
                    kolumna = 1
                    for j in range(kategorie):
                        Column = "Column #" + str(kolumna)
                        g = 3
                        h = 1 + j
                        b = Label(danewyniki, text=Column, height=1, width=10)
                        b.grid(row=g, column=h)
                        kolumna += 1
                else:
                    error3 = "Unable to load columns."
                    Error(error3)
                    pass

                srednia = loadingfile.getsrednia()
                iloscsrednia = len(srednia)
                infosrednia = Label(danewyniki, text="Average:")
                infosrednia.grid(row=4, column=0)
                for s, i in zip(srednia, range(iloscsrednia)):
                    g = 4
                    h = 1 + i
                    b = Text(danewyniki, height=1, width=10)
                    b.grid(row=g, column=h)
                    b.delete('1.0', END)
                    b.insert(END, s)

                maxliczba = loadingfile.getmaxliczba()
                iloscmax = len(maxliczba)
                infosrednia = Label(danewyniki, text="Max Number:")
                infosrednia.grid(row=5, column=0)
                for s, i in zip(maxliczba, range(iloscmax)):
                    g = 5
                    h = 1 + i
                    b = Text(danewyniki, height=1, width=10)
                    b.grid(row=g, column=h)
                    b.delete('1.0', END)
                    b.insert(END, s)

                minliczba = loadingfile.getminliczba()
                iloscmin = len(minliczba)
                infosrednia = Label(danewyniki, text="Min Number:")
                infosrednia.grid(row=6, column=0)
                for s, i in zip(minliczba, range(iloscmin)):
                    g = 6
                    h = 1 + i
                    b = Text(danewyniki, height=1, width=10)
                    b.grid(row=g, column=h)
                    b.delete('1.0', END)
                    b.insert(END, s)
            else:
                pass

        root = Tk()
        root.title('Data Analyzer')

        przycisk1 = Button(root, text='Select File', command=WybierzPlikWindow)
        przycisk1.grid(row=1, column=1, sticky="news")
        przycisk2 = Button(root, text='Load File', command=LoadFile)
        przycisk2.grid(row=1, column=2, sticky="news")
        przycisk3 = Button(root, text='Reset', command=Clean)
        przycisk3.grid(row=1, column=3, sticky="news")
        przycisk5 = Button(root, text='Exit', command=exit)
        przycisk5.grid(row=1, column=20, sticky="news")

        infoplik = Label(root, text="Selected File:")
        infoplik.grid(row=2, column=1)
        textboxloadedfile = Text(root, height=1, width=50)
        textboxloadedfile.grid(row=2, column=2)

        textboxloadedfile.delete('1.0', END)
        textboxloadedfile.insert(END, pathpelny)

        root.mainloop()
