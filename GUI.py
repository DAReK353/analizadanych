from tkinter import *
from tkinter.filedialog import askopenfilename
import loadingfile

pathpodzielony = 0
fsafsa = 0
dane = 0
height = 5
width = 5


class GUI:
    def __init__(self):
        def WybierzPlikWindow():
            global pathpodzielony
            rawpath = askopenfilename()
            pathpelny = rawpath.replace('/', '\\')
            pathpodzielony = pathpelny.split('\\')
            print(pathpodzielony)
            textboxloadedfile.delete('1.0', END)
            textboxloadedfile.insert(END, pathpodzielony[-1])

        def LoadFile():
            global pathpodzielony
            global dane
            dane = loadingfile.loadfile(pathpodzielony)
            print(dane.read())
            #textboxloadedfile.delete('1.0', END)
            #textboxloadedfile.insert(END, 'Unable to open file.')

        root = Tk()
        root.title('Data Analyzer')

        przycisk1 = Button(root, text='Select File', command=WybierzPlikWindow)
        przycisk1.grid(row=1, column=1, sticky="news")
        przycisk2 = Button(root, text='Load File', command=LoadFile)
        przycisk2.grid(row=1, column=2, sticky="news")
        przycisk3 = Button(root, text='Clean', command=WybierzPlikWindow)
        przycisk3.grid(row=1, column=3, sticky="news")
        przycisk5 = Button(root, text='Exit', command=exit)
        przycisk5.grid(row=1, column=5, sticky="news")

        infoplik = Label(root, text="Selected File:")
        infoplik.grid(row=2, column=1)
        textboxloadedfile = Text(root, height=1, width=15)
        textboxloadedfile.grid(row=2, column=2)

        if fsafsa > 0:
            for i in range(height):  # Rows
                for j in range(width):  # Columns
                    g = 4 + j
                    h = 1 + i
                    b = Entry(root, text="")
                    b.grid(row=g, column=h)

        root.mainloop()

        exit()
