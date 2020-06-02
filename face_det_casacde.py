import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier(r'C:\Users\imswa\.spyder-py3\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 10)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 130, 255), 2)
        roi_face=frame[y:y+h,x:x+w]
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (10, 50)  
    fontScale = 1      
    color = (255, 0, 0)       
    thickness = 2       
    frame2 = cv2.putText(frame, f"There is/are {len(faces)} face(s) in the cam", org, font,  
                       fontScale, color, thickness, cv2.LINE_AA) 
    
    cv2.imshow('Picture',frame2)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()