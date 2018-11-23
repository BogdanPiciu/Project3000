# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:40:48 2018

@author: Bogdan
"""

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
import sys
import numpy as np


#faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')





#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

video_capture = cv2.VideoCapture(0)
vs = VideoStream(src=1).start()
time.sleep(1.0)










while(True):
    
    
    
    
    
    frame = vs.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   

    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    
    
    
    #cv2.imshow("gray", gray)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#vs.release()
vs.stop()
cv2.destroyAllWindows()