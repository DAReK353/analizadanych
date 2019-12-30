from tkinter import *


class MainWindow:
    def __init__(self):
        root = Tk()
        root.title('Data Analyzer')

        infologi = Label(root, text="Logs")
        infologi.grid(row=1, column=1)
        textboxlogi = Text(root, height=20, width=50)
        textboxlogi.grid(row=2, column=1, rowspan=10)

        root.mainloop()
