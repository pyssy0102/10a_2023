import tkinter
from tkinter import*
root=Tk("окно")
root.title("заголовок")
root.geometry("500x400+300+200")
ramka = Frame(root)
knopka1 = Button(ramka, text = 'Кнопка 1')
knopka2 = Button(ramka, text = 'Кнопка 2')
knopka3 = Button(ramka, text = 'Кнопка 3')
ramka.pack()
knopka1.grid(row = 0, column = 0)
knopka2.grid(row = 0, column = 1)
knopka3.grid(row = 0, column = 2)
