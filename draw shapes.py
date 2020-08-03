import cv2
import numpy as np

# to make a black image

img=np.zeros([512,512,3],np.uint8) #so this is the black image
#now lets make a line in this image

img=cv2.line(img,(255,255),(100,200),(255,0,0),5) # 2nd argument is point 1 and third argument is point 2 and 4th is the colour and 5th is the thickness
#now lets draw a arrowed line

img=cv2.arrowedLine(img,(200,200),(10,10),(255,0,0),5)# so this is the arrowed line
#now lets draw a rectangle in this image
img=cv2.rectangle(img,(255,255),(100,200),(0,0,255),5) #so this is the rectangle
#now a circle
img=cv2.circle(img, (150,150), 60,(0,255,0),2) # so this was the circle
#now let see how to put a text of image
font=cv2.FONT_HERSHEY_COMPLEX_SMALL #this is the font style
img=cv2.putText(img, 'yusuf',(100,255),font,1,(255,255,255),2) #this is how you can put text on the image

cv2.imshow("black",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
