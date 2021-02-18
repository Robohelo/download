# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:14:08 2021

@author: Roboadmin
"""
import os
import numpy as np
from tqdm import tqdm
from PIL import Image
import tensorflow as tf
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

config = tf.ConfigProto()
config.gpu_options.allow_growth = True

PATH = "F:/Matura/Pictures_1024/images1024x1024"
PATH_N ="F:/Matura/dogcat/train"

def open_images(filename):
    dirList = os.listdir(filename)
    data = []
    
    for dirName in dirList:
        dirName = os.path.join(filename, dirName)
        imageList = os.listdir(dirName)
        for image in tqdm(imageList):
            with open(os.path.join(dirName, image), 'rb') as i:
                img = Image.open(i)
                img = img.resize((1024,1024), Image.LANCZOS)
                img = img.convert("RGB")
                img = np.asarray(img)
                data.append(np.asarray(img))
            if len(data) > 999:
                return np.asarray(data)
    return np.asarray(data)


X_train_p = open_images(PATH)
y_train_p = np.ones(len(X_train_p), dtype=bool)
X_train_n = open_images(PATH_N)
y_train_n = np.zeros(len(X_train_n), dtype=bool)


print(X_train_p.shape)
print(X_train_n.shape)
print(y_train_p.shape)
print(y_train_n.shape)


X_train,y_train = shuffle(np.append(X_train_n,X_train_p, axis=0),np.append(y_train_n,y_train_p, axis=0))

X_train_p = None
y_train_p = None
X_train_n = None
y_train_n = None

X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.33, random_state=42)

config = tf.compat.v1.ConfigProto(gpu_options = 
                         tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8)
# device_count = {'GPU': 1}
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)

#y_test = open_labels("./data/fashion/t10k-labels-idx1-ubyte.gz")

#y_train = to_categorical(y_train)
#y_test = to_categorical(y_test)


from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(1024, 1024, 3), activation="relu", padding="same"))
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

model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

model.summary()

model.fit(X_train, y_train, batch_size=128, epochs=10, shuffle=True)

print(model.evaluate(X_test, y_test))
# import matplotlib.pyplot as plt

# plt.imshow(X_train[5], cmap="gray_r")
# plt.show()