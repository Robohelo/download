# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:33:00 2021

@author: Roboohelo-PC
"""
# The contents of this file are in the public domain. See LICENSE_FOR_EXAMPLE_PROGRAMS.txt
#
#   This example program shows how to find frontal human faces in an image.  In
#   particular, it shows how you can take a list of images from the command
#   line and display each on the screen with red boxes overlaid on each human
#   face.
#
#   The examples/faces folder contains some jpg images of people.  You can run
#   this program on them and see the detections by executing the
#   following command:
#       ./face_detector.py ../examples/faces/*.jpg
#
#   This face detector is made using the now classic Histogram of Oriented
#   Gradients (HOG) feature combined with a linear classifier, an image
#   pyramid, and sliding window detection scheme.  This type of object detector
#   is fairly general and capable of detecting many types of semi-rigid objects
#   in addition to human faces.  Therefore, if you are interested in making
#   your own object detectors then read the train_object_detector.py example
#   program.
#
#
# COMPILING/INSTALLING THE DLIB PYTHON INTERFACE
#   You can install dlib using the command:
#       pip install dlib
#
#   Alternatively, if you want to compile dlib yourself then go into the dlib
#   root folder and run:
#       python setup.py install
#
#   Compiling dlib should work on any operating system so long as you have
#   CMake installed.  On Ubuntu, this can be done easily by running the
#   command:
#       sudo apt-get install cmake
#
#   Also note that this example requires Numpy which can be installed
#   via the command:
#       pip install numpy

import sys
import os
import cvlib as cv
import numpy as np
import time
import cv2
from tqdm import tqdm

# detector = dlib.cnn_face_detection_model_v1("./mmod_human_face_detector.dat")

# detector = dlib.cnn_face_detection_model_v1("./facedetect.h5")

#sdir = "./img"
sdir = "F:/Matura/Pictures_128/thumbnails128x128/00000"
imageList = os.listdir(sdir)
imageList = np.char.add(sdir + "/", imageList)
meantime = []
meanconf = []
incorrect = len(imageList)
for f in tqdm(imageList):
    # print("Processing file: {}".format(f))
    img = cv2.imread(f)
    # The 1 in the second argument indicates that we should upsample the image
    # 1 time.  This will make everything bigger and allow us to detect more
    # faces.
    start = time.time()
    dets, confidences = cv.detect_face(img, enable_gpu=True)
    end = time.time()
    Time = end-start
    meantime.append(Time)
    meanconf.append(confidences)
    incorrect -= len(dets)
    # print("Number of faces detected: {}".format(len(dets)))
    # for i, d in enumerate(dets):
    #     print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Time: {}".format(
    #         i, d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom(), Time))

print("\nMeantime: ", end="")
print(np.mean(meantime))
print("False: ", end="")
print(incorrect)
print("Confidence: ", end="")
print(meanconf[0][0])
# Finally, if you really want to you can ask the detector to tell you the score
# for each detection.  The score is bigger for more confident detections.
# The third argument to run is an optional adjustment to the detection threshold,
# where a negative value will return more detections and a positive value fewer.
# Also, the idx tells you which of the face sub-detectors matched.  This can be
# used to broadly identify faces in different orientations.
# if (len(sys.argv[1:]) > 0):
#     img = dlib.load_rgb_image(sys.argv[1])
#     dets, scores, idx = detector.run(img, 1, -1)
#     for i, d in enumerate(dets):
#         print("Detection {}, score: {}, face_type:{}".format(
#             d, scores[i], idx[i]))
