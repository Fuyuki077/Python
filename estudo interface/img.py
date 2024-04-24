import os
import tkinter as t
import numpy as np
import cv2
from PIL import Image, ImageTk


os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system('cls')

def olacallback():
    print("Hello World!")
    input01.delete(0, t.END)
    input01.insert(0, "Hello world!")

#   img = cv2.imread("img.png") + 255
img = np.zeros((10, 10, 3), dtype=np.uint16) + 255
img[4, 7, :] = 0
imgBIG = cv2.resize(img, (0,0), fx = 20, fy = 20, interpolation = cv2.INTER_AREA)
#   cv2.imshow("janela 01", imgBIG)
#   cv2.waitKey(0)

mainWindow = t.Tk()
mainWindow.title("Janela com imagem")
mainWindow.geometry("400x300")

PILimg = Image.fromarray(imgBIG)
PILimgTk = ImageTk.PhotoImage(Image=PILimg)

rotulo01 = t.Label(mainWindow, text="Minha Imagem")
rotulo01.place(x = 20, y = 20)

btn_01 = t.Button(mainWindow, text="Botão olá mundo!", command = olacallback)
btn_01.place(x = 20, y = 20)
#   btn_01.pack()

input01 = t.Entry(mainWindow)
input01.place(x = 20, y = 20)

mainWindow.mainloop()
