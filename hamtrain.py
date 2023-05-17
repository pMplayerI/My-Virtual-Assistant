import cv2,os
import numpy as np
from PIL import Image
import hamdatabase

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        #split to get ID of the image
        ID=str(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.waitKey(10)
    faces = np.asarray(faces, np.uint8)
    IDs = np.asarray(IDs, np.int32)
    return IDs,faces

def train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    id = hamdatabase.getcountdatabase()
    path= "D:\\My-Virtual-Assistant\\dataSet\\user" +str(id)
    Ids,facess=getImagesAndLabels(path)  
    #trainning
    recognizer.train(facess,Ids)
    recognizer.save("D:\\My-Virtual-Assistant\\recognizer\\trainningData" +str(Ids[0])+ ".yml")

