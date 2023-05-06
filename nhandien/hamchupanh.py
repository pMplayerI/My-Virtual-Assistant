import cv2
import hamdatabase
import numpy
def chupanh():
    cam = cv2.VideoCapture(0)
    detector= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # bien so luong anh
    sampleNum=0
    # nhap ten va mat khau cua nguoi dung 
    ten=input("nhap ten: ")
    pas= input("nhap mat khau: ")
    hamdatabase.themnguoidung(ten,pas)
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 
            #gioi han anh
            sampleNum=sampleNum+1
            #luu vao folder
            print(cv2.imwrite("nhandien/dataSet/User."+ten+'.'+ str(sampleNum) + ".jpg",gray))
            # xem hinh anh camera luc nay
            # cv2.imshow('frame',img)
        # tg delay
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # dung khi du 20 anh
        elif sampleNum>20:
            break
    cam.release()
    cv2.destroyAllWindows()