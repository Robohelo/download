# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:14:08 2021

@author: Roboadmin
"""
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


config = tf.ConfigProto()
config.gpu_options.allow_growth = True

PATH = "F:/Matura/Pictures_128/thumbnails128x128"
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
    for image in imageList:
        with open(image, 'rb') as i:
            img = Image.open(i)
            img = img.resize((128, 128), Image.LANCZOS)
            img = img.convert("RGB")
            img = np.asarray(img)
            data.append(img)
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
                data.append(data_img)
    return np.asarray(np.asarray(data).reshape(-1, 128, 128, 3))


X_train_p = open_images(PATH)
y_train_p = np.ones(len(X_train_p), dtype=bool)
X_train_n = open_images(PATH_N)
y_train_n = np.zeros(len(X_train_n), dtype=bool)


print(X_train_p.shape)
print(X_train_n.shape)
print(y_train_p.shape)
print(y_train_n.shape)


X_train, y_train = shuffle(np.append(
    X_train_n, X_train_p, axis=0), np.append(y_train_n, y_train_p, axis=0))

X_train_p = None
y_train_p = None
X_train_n = None
y_train_n = None

X_train, X_test, y_train, y_test = train_test_split(
    X_train, y_train, test_size=0.33, random_state=42)

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


model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(
    128, 128, 3), activation="relu", padding="same"))
model.add(Conv2D(32, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(Conv2D(64, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(Conv2D(128, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dense(128, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(optimizer="rmsprop", loss="binary_crossentropy",
              metrics=["accuracy"])

model.summary()

model.fit(X_train, y_train, batch_size=128, epochs=10, shuffle=True)

print(model.evaluate(X_test, y_test))

model.save("facedetect.h5")

# import matplotlib.pyplot as plt

# plt.imshow(X_train[5], cmap="gray_r")
# plt.show()
