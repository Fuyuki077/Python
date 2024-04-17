import cv2
import numpy as np

def desenhar_linha_dda(img, x1, y1, x2, y2, red):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        passos = abs(dx)
    else:
        passos = abs(dy)

    x_inc = dx / passos
    y_inc = dy / passos

    x = x1
    y = y1

    for i in range(int(passos) + 1):
        img[int(round(y)), int(round(x))] = red
        x += x_inc
        y += y_inc

# Criar uma imagem em branco
img = np.zeros((300, 300, 3), dtype=np.uint8)

# Coordenadas iniciais e finais da linha
x1, y1 = 50, 50
x2, y2 = 80, 200

# Cor da linha (vermelho)
red = (0, 0, 255)

# Desenhar linha usando o método DDA
desenhar_linha_dda(img, x1, y1, x2, y2, red)

# Mostrar imagem
cv2.imshow("Linha DDA", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



def desenha_linha_analitica(img, x1, y1, x2, y2, green=(0, 255, 0)):
    """
    Desenha uma linha na imagem usando o método analítico.

    """
    if x2 - x1 == 0:
        for y in range(y1, y2 + 1):
            img[x1, y] = green
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y2 - m * x2
        for x in range(x1, x2 + 1):
            y = int(m * x + b)
            img[y, x] = green

# Exemplo de uso:
img = np.zeros((300, 300, 3), dtype=np.uint8)
x1, y1 = 50, 50
x2, y2 = 80, 200
desenha_linha_analitica(img, x1, y1, x2, y2)

# Mostra a imagem com a linha desenhada
cv2.imshow('Linha Analitica', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# É possivel obervar neste exemplo de coordenada a linha dda é mais precisa que a linha analitica
# Este fenomeno fica claro pois no calculo para x de x1 ate x2 que para cada passo do x so é atribuido um passo de y ao inves de fazer o caminho todo