import cv2

imagem = cv2.imread("FluorescentCells.jpg")
#imagem = cv2.imread("FluorescentCells.jpg",0) -> muda a cor da imagem para preto e branco
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
