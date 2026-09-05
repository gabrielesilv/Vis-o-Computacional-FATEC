import cv2

imagem = cv2.imread("baboon.jpg")

#Separa os canais B, G e R
blue, green, red = cv2.split(imagem)

#Junta novamente os canais
imagemRGB = cv2.merge((blue, green, red))

#Exibe a imagem com os canais unidos
cv2.imshow("Imagem com juncao dos canais", imagemRGB)

#Exibe cada canal separadamente - BGR
cv2.imshow("Canal Blue", blue)
cv2.imshow("Canal Green", green)
cv2.imshow("Canal Red", red)

cv2.waitKey(0)
cv2.destroyAllWindows()