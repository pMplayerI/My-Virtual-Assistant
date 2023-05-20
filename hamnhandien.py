import cv2
import hamdatabase
import os
def nhandien():
    faceDetect=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0)
    rec=cv2.face.LBPHFaceRecognizer_create()
    id=0
    path='recognizer'
    #get the path of all the files in the folder
    trainPaths=[os.path.join(path,f) for f in os.listdir(path)] 
    bienlap = True
    while(bienlap==True):
        for i in trainPaths:
            rec.read(i)
            #camera read
            ret,img=cam.read()
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=faceDetect.detectMultiScale(gray,1.3,5);
            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                id,conf=rec.predict(gray[y:y+h,x:x+w])
                id = int(id)
                profile=hamdatabase.getdatabase(id)
                #set text to window
                if(profile!=None):
                    print("nhan dien thanh cong : ")
                    print(profile)
                    bienlap = False
                    return profile
            if cv2.waitKey(1)==ord('q'):
                break
        