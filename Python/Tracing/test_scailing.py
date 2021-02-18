# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:14:08 2021

@author: Roboadmin
"""
import matplotlib.pyplot as plt
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.models import Sequential
import os
import numpy as np
from tqdm import tqdm
from PIL import Image
import tensorflow as tf
from sklearn.utils import shuffle
import concurrent.futures
from sklearn.model_selection import train_test_split
import cv2
import gc

config = tf.ConfigProto()
config.gpu_options.allow_growth = True

PATH = "F:/Matura/Pictures_128/thumbnails128x128"
PATH_H = "F:/Matura/Pictures_1024/images1024x1024"
PATH_N = "F:/Matura/dogcat/train"
# PATH_DOG ="F:/Matura/dogcat/train/dogs"


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
    # print("start")
    imageList = os.listdir(sdir)
    imageList = np.char.add(sdir + "/", imageList)
    x = 0
    for image in imageList:
        x = x+1
        with open(image, 'rb') as i:
            img = Image.open(i)
            #img = img.resize((128, 128), Image.LANCZOS)
            img = img.convert("RGB")
            img = np.asarray(img, dtype=np.float16)
            img = img / 255
            data.append(img)
        if x >= 10:
            break
    return data


def open_images(filename):
    """
    Readfunction for images (Multithreaded)

    Parameters
    ----------
    filename : TYPE
        Path to Pictures (one layer aboth).

    Returns
    -------
    TYPE
        Numpy array with the pictures in shape -1,128,128,3.

    """
    data = []
    dirList = os.listdir(filename)
    dirList = np.char.add(filename + "/", dirList)
    for sdir, it in zip(dirList, range(dirList.shape[0])):
        if not(os.path.isdir(sdir)):
            dirList = np.delete(dirList, it, axis=0)

    with concurrent.futures.ThreadPoolExecutor(max_workers=120) as executor:
        # Start the load operations and mark each future with its URL
        future_to_img = {executor.submit(
            thread_function, sdir): sdir for sdir in dirList}
        for future in tqdm(concurrent.futures.as_completed(future_to_img)):
            img = future_to_img[future]
            try:
                data_img = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (img, exc))
            else:
                data.append(data_img[0][:][:][:])
            break
        return np.asarray(data)


X_train = open_images(PATH)
gc.collect()

imgs = open_images(PATH_H)
gc.collect()

config = tf.compat.v1.ConfigProto(gpu_options=tf.compat.v1.GPUOptions(
    per_process_gpu_memory_fraction=0.8)
    # device_count = {'GPU': 1}
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)

#y_test = open_labels("./data/fashion/t10k-labels-idx1-ubyte.gz")

#y_train = to_categorical(y_train)
#y_test = to_categorical(y_test)


encoder = Sequential()
encoder.add(Conv2D(3, kernel_size=(3, 3), padding="same",
                   activation="relu", input_shape=(1024, 1024, 3)))
encoder.add(MaxPooling2D(pool_size=(2, 2)))
encoder.add(Conv2D(3, kernel_size=(3, 3), padding="same", activation="relu"))
encoder.add(MaxPooling2D(pool_size=(2, 2)))
encoder.add(Conv2D(3, kernel_size=(3, 3), padding="same", activation="relu"))
encoder.add(MaxPooling2D(pool_size=(2, 2)))

encoder.summary()
gc.collect()
encoder.compile(optimizer="rmsprop", loss="mse")

encoder.fit(imgs, X_train, batch_size=128, epochs=100, shuffle=True)

encoded = encoder.predict(imgs[0].reshape(-1, 1024, 1024, 3))

encoder.save("encoder.h5")

print(encoded.shape)
plt.imshow(np.asarray(encoded[0]*255, dtype=np.uint8))
plt.show()
Image.fromarray(np.asarray((imgs[0]*255), dtype=np.uint8)).show()

# plt.imshow(X_train[5], cmap="gray_r")
# plt.show()
