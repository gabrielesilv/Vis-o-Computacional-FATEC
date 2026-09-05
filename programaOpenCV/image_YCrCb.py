import cv2

imagem = cv2.imread("FluorescentCells.jpg")
cv2.imshow("Imagem original", imagem)

#Separando os canais da imagem YCrCb
#Y = luminosidade/brilho, Cr = vermelho, Cb = azul
imagem_ycrcb = cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
cv2.imshow("Imagem YCrCb", imagem_ycrcb) 

Y, Cr, Cb = cv2.split(imagem_ycrcb)
cv2.imshow("Y - Luminosidade", Y)
cv2.imshow("Cr - Vermelho", Cr)
cv2.imshow("Cb - Azul", Cb)

cv2.waitKey(0)
cv2.destroyAllWindows()