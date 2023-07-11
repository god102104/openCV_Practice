import cv2

src = cv2.imread("Image/lena.jpg", cv2.IMREAD_COLOR)


print("cv2.flip(src, 0)is x-axis_reflection")
print("cv2.flip(src, 1)is y-axis_reflection")
print("cv2.flip(src, -1)is zero_point_axis_reflection")

cv2.imshow("original", src)
cv2.imshow("x-axis_reflection", cv2.flip(src, 0))
cv2.imshow("y-axis_reflection", cv2.flip(src, 1))
cv2.imshow("zero_point_axis_reflection", cv2.flip(src, -1))
cv2.waitKey()
cv2.destroyAllWindows()
