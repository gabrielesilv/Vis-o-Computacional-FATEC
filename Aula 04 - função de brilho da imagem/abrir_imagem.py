import cv2

imagem = cv2.imread("baboon.jpg")
#imagem = cv2.imread("FluorescentCells.jpg",0) -> muda a cor da imagem para preto e branco
cv2.imshow("Imagem", imagem)

#o código que determina o que a imagem deve fazer tem que estar antes de waitkey
cv2.waitKey(0)
cv2.destroyALLWindows()
