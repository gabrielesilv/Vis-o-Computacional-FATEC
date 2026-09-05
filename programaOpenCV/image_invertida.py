import cv2

imagem = cv2.imread("FluorescentCells.jpg")
imgI = cv2.bitwise_not(imagem)
cv2.imshow("Imagem invertida", imgI)
cv2.imwrite("FluorescentCells_invertida.jpg", imgI)
cv2.waitKey(0)
cv2.destroyAllWindows()