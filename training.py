import numpy as np
import cv2
import os
import face_recognizer as fr
dir='E:\\face_identification\\Data'
faces,faceID=fr.labels_for_training(dir)    
face_train=fr.training_imgs(faces,faceID)
face_train.save('E:\\face_identification\\trained_model.yml')