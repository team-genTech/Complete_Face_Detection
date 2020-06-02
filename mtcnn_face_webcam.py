import numpy as np
import cv2
import matplotlib.pyplot as plt
from mtcnn.mtcnn import MTCNN
detector=MTCNN()
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    faces=detector.detect_faces(frame)
    #print(faces2)
    for face in faces:
        x,y,w,h=face['box']
        roi_head=frame[y:y+h,x:x+h]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 130, 255), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (10, 50)  
    fontScale = 1      
    color = (255, 0, 0)       
    thickness = 2       
    frame2= cv2.putText(frame, f"There is/are {len(faces)} face(s) in the picture", org, font,  
                       fontScale, color, thickness, cv2.LINE_AA) 
    cv2.imshow('Live Cam',frame2)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()