# pylint: disable=E1101
# pylint: disable=W0105
# pylint: disable=C0325
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20, 2020

@author: Roboadmin
"""

import face_recognition
import os
import cv2
import numpy as np

known_faces = []
known_names = []


def init_knowen_faces(file="known_faces"):
    """
    
    Loads Known Faces from dir.

    :param file: Image file name or file object to load.
    
    :return: Returns a string with "finished" or a Errormassage.
    """
    for name in os.listdir(file):
        for filename in os.listdir(f"{file}/{name}"):
            image = face_recognition.load_image_file(f"{file}/{name}/{filename}", mode='RGB')
            encoding = face_recognition.face_encodings(image)
            if(not encoding):
                return "Error by reading Pictures of known faces"
            known_faces.append(encoding[0])
            known_names.append(name)
    return "finished"

def check_ID(image = None, unknown_faces="unknown_faces", tolerance = 0.55, model = "cnn"):
    """
    
    Looks for known faces and gives the name and postion as return.
    
    :param image: RGB array with the image (optional)
    :param tolerance: Precision of the model (lower => more accurate)
    :param unknown_faces: Dir of the picture to identify.
    :param mode: Model for processing the images (hog for CPU, cnn for GPU (CUDA)).
    
    :return: Position and Name of found faces.
    """
    if not known_faces:
        return "Error: Before you can check ID you must initialize knowen faces!"
    match = [[],[]]
    if image is None:
        for filename in os.listdir(unknown_faces):
            image = face_recognition.load_image_file(f"{unknown_faces}/{filename}")
            if(image == 0):
                return "Error by reading Pictures of unknown faces"
            locations = face_recognition.face_locations(image, model=model)
            encodings = face_recognition.face_encodings(image, locations)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            for face_encoding, face_location in zip(encodings,locations):
                results = face_recognition.compare_faces(known_faces, face_encoding, tolerance)
                if True in results:
                    match[0].append(known_names[results.index(True)])
                    match[1].append(face_location)
    else:
        locations = face_recognition.face_locations(image, model=model)
        encodings = face_recognition.face_encodings(image, locations)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        for face_encoding, face_location in zip(encodings,locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, tolerance)
            if True in results:
                match[0].append(known_names[results.index(True)])
                match[1].append(face_location)
    return match