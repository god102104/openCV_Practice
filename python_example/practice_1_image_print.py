import cv2

image = cv2.imread("Image/lena.jpg", cv2.IMREAD_ANYDEPTH )
cv2.imshow("Lena_the_girl", image)
cv2.waitKey()
cv2.destroyAllWindows()