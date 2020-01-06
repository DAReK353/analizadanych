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
    choice = askquestion("Category", "Does the file contain data category names in the first line?")
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
            kategorie = loadingfile.wykryjkolumny()
            if choice == "yes":
                print(type(kategorie[1]), len(kategorie), kategorie)
                print("Z kategorią")
            elif choice == "no":
                print("Bez kategorii")
            danezlisty = loadingfile.odczytajdane()
            print(danezlisty)

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
        textboxloadedfile.grid(row=2, column=2, columnspan=10)

        if not kategorie == 0:
            for i in range(height):  # Rows
                for j in range(width):  # Columns
                    g = 4 + j
                    h = 1 + i
                    b = Entry(root, text="")
                    b.grid(row=g, column=h)

        root.mainloop()

        exit()
