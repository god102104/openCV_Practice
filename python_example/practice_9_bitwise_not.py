import cv2

src = cv2.imread("Image/lena.jpg", cv2.IMREAD_COLOR)
dst = cv2.bitwise_not(src)
rect = cv2.rectangle(src,(10,10),(100,100),(255,0,0),3)
print("dst = cv2.bitwise_not(src) or dst = ~src ")

cv2.imshow("Rect",rect)
#cv2.imshow("src", src)
#cv2.imshow("dst", dst)
#cv2.imshow("~src", ~src)
cv2.imshow("~src with rect",~rect)

cv2.waitKey()
cv2.destroyAllWindows()