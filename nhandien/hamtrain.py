import cv2,os
import numpy as np
from PIL import Image

def getImagesAndLabels(path):
    path='nhandien/dataSet'
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faces=[]
    IDs=[]
    y = 0
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        #split to get ID of the image
        ID=str(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("text",faceNp)
        cv2.waitKey(10)
    faces = np.asarray(faces, np.uint8)
    IDs = np.asarray(IDs, np.int32)
    return np.array(IDs), faces

def train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path='nhandien/dataSet'
    Ids,facess=getImagesAndLabels(path)  
#trainning
    recognizer.train(facess,Ids)
    recognizer.save('nhandien/recognizer/trainningData.yml')

