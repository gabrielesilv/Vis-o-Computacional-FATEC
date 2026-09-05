import cv2

#imagem em tons de cinza
img = cv2.imread("baboon.jpg", 0)

#verificando se a imagem foi carregada
if img is None:
    print("Erro ao carregar a imagem!")
    exit()

#cópia da imagem
imgB = img.copy()

#percorrendo todos os pixels
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        imgB[x][y] = min(img[x][y] + 50, 255)  #limite do pixel é 255

#mostra as imagens
cv2.imshow("Imagem original", img)
cv2.imshow("Imagem alterada pra mais claridade", imgB)

#calcula o histograma da imagem original
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])

#calcula o histograma da imagem modificada
hist_clareada = cv2.calcHist([imgB], [0], None, [256], [0, 256])

cv2.waitKey(0)
cv2.destroyAllWindows()