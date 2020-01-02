from tkinter import *
from tkinter.filedialog import askopenfilename


class GUI:
    def __init__(self):
        def LogiWindow():
            logiokno = Tk()
            logiokno.title('Program Logs')

            infologi = Label(logiokno, text="Logs")
            infologi.grid(row=1, column=1)
            textboxlogi = Text(logiokno, height=20, width=50)
            textboxlogi.grid(row=2, column=1, rowspan=10)

            logiokno.mainloop()

        def WybierzPlikWindow():
            def aof():
                filename = askopenfilename()
                print(filename)
                nazwapliku = filename

                textboxplik.see("end")
                textboxplik.insert(END, filename)
                textboxloadedfile.see("end")
                textboxloadedfile.insert(END, filename)

            wybierzplik = Tk()
            wybierzplik.title('Select File')

            info1 = Label(wybierzplik, text="File:")
            info1.grid(row=1, column=1)
            textboxplik = Text(wybierzplik, height=1, width=60)
            textboxplik.grid(row=1, column=2, columnspan=4)
            przyciskwybierz1 = Button(wybierzplik, text='Select File...', command=aof)
            przyciskwybierz1.grid(row=2, column=1, columnspan=2, sticky="news")
            przyciskwybierz2 = Button(wybierzplik, text='Done', command=wybierzplik.destroy)
            przyciskwybierz2.grid(row=2, column=3, columnspan=4, sticky="news")

            wybierzplik.mainloop()

        root = Tk()
        root.title('Data Analyzer')

        przycisk1 = Button(root, text='Select File', command=WybierzPlikWindow)
        przycisk1.grid(row=1, column=1, sticky="news")
        przycisk2 = Button(root, text='Load File', command=LogiWindow)
        przycisk2.grid(row=1, column=2, sticky="news")
        przycisk3 = Button(root, text='Clean', command=LogiWindow)
        przycisk3.grid(row=1, column=3, sticky="news")
        przycisk4 = Button(root, text='Wyświel Logi', command=LogiWindow)
        przycisk4.grid(row=1, column=4, sticky="news")
        przycisk5 = Button(root, text='Exit', command=exit)
        przycisk5.grid(row=1, column=5, sticky="news")

        infoplik = Label(root, text="Selected File:")
        infoplik.grid(row=2, column=1)
        textboxloadedfile = Text(root, height=1, width=20)
        textboxloadedfile.grid(row=2, column=2)

        root.mainloop()
