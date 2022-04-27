

import numpy as np
import cv2




def box(a,b,c,d):
    cv2.rectangle(imag,(a,b),(a+c,b+d),(0,255,0),2)

def var_iter(l):
    l=l+1
    return(l)


n=140

face_casc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vid = cv2.VideoCapture(0)
while (vid.isOpened()):
    ret,imag = vid.read()

    faces = face_casc.detectMultiScale(imag, 1.2, 5, minSize=(10,10),maxSize=(500,500))

    for (x,y,w,h) in faces:
        n=var_iter(n)
        box(x,y,w,h)
        save_image = imag[y:y+h, x:x+w]
        cv2.imwrite("face%d.png"%(n),save_image)
        print(n)

    cv2.imshow('image',imag)
    k=cv2.waitKey(10) 
    if k==27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
