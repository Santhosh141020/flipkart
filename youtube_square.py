import cv2
import numpy as np


def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        print(len(cnt))
        cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
    print(len(contours))

img = cv2.imread('arena_pic.jpg')
img = cv2.resize(img, (400, 200))
imgContour = img.copy()
img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_gry, (7, 7), 1)

# threshold1 = cv2.getTrackbarPos('thersh1', 'parameters')
# threshold2 = cv2.getTrackbarPos('thersh2', 'parameters')
img_cny = cv2.Canny(img_blur, 150, 25)

kernel = np.ones((5,5))

imgDil = cv2.dilate(img_cny, kernel, iterations=1)
#print(imgDil[0])
getContours(imgDil, imgContour)


conc = np.concatenate((img_gry, img_blur), axis=1)
conc1 = np.concatenate((img_cny, imgDil), axis=1)
finalImg = np.concatenate((conc, conc1), axis=0)
cv2.imshow('Counters', imgContour)
cv2.imshow('wait', finalImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
