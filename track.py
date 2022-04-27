import numpy as np
import cv2
import serial

ser = serial.Serial(port='COM5',baudrate=9600,timeout=1)

def servo_rotate(motornum, AngleServo):
    ser.write(chr(255))
    ser.write(chr(motornum))
    ser.write(chr(AngleServo))


def box(a,b,c,d):
    cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,0),2)

def var_iter(l):
    l=l+1
    return(l)

def write_image():
    save_image= img[y:y+h, x:x+w] 
    cv2.imwrite("hey%d.png"%(n),save_image)

def angular_rotate_servo(angle):
    #prov=90
    if angle>230:
        prov=2
        servo_rotate(1,prov)

    elif angle<195:
        prov=1
        servo_rotate(1,prov)



face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

videoCap = cv2.VideoCapture(0)

n=0

while (videoCap.isOpened()):
    ret,img = videoCap.read()
    #cv2.imshow('xyz',img)
    faces = face.detectMultiScale(img, 1.2, 5, minSize=(10,10),maxSize=(500,500))
    for (x,y,w,h) in faces:
        box(x,y,w,h)
        n=var_iter(n)

        angular_rotate_servo(x)

    cv2.imshow('image',img)

    k=cv2.waitKey(10)
    if k==27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
