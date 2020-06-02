# Complete_Face_Detection
Face Detection using LBPH Face recognition
Just ignore the mtcnn_face_webcam.py file.We can open it just to check how face detection works.
Be sure to change the directory of the file to where you download.
For me I had all the files stored in 'E:\\face_identification\\'
'E:\\face_identification\\Data' is used to store the captured images.
### Just a note, I will be explaining as per my directory
# Be sure to create your face dataset at the beginning(I've deleted mine :p) 
## There are 4 main Files that we need here:
### >creating_data.py
  --This is used to collect pictures of our facial data.Once you run this file, enter your name and the webcam will open.
    Be sure to check the Directory path.Zuckerberg's Image  is stored in 'E:\\face_identification\\Data\\0'
    Hence the next images captured would be stored in 'E:\\face_identification\\Data\\1' and so on.
    
### >face_recognizer.py
  --This is used to detect the faces, generate labels from data and place the rectangle and text within the frame
  
### >training.py
  --This is used for the training purpose, and creating our saved model

### >main_calling.py
  --This is the main file which calls all the functions and starts our webcam to detect the faces.


HAPPY HACKING!!



