from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askquestion
import loadingfile

pathpodzielony = 0
dane = 0
height = 5
width = 5
kategorie = 0
choice = 0


def askcategory():
    global choice
    choice = askquestion("Category", "Does the file contain data category names in the first line?\nCheck and select "
                                     "the appropriate option. Otherwise the file may not load correctly.")
    if choice == 'yes':
        return 1
    elif choice == 'no':
        return 2


def Error():
    error = Tk()
    error.title('Error')

    infoplik = Label(error, text="Error")
    infoplik.grid(row=1, column=2)
    przycisk1 = Button(error, text='OK', command=error.destroy)
    przycisk1.grid(row=1, column=1, sticky="news")

    error.mainloop()


class GUI:
    def __init__(self):
        def Clean():
            global pathpodzielony
            global dane
            global height
            global width
            global kategorie
            global choice
            pathpodzielony = 0
            dane = 0
            height = 5
            width = 5
            kategorie = 0
            choice = 0
            textboxloadedfile.delete('1.0', END)
            root.destroy()

        def WybierzPlikWindow():
            global pathpodzielony
            rawpath = askopenfilename()
            pathpelny = rawpath.replace('/', '\\')
            pathpodzielony = pathpelny.split('\\')
            print(pathpelny)
            textboxloadedfile.delete('1.0', END)
            textboxloadedfile.insert(END, pathpelny)

        def LoadFile():
            global pathpodzielony
            global dane
            global kategorie
            dane = loadingfile.zaladujplik(pathpodzielony)
            loadingfile.wykryjkolumny()
            if choice == "yes":
                kategorie = loadingfile.odczytajkolumny()
                print(len(kategorie), kategorie)
                print("Z kategorią")
            elif choice == "no":
                kategorie = loadingfile.odczytajilosckolumn()
                print(kategorie)
                print("Bez kategorii")
            danezlisty = loadingfile.odczytajdane()
            root.destroy()

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

        if not dane == 0:
            if type(kategorie) == list:
                ilosckategorii = len(kategorie)
                for naglowek, j in zip(kategorie, range(ilosckategorii)):
                    g = 3
                    h = 3 + j
                    b = Label(root, text=naglowek, height=1, width=10)
                    b.grid(row=g, column=h)
            elif type(kategorie) == int:
                kolumna = 1
                for j in range(kategorie):  # Columns
                    Column = "Column #" + str(kolumna)
                    g = 3
                    h = 3 + j
                    b = Label(root, text=Column, height=1, width=10)
                    b.grid(row=g, column=h)
                    kolumna += 1
        else:
            pass

        root.mainloop()
