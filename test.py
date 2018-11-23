# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:50:39 2018

@author: Bogdan
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
  #  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(frame, (7, 7), 0)
    # Display the resulting frame
    cv2.imshow('frame',blurred)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()