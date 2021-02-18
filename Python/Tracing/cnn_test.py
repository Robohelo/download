# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 08:50:00 2021

@author: Roboohelo-PC
"""

import cv2
import gzip
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import to_categorical

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

try:
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Display the resulting frame
        cv2.imshow("frame",frame)
        cv2.waitKey(1) 
except KeyboardInterrupt:
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    print("Exited")
    pass 


