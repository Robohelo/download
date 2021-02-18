# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:57:21 2021

@author: Roboadmin
"""

from PIL import Image
import numpy as np
import keras.models as models
import tensorflow as tf
import os
import matplotlib.pyplot as plt
import time


def thread_function(sdir):
    """
    Only for multithreading

    Parameters
    ----------
    sdir : TYPE
        Path.

    Returns
    -------
    data : TYPE
        Image array.

    """
    data = []
    imageList = os.listdir(sdir)
    imageList = np.char.add(sdir + "/", imageList)
    for image in imageList:
        with open(image, 'rb') as i:
            img = Image.open(i)
            #img = img.resize((128, 128), Image.LANCZOS)
            img = img.convert("RGB")
            img = np.asarray(img)
            data.append(img)
    return np.asarray(data, dtype=object)


class ftrack(object):
    def __init__(self, h5_dir=None):
        config = tf.compat.v1.ConfigProto()
        config.gpu_options.allow_growth = True
        if h5_dir is None:
            h5_dir = "facedetect.h5"
        self.h5 = models.load_model(h5_dir)

    def track(self, img, step: int = 20, boxes: list = None, threshold=0.5):
        if boxes is None:
            boxes = [1024]  # , 192, 256, 384, 512]

        imgwidth = img.shape[1]
        imgheight = img.shape[0]
        predict = []
        img = Image.fromarray(img)
        for box in boxes:
            for posy in range(box, imgheight, step):
                for posx in range(box, imgwidth, step):
                    predict.append(self.h5.predict(np.asarray(img.crop(
                        (posx-box, posy-box, posx, posy)).resize((128, 128), Image.BILINEAR)).reshape(1, 128, 128, 3)))
        return np.array(predict, dtype=np.float32).reshape(len(range(box, imgheight, step)), len(range(box, imgwidth, step)), 1)


if __name__ == "__main__":
    x = ftrack()
    imgs = thread_function("./img/")
    # for img in imgs:
    #     plt.imshow(img)
    #     plt.show()
    # for i in range(len(imgs)):
    #     print(imgs[i].shape
    start = time.time()
    erg = x.track(imgs[0])
    end = time.time()
    plt.imshow(erg*255, cmap="gray")
    print(end-start)
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
