import tkinter
from tkinter import*
root=Tk("окно")
root.title("задача 29 вариант 8")
root.geometry("500x400+300+200")
nadp_A = Label(root, text = 'введите сторону a', font = 'Arial 12')
nadp_B = Label(root, text = 'введите сторону b', font = 'Arial 12')
nadp_h = Label(root, text = 'введите высоту h', font = 'Arial 12')
nadp_С = Label(root, text = 'сторона c', font = 'Arial 12')
nadp_alpha = Label(root, text = 'угол alpha', font = 'Arial 12')
nadp_beta = Label(root, text = 'угол beta', font = 'Arial 12')
nadp_gamma = Label(root, text = 'угол gamma', font = 'Arial 12')
nadp_S= Label(root, text = 'площадь S', font = 'Arial 12')
nadp_P = Label(root, text = 'периметр P', font = 'Arial 12')
A = DoubleVar()
vA = Entry(root, width=15 , textvariable = A)
B = DoubleVar()
vB= Entry(root, width=15 , textvariable = B)
h = DoubleVar()
vh= Entry(root, width=15 , textvariable = h)
C = DoubleVar()
vC= Entry(root, width=15 , textvariable = C)
alpha = DoubleVar()
valpha= Entry(root, width=15 , textvariable =alpha )
beta = DoubleVar()
vbeta= Entry(root, width=15 , textvariable =beta )
gamma = DoubleVar()
vgamma= Entry(root, width=15 , textvariable =gamma )
S = DoubleVar()
vS= Entry(root, width=15 , textvariable = S)
P = DoubleVar()
vP= Entry(root, width=15 , textvariable = P)
nadp_A.grid(row = 0, column = 0)
vA.grid(row = 0, column = 1)
nadp_B.grid(row = 1, column = 0)
vB.grid(row = 1, column = 1)
nadp_h.grid(row = 2, column = 0)
vh.grid(row = 2, column = 1)
nadp_С.grid(row = 3, column = 0)
vC.grid(row = 3, column = 1)
nadp_alpha.grid(row = 4, column = 0)
valpha.grid(row = 4, column = 1)
nadp_beta.grid(row = 5, column = 0)
vbeta.grid(row = 5, column = 1)
nadp_gamma.grid(row = 6, column = 0)
vgamma.grid(row = 6, column = 1)
nadp_S.grid(row = 7, column = 0)
vS.grid(row = 7, column = 1)
nadp_P.grid(row = 8, column = 0)
vP.grid(row = 8, column = 1)
knopka_raschet = Button(root, text = 'Расчет', width = 10)
knopka_vihod = Button(root, text = 'Выход', width = 10)
knopka_raschet.grid(row = 9, column = 0)
knopka_vihod.grid(row = 9, column = 1)
def Raschet(event):
    storA = A.get()
    storh = h.get()
    storS = 1/2* storA* storh
    S.set('%.3f'% storS)
knopka_raschet.bind('<Button-1>', Raschet)
def Raschet(event):
    storh = h.get()
    storB = B.get()
    storalpha=storh/storB
    alpha.set('%.3f'% storalpha)
knopka_raschet.bind('<Button-1>', Raschet)
def Raschet(event):
    storh = h.get()
    storA = A.get()
    storbeta=storh/storA
    beta.set('%.3f'% storbeta)
knopka_raschet.bind('<Button-1>', Raschet)
def Raschet(event):
    storalpha =alpha.get()
    storbeta=beta .get()
    storgamma=180-(storalpha+storbeta)
    gamma.set('%.3f'% storgamma)
knopka_raschet.bind('<Button-1>', Raschet)
def Raschet(event):
    storA =A.get()
    storB=B.get()
    storgamma=gamma.get()
    storC=('sqrt storB2+storA2-2*storB*storA*storgamma')
    C.set('%.3f'% storC)
knopka_raschet.bind('<Button-1>', Raschet)
def Raschet(event):
    storA =A.get()
    storB=B.get()
    storC=C.get()
    storP=storA+storB+storC
    P.set('%.3f'% storP)
knopka_raschet.bind('<Button-1>', Raschet)

















