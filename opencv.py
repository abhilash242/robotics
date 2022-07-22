import cv2
from matplotlib import pyplot as plt
# create figure
fig = plt.figure(figsize=(10, 7))

# reading image
img = cv2.imread('shapes.jpeg')
im1=img
# converting image into grayscale image

print('Enter your Shape:')
x = input()
print('Hello you entered , ' + x)
shapename=x
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
_, threshold = cv2.threshold(gray, 200, 200, cv2.THRESH_BINARY)

####################################################
imgContour = im1.copy()

imgGray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur,50,50)

##########################################################

# using a findContours() function
contours, _ = cv2.findContours(
	threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# list for storing names of shapes
for contour in contours:
  
    # here we are ignoring first counter because 
    # findcontour function detects whole image as shape
    if i == 0:
        i = 1
        continue
  
    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
     # finding center point of shape
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
  
    # putting shape name at center of each shape
    
    
    if (len(approx) == 3):

    # using drawContours() function
      cv2.drawContours(img, [contour], 0, (0, 0, 0), 2)
      
    elif len(approx) == 4:
       cv2.drawContours(img, [contour], 0, (0, 0, 255), 2)
  
    elif len(approx) == 5:
       cv2.drawContours(img, [contour], 0, (0, 0, 255), 2)
  
    elif len(approx) == 4:
       cv2.drawContours(img, [contour], 0, (0, 0, 255), 2)
  
    else:
       cv2.drawContours(img, [contour], 0, (0, 0, 255), 2)
     
     
     
     
     

        
###############################################3

cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# setting values to rows and column variables
rows = 3
columns = 3