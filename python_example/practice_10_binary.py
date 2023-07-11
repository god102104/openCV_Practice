import cv2

src = cv2.imread("Image/lena.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
print("With cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) function, we can make image to binay image")
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()