from tkinter import *
from tkinter.filedialog import askopenfilename
import os

pathpodzielony = 0


class GUI:
    def __init__(self):
        def WybierzPlikWindow():
            def select():
                global pathpodzielony
                rawpath = askopenfilename()
                pathpelny = rawpath.replace('/', '\\')
                pathpodzielony = pathpelny.split('\\')
                print(pathpodzielony)
                textboxplik.see("end")
                textboxplik.insert(END, pathpelny)
                textboxloadedfile.see("end")
                textboxloadedfile.insert(END, pathpodzielony[-1])

            wybierzplik = Tk()
            wybierzplik.title('Select File')

            info1 = Label(wybierzplik, text="File:")
            info1.grid(row=1, column=1)
            textboxplik = Text(wybierzplik, height=1, width=60)
            textboxplik.grid(row=1, column=2, columnspan=4)
            przyciskwybierz1 = Button(wybierzplik, text='Select File...', command=select)
            przyciskwybierz1.grid(row=2, column=1, columnspan=2, sticky="news")
            przyciskwybierz2 = Button(wybierzplik, text='Done', command=wybierzplik.destroy)
            przyciskwybierz2.grid(row=2, column=3, columnspan=4, sticky="news")

            wybierzplik.mainloop()

        def LoadFile():
            global pathpodzielony
            s = "\\"
            pathbezpliku = s.join(pathpodzielony[:-1])
            os.chdir(pathbezpliku)
            dane = os.open(pathpodzielony[-1], os.O_RDONLY)
            print(dane)

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
        textboxloadedfile = Text(root, height=1, width=20)
        textboxloadedfile.grid(row=2, column=2)

        root.mainloop()
