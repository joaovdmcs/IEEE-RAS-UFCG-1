import cv2
imagem = cv2.imread('entrada.jpg')

for i in range(0,imagem.shape[0]):
    for j in range(0,imagem.shape[1]):
        imagem[i,j] = (0,(i*j)%256,0) 

cv2.imshow('Imagem modificada', imagem)
cv2.waitKey(0) 