import numpy as np
import cv2
import os
import face_recognizer as fr
face_identify=cv2.face.LBPHFaceRecognizer_create()
face_identify.read('E:\\face_identification\\trained_model.yml')

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    faces_det,gray=fr.faceDetection(frame)
    for face in faces_det:
        x,y,w,h=face['box']
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
        roi_gray=gray[y:y+h,x:x+w]
        lab,conf=face_identify.predict(roi_gray)
        
        if conf<=118:
            for s in os.listdir(os.path.join('E:\\face_identification\\Data',str(lab))):
                label=s.split('_')[0]
                break              
        else:
            label='Unknown'
        
        fr.draw_rect(frame,face)
        font = cv2.FONT_HERSHEY_SIMPLEX 
        org = (x, y)  
        fontScale = 1      
        color = (255, 130, 0)       
        thickness = 2                                   
        frame = cv2.putText(frame,f'{label}', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("My Cam",frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()