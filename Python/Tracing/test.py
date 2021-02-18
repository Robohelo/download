# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:46:59 2021

@author: Roboadmin
"""

from multiprocessing.pool import ThreadPool
import os
from PIL import Image
import numpy as np


def open_image(imageList):
    data = []
    for image in imageList:
        with open(image, 'rb') as i:
            img = Image.open(i)
            img = img.resize((128, 128), Image.LANCZOS)
            img = img.convert("RGB")
            img = np.asarray(img)
            data.append(np.asarray(img))
    return data


def open_images(filename):
    dirList = os.listdir(filename)
    data = []
    pool = ThreadPool()
    for dirName in dirList:
        dirName = os.path.join(filename, dirName)
        try:
            imageList = os.listdir(dirName)
        except NotADirectoryError:
            print("File: \"" + str(dirName) + "\" is no dir")
        imageList = np.char.add(dirName+"/", imageList)
        async_result = pool.apply_async(open_image, imageList)
        break
    data = (async_result.get())
    return np.asarray(data)


PATH = "F:/Matura/Pictures_128/thumbnails128x128"
open_images(PATH)
