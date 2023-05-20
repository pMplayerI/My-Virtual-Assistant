import cv2
import hamdatabase
import numpy as np
import os
def chupanh(ten_):
    cam = cv2.VideoCapture(0)
    detector= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # bien so luong anh
    sampleNum=0
    # nhap ten va mat khau cua nguoi dung 
    ten=ten_
    id = hamdatabase.themnguoidung(ten)
    # tao folder
    folder_path = f'./dataSet/user{id}'
    os.mkdir(folder_path)
    while(True):
        ret,img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 
            #gioi han anh
            sampleNum=sampleNum+1
            #luu vao folder
            cv2.imwrite(f"dataSet/user{id}/User."+str(id)+'.'+ str(sampleNum) + ".jpg",gray)
            # xem hinh anh camera luc nay
        # dung khi du anh
        if sampleNum>10:
            break
    cam.release()
    cv2.destroyAllWindows()