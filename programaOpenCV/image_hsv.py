import cv2

imagem = cv2.imread("FluorescentCells.jpg")

imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV) #Convertendo RGB em HSV

matiz, saturacao, valor = cv2.split(imagem_hsv) #Separando os canais da imagem HSV

cv2.imshow("Imagem original", imagem)
cv2.imshow("Imagem HSV", imagem_hsv)
cv2.imshow("Canal H", matiz)
cv2.imshow("Canal S", saturacao)
cv2.imshow("Canal V", valor)

cv2.imwrite("imhH.jpg", matiz)
cv2.imwrite("imhS.jpg", saturacao)
cv2.imwrite("imhV.jpg", valor)

cv2.waitKey(0)
cv2.destroyAllWindows()