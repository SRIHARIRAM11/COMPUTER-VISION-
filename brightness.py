import cv2 
img=cv2.imread("man.jpg")
brightness=50

new=cv2.add(img,brightness)
cv2.imshow("original",img)
cv2.imshow("new image",new)
cv2.waitkey(0)
cv2.destroyallwindows()

