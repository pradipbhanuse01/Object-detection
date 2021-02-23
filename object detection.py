import cv2
import numpy as np

def nothing(x):
    pass





#cv2.imshow("image",img)


cv2.namedWindow("track")
cv2.createTrackbar("LH", "track", 0, 255,nothing)
cv2.createTrackbar("LS", "track", 0, 255,nothing)
cv2.createTrackbar("LV", "track", 0, 255,nothing)

cv2.createTrackbar("HH", "track", 255, 255,nothing)
cv2.createTrackbar("HS", "track", 255, 255,nothing)
cv2.createTrackbar("HV", "track", 255, 255,nothing)


while True:
    img = cv2.imread("smarties.png")
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH","track")
    l_s = cv2.getTrackbarPos("LS","track")
    l_v = cv2.getTrackbarPos("LV","track")

    h_h = cv2.getTrackbarPos("HH","track")
    h_s = cv2.getTrackbarPos("HS","track")
    h_v = cv2.getTrackbarPos("HV","track")

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([h_h,h_s,h_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(img,img,mask=mask)

   # cv2.imshow("track",track)
    cv2.imshow("image", img)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    key = cv2.waitKey(1)
    if key == 27:
        cv2.destroyAllWindows()