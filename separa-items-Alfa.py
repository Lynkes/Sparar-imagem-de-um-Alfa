import cv2
import numpy as np

# Carregue a imagem
caminho_imagem = "E:/Sparar imagem de um Alfa/test.png"
imagem = cv2.imread(caminho_imagem, cv2.IMREAD_UNCHANGED)

# Verifique se a imagem foi carregada corretamente
if imagem is None:
    print(f"Erro ao carregar a imagem em {caminho_imagem}")
else:
    # Extraia os canais RGBA
    if imagem.shape[2] == 4:  # Verifique se a imagem tem 4 canais (RGBA)
        canal_alpha = imagem[:, :, 3]

        # Encontre contornos na imagem alpha
        contornos, _ = cv2.findContours(canal_alpha, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Salve cada item isolado
        for i, contorno in enumerate(contornos):
            x, y, w, h = cv2.boundingRect(contorno)
            item = imagem[y:y+h, x:x+w]

            cv2.imwrite(f'item_{i+1}.png', item)
    else:
        print("A imagem não possui canal alfa (transparência)")
