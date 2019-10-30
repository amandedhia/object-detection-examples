import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX

def nothing(x):
    pass

cv2.namedWindow('hsv_value_adjuster')
#ADJUST THE FOLLOWING VALUE TO GET A SPECTRUM THAT DETECTS YOUR SAMPLE COLOUR BALL IN A GIVEN LIGHTING (I've adjusted it to detect red bsll in specific lighting condition)
cv2.createTrackbar('lh', 'hsv_value_adjuster', 167, 255, nothing)
cv2.createTrackbar('ls', 'hsv_value_adjuster', 127, 255, nothing)
cv2.createTrackbar('lv', 'hsv_value_adjuster', 0, 255, nothing)
cv2.createTrackbar('uh', 'hsv_value_adjuster', 180, 180, nothing)
cv2.createTrackbar('us', 'hsv_value_adjuster', 255, 255, nothing)
cv2.createTrackbar('uv', 'hsv_value_adjuster', 255, 255, nothing)

def wheresmyball(img):
    # RESIZING THE IMAGE
    max_dim = max(img.shape)
    scale = 700 / max_dim
    img = cv2.resize(img, None, fx=scale, fy=scale)

    # SMOOTHING THE IMAGE
    img_smooth = cv2.GaussianBlur(img, (41, 41), 0)
    img_hsv = cv2.cvtColor(img_smooth, cv2.COLOR_BGR2HSV)

    # DEFINE FILTER FOR RED BALL
    lh = cv2.getTrackbarPos('lh', 'hsv_value_adjuster')
    ls = cv2.getTrackbarPos('ls', 'hsv_value_adjuster')
    lv = cv2.getTrackbarPos('lv', 'hsv_value_adjuster')
    uh = cv2.getTrackbarPos('uh', 'hsv_value_adjuster')
    us = cv2.getTrackbarPos('us', 'hsv_value_adjuster')
    uv = cv2.getTrackbarPos('uv', 'hsv_value_adjuster')
    lr = np.array([lh, ls, lv])
    ur = np.array([uh, us, uv])
    mask = cv2.inRange(img_hsv, lr, ur)

    #APPLYING FILTER MASK
    result = cv2.bitwise_and(img, img, mask=mask)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    # IMAGE SEGMENTATION USING THRESHOLD 
    ret, thresh = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # MORPHOLOGICAL TRANSFORMATIONS
    kernel = np.ones((7, 7), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # CONTOURS AND STUFF RELATED TO IT
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    imgf = np.zeros(img.shape, np.uint8)

    # APPROXIMATE IT TO GET WELL DEFINED CONTOUR SHAPES AND DRAW THE CONTOUR
    for cntr in contours:
        apx = cv2.approxPolyDP(cntr, 0.01*cv2.arcLength(cntr, True), True)
        area = cv2.contourArea(apx)
        x = apx.ravel()[0]
        y = apx.ravel()[1]
        if 10 < len(apx) < 15 and area > 800:
            cv2.drawContours(img, [apx], -1, (0, 0, 0), 2, cv2.FILLED)
            cv2.putText(img, 'Red Ball', (x, y), font, 1, 0)

    #DISPLAYING EACH FRAME
    cv2.imshow('detect', img)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    wheresmyball(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
