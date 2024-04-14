from tkinter import *

janelaA = Tk()
janelaA.title("Quadrado1")
janelaA['bg'] = "black"
janelaA.geometry("600x600")

pontoR1 = LabelFrame(background="#ff0000").place(x=200,y=200)
pontoR2 = LabelFrame(background="#ff0000").place(x=200,y=400)
pontoB2 = LabelFrame(background="#0000ff").place(x=400,y=200)
pontoB1 = LabelFrame(background="#0000ff").place(x=400,y=400)



janelaA.mainloop()

janelaB = Tk()
janelaB.title("Quadrado2")
janelaB['bg'] = "black"
janelaB.geometry("600x600")

pontoR1 = LabelFrame(background="#ff0000").place(x=200,y=200)
pontoR2 = LabelFrame(background="#ff0000").place(x=200,y=400)
pontoB2 = LabelFrame(background="#0000ff").place(x=400,y=200)
pontoB1 = LabelFrame(background="#0000ff").place(x=400,y=400)


linhaR = LabelFrame(width=1, height=200, bg="#ff0000")
linhaR.pack()
linhaR.place(x=200,y=200)

linhaB = LabelFrame(width=1, height=200, bg="#0000ff")
linhaB.pack()
linhaB.place(x=400,y=200)

janelaB.mainloop()

janelaC = Tk()
janelaC.title("Quadrado2")
janelaC['bg'] = "black"
janelaC.geometry("600x600")

pontoR1 = LabelFrame(background="#ff0000").place(x=200,y=200)
pontoR2 = LabelFrame(background="#ff0000").place(x=200,y=400)
pontoB2 = LabelFrame(background="#0000ff").place(x=400,y=200)
pontoB1 = LabelFrame(background="#0000ff").place(x=400,y=400)


linhaR = LabelFrame(width=1, height=200, bg="#ff0000")
linhaR.pack()
linhaR.place(x=200,y=200)

linhaB = LabelFrame(width=1, height=200, bg="#0000ff")
linhaB.pack()
linhaB.place(x=400,y=200)

linhaBD1 = LabelFrame(width=200, height=1)
linhaBD1.S("red.Horizontal.TProgressbar", foreground='red', background='red')
linhaBD1.pack()
linhaBD1.place(x=200,y=400)

janelaC.mainloop()
