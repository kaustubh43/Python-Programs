import tkinter as tk
from tkinter import *
from tkinter import ttk


class Karl(Frame):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.newWindow = None
        self.pack()
        self.master.title("Karlos")
        self.button1 = Button(self, text="Click please", width=25, command=self.new_window)
        self.button1.grid(row=0, column=1, columnspan=2, sticky=W+E+N+S)

    def new_window(self):
        self.newWindow = Karl2()


class Karl2(Frame):
    def __init__(self):
        new = tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("karlos More Window")
        new.button = tk.Button(text="PRESS TO CLOSE", width=25, command=self.close_window)
        new.button.pack()

    def close_window(self):
        self.destroy()


def main():
    Karl().mainloop()


if __name__ == '__main__':
    main()
