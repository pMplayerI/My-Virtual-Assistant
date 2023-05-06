import cv2
import numpy as np
from PIL import Image
import pickle
import sqlite3
import hamdatabase
def nhandien():
    faceDetect=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0);
    rec=cv2.face.LBPHFaceRecognizer_create();
    rec.read("nhandien/recognizer/trainningData.yml")
    id=0
    #set text style
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    fontscale = 1
    fontcolor = (203,23,252)

    while(True):
        #camera read
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5);
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            profile=hamdatabase.getdatabase(id)
            #set text to window
            if(profile!=None):
                print("nhan dien thanh cong : \n")
                print(profile)
        if cv2.waitKey(1)==ord('q'):
            break;
    cam.release()
    cv2.destroyAllWindows()