
import cv2
src = cv2.imread("myimage/1.jpg")
cv2.namedWindow("input image",cv2.WINDOW_AUTOSIZE)
cv2.imshow("input image",src)
cv2.waitKey(0)
cv2.destroyAllWindows()

