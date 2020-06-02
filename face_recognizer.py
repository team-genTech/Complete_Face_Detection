import numpy as np
import cv2
import os
from mtcnn.mtcnn import MTCNN


def faceDetection(test_img):
    detector=MTCNN()
    gray=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    faces=detector.detect_faces(test_img)
    return faces,gray


def labels_for_training(directory):              #directory=E:\face_identification\Data
    faces=[]
    faceID=[]
    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            id=os.path.basename(path)
            img_path=os.path.join(path,filename)
            print(img_path,id)
            test_img=cv2.imread(img_path)
            if test_img is None:
                continue

            face,gray_img=faceDetection(test_img)
            if len(face)!=1:
                continue
            for fac in face:
                (x,y,w,h)=fac['box']
                roi_gray=gray_img[y:y+h,x:x+h]
                faces.append(roi_gray)
                faceID.append(int(id))
                
    return faces,faceID                   #returns cropped faces and ids in the 2 lists

def training_imgs(faces_got,fID):
    face_recog=cv2.face.LBPHFaceRecognizer_create()
    face_recog.train(faces_got,np.array(fID))
    return face_recog

def draw_rect(test_img,face):                                         
    (x,y,w,h)=face['box']
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,120,250),thickness=2)

def put_text(test_img,text,x,y): 
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (x, y)  
    fontScale = 1      
    color = (255, 130, 0)       
    thickness = 2                                   
    cv2.putText(test_img,text, org, font,fontScale, color, thickness, cv2.LINE_AA) 
            
                
            
            
            
            


