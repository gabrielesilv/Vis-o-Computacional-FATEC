import cv2

imagem = cv2.imread("FluorescentCells.jpg")
cv2.imshow("Imagem lida", imagem)
blue, green, red = cv2.split(imagem)
cv2.imshow("Canal Blue", blue)
cv2.imshow("Canal Green", green)
cv2.imshow("Canal Red", red)
imagem_resultado = cv2.merge((blue, green, red))
cv2.imshow("Imagem resultado", imagem_resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()