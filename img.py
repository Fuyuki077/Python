import os
import numpy as np
import cv2 as cv

import tkinter as t
from PIL import Image, ImageTk


os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system('cls')

def olaCallBack():
    print("Hello World!")
    input01.delete(0, t.END)
    input01.insert(0, "Hello world!")

#   img = cv.imread("img.png") + 255
img = np.zeros((10, 10, 3), dtype=np.uint8) + 255
img[4, 7, :] = 0
imgBIG = cv.resize(img, (0,0), fx=20, fy=20, interpolation=cv.INTER_AREA)
#   cv.imshow("janela 01", imgBIG)
#   cv.waitKey(0)


mainWindow = t.Tk()
mainWindow.title("Janela com imagem")
mainWindow.geometry("400x300")

PILimg = Image.fromarray(imgBIG)
PILimgTk = ImageTk.PhotoImage(Image=PILimg)

rotulo01 = t.Label(mainWindow, text="Minha Imagem")
rotulo01.place(x=20, y=20)

btn_01 = t.Button(mainWindow, text="Botão olá mundo!", command=olaCallBack)
btn_01.place(x=20, y=20)
#   btn_01.pack()

input01 = t.Entry(mainWindow)
input01.place(x=20, y=20)

mainWindow.mainloop()