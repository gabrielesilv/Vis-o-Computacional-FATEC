import cv2

img = cv2.imread("baboon.jpg")

img_brilho = cv2.convertScaleAbs(img, alpha=1.0, beta=70)

cv2.imshow("Original", img)
cv2.imshow("Mais clara", img_brilho)

cv2.waitKey(0)
cv2.destroyAllWindows()



# import cv2

# img = cv2.imread("imagem/baboon.jpg")

# if img is None:
#     print("ERRO: não foi possível carregar baboon.jpg")
#     exit()

# img_brilho = cv2.convertScaleAbs(img, alpha=1.0, beta=70)

# cv2.imshow("Original", img)
# cv2.imshow("Mais clara", img_brilho)

# cv2.waitKey(0)
# cv2.destroyAllWindows()