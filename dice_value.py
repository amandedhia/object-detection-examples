import cv2
import numpy as np

def dicevalue(img_og):
  #RESIZE THE IMAGE
  max_dim = max(img_og.shape)
  scale = 700/max_dim
  img_og = cv2.resize(img_og, None, fx=scale, fy=scale)
  
  #SMOOTH AND THE IMAGE AND CONVERT TO GRAYSCALE
  img = cv2.GaussianBlur(img_og, (15,15), 0)  #Adjust the kernel value to make sure the dice value match based on the lighting condition of dice photos
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  #THRESHOLDING AND MORPHOLOGY
  ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
  kernel = np.ones((7,7), np.uint8)
  thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
  thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
  
  #CONTOURING AND APPROXIMATION
  contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  value = 0
  cv2.drawContours(img_og, contours, -1, (0,0,255), 2, cv2.FILLED)
  #cv2.imshow(img_og) # display the dice with contours
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  for i in hierarchy:
    for j in i:
      if(j[2] == -1 and j[3] != -1):
        value = value + 1
  return value

dice = cv2.imread('many_dice.jpg', 1) #Upload dice image
value = dicevalue(dice)
print("The dice rolled to: ", value)
