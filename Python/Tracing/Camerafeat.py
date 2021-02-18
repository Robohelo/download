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

# Ringbuffer
class RingBuffer:
    def __init__(self, size):
        self.maxsize = size
        self.data = []
        self.size = 0

    def append(self, x):    
        self.data.append(x)
        if self.size < self.maxsize:
            self.size = self.size + 1
        else:
            self.data.pop(0)
            
    def get(self):
        if self.size > 0:
            self.size = self.size -1
            return self.data.pop(0)

    def get_buffer(self):
        return self.data

    def get_size(self):
        return self.size
    

#PC 0
#Laptop 2
cap = cv2.VideoCapture(2)
ret, frame = cap.read()
print(frame.shape)
R = RingBuffer(3)
try:
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Display the resulting frame
        # cv2.imshow("frame",frame)
        # cv2.waitKey(1)
        R.append(frame)
        movement = np.where(np.clip(frame-np.mean(R.get()),0,255)<60,0,1)
        
        if np.sum(movement)>100000:
            print("Movement, Sum: ",end="")
            print(np.sum(movement))
            # plt.imshow(np.clip(frame-last_frame,0,255))
            # plt.show()
            # plt.imshow(movement*255,)
            # plt.show()
        last_frame = frame
except KeyboardInterrupt:
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    print("Exited")
    pass 


