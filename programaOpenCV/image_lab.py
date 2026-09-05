import cv2

imagem = cv2.imread("FluorescentCells.jpg")
cv2.imshow("Imagem original", imagem)

#Separando os canais da imagem LAB
#L = luminosidade, A = verde/vermelho, B = azul/amarelo
imagem_lab = cv2.cvtColor(imagem, cv2.COLOR_BGR2LAB)
cv2.imshow("Imagem LAB", imagem_lab)

L, A, B = cv2.split(imagem_lab)
cv2.imshow("Canal L - Luminosidade", L)
cv2.imshow("Canal A - Verde/Vermelho", A)
cv2.imshow("Canal B - Azul/Amarelo", B)

cv2.waitKey(0)
cv2.destroyAllWindows()