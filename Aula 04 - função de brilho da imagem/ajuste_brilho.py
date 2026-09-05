import cv2

img = cv2.imread("baboon.jpg")

img_brilho = cv2.convertScaleAbs(img, alpha=1.0, beta=70)

cv2.imshow("Original", img)
cv2.imshow("Mais clara", img_brilho)

cv2.waitKey(0)
cv2.destroyAllWindows()