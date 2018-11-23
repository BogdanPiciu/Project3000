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

vs = VideoStream(src=1).start()
time.sleep(1.0)
while(True):
    frame = vs.read()
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#vs.release()
vs.stop()
cv2.destroyAllWindows()