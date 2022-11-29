import tkinter
from tkinter import*
root=Tk("окно")
root.title("Площадь круга")
root.geometry("500x400+300+200")
nadpis_R = Label(root, text = 'Введите радиус', font = 'Arial 12')
nadpis_Pl = Label(root, text = 'Площадь:', font = 'Arial 12')
r = DoubleVar()
vvod_radiusa = Entry(root, width = 10, textvariable = r)
pl = DoubleVar()
vivod_plo = Entry(root, width = 15, textvariable = pl)
knopka_raschet = Button(root, text = 'Расчет', width = 10)
knopka_vihod = Button(root, text = 'Выход', width = 10)
nadpis_R.grid(row = 0, column = 0)
radius_entry.grid(row = 0, column = 1)
nadpis_Pl.grid(row = 1, column = 0)
plo.grid(row = 1, column =1)
knopka_raschet.grid(row = 2, column = 0)
knopka_vihod.grid(row = 2, column = 1)
knopka_raschet.bind('<Button-1>', Raschet_Plo)
def Raschet_Plo(event):
    radius = r.get()
    ploschad = 3.14 * radius**2
    pl.set('%.3f'% ploschad)
def Vihod(event):
root.destroy()
knopka_vihod.bind('<Button-1>', Vihod)
