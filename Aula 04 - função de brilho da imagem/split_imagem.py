import cv2

imagem = cv2.imread("baboon.jpg")

#Separa os canais
blue, green, red = cv2.split(imagem)

#Mostra os canais separadamente
cv2.imshow("Canal Azul", blue)
cv2.imshow("Canal Verde", green)
cv2.imshow("Canal Vermelho", red)

#Junta novamente os canais
#imagem = cv2.merge((blue, green, red))

#Mostra a imagem resultante
cv2.imshow("imagem_Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()