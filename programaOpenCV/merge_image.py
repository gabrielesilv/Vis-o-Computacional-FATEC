import cv2

imagem = cv2.imread("FluorescentCells.jpg") #Separando os canais da imagem
blue, green, red = cv2.split(imagem) #Juntando novamente os canais
imagemRGB = cv2.merge((blue, green, red))
cv2.imshow("Imagem com juncao dos canais", imagemRGB)
cv2.imshow("Canal Blue", blue)
cv2.imshow("Canal Green", green)
cv2.imshow("Canal Red", red)
cv2.waitKey(0)
cv2.destroyAllWindows()