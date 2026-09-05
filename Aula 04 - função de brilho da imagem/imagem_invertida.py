import cv2

imagem = cv2.imread("baboon.jpg")
cv2.imshow("Imagem", imagem)
imgI = cv2.bitwise_not(imagem)
cv2.imshow("imagem invertiva", imgI)
cv2.waitKey(0)
cv2.destroyALLWindows()