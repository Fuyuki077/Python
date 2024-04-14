import cv2
import numpy as np


def desenhar_quadrado(img):
    # Calcula as coordenadas do centro da imagem
    centro_x = img.shape[1] // 2
    centro_y = img.shape[0] // 2

    # Define o tamanho do quadrado dos pontos
    tamanho_quadrado = 100

    # define as cores
    blue = [0, 0, 255]
    red = [255, 0, 0]

    # Calcula as coordenadas dos vértices do quadrado
    ponto1 = (centro_x - tamanho_quadrado // 2,
              centro_y - tamanho_quadrado // 2)
    ponto2 = (centro_x + tamanho_quadrado // 2,
              centro_y - tamanho_quadrado // 2)
    ponto3 = (centro_x + tamanho_quadrado // 2,
              centro_y + tamanho_quadrado // 2)
    ponto4 = (centro_x - tamanho_quadrado // 2,
              centro_y + tamanho_quadrado // 2)

    # Desenha os pontos no centro da imagem
    cv2.circle(img, ponto1, 0, blue, -1)
    cv2.circle(img, ponto2, 0, red, -1)
    cv2.circle(img, ponto3, 0, red, -1)
    cv2.circle(img, ponto4, 0, blue, -1)


    # Conecta os pontos com gradiente de cor
    for i in range(200):
        cor = (
            int((1 - i / 200) * 0 + (i / 200) * 255),   # Gradiente para o canal R
            int((1 - i / 200) * 0 + (i / 200) * 0),     # Gradiente para o canal G
            int((1 - i / 200) * 255 + (i / 200) * 0)    # Gradiente para o canal B
        )
        # Calcula a posição intermediária ao longo da linha entre ponto1 e ponto2
        x1_intermediario = int(ponto1[0] + (i / 200) * (ponto2[0] - ponto1[0]))
        y1_intermediario = int(ponto1[1] + (i / 200) * (ponto2[1] - ponto1[1]))
        cv2.circle(img5, (x1_intermediario, y1_intermediario), 0, cor, 1)

        # Calcula a posição intermediária ao longo da linha entre ponto4 e ponto3
        x2_intermediario = int(ponto4[0] + (i / 200) * (ponto3[0] - ponto4[0]))
        y2_intermediario = int(ponto4[1] + (i / 200) * (ponto3[1] - ponto4[1]))
        cv2.circle(img4, (x2_intermediario, y2_intermediario), 0, cor, 1)
        cv2.circle(img5, (x2_intermediario, y2_intermediario), 0, cor, 1)

        # Conecta o ponto1 ao ponto4 sem transição de cor
        cv2.line(img3, ponto1, ponto4, blue, 1)
        # Conecta o ponto1 ao ponto4 sem transição de cor
        cv2.line(img3, ponto2, ponto3, red, 1)

        # Conecta o ponto1 ao ponto4 sem transição de cor
        cv2.line(img4, ponto1, ponto4, blue, 1)
        # Conecta o ponto1 ao ponto4 sem transição de cor
        cv2.line(img4, ponto2, ponto3, red, 1)

        # Conecta o ponto1 ao ponto4 sem transição de cor
        cv2.line(img5, ponto1, ponto4, blue, 1)
        # Conecta o ponto1 ao ponto4 sem transição de cor
        cv2.line(img5, ponto2, ponto3, red, 1)

    # Exibe a imagem
    cv2.imshow("Quadrado", img)


# Define o título da janela
titulo_janela = "Quadrado"


# Cria uma imagem preta de 600x600 pixels
img2 = 0 * np.zeros((600, 600, 3), dtype=np.uint8)

# Cria uma segunda imagem preta de 600x600 pixels
img3 = 0 * np.ones((600, 600, 3), dtype=np.uint8)

# Cria uma imagem preta de 600x600 pixels
img4 = 0 * np.ones((600, 600, 3), dtype=np.uint8)

# Cria uma segunda imagem preta de 600x600 pixels
img5 = 0 * np.ones((600, 600, 3), dtype=np.uint8)

# Desenha o quadrado na segunda imagem
desenhar_quadrado(img2)

# Aguarda por uma tecla
cv2.waitKey(0)

# Fecha a segunda janela
cv2.destroyAllWindows()

# Desenha o quadrado na segunda imagem
desenhar_quadrado(img3)

# Aguarda por uma tecla
cv2.waitKey(0)

# Fecha todas as janelas ao pressionar uma tecla
cv2.destroyAllWindows()

# Desenha o quadrado na segunda imagem
desenhar_quadrado(img4)

# Aguarda por uma tecla
cv2.waitKey(0)

# Fecha a segunda janela
cv2.destroyAllWindows()

# Desenha o quadrado na segunda imagem
desenhar_quadrado(img5)

# Aguarda por uma tecla
cv2.waitKey(0)

# Fecha todas as janelas ao pressionar uma tecla
cv2.destroyAllWindows()
