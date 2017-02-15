import csv
import cv2
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
%matplotlib inline

######### Data collecting and tidying #########
samples_stable = []
samples_left   = []
samples_right  = []

# data_stable

with open('./data_stable/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        image_dir = line[0]
        steering_angle = float(line[3])
        if -0.05 < steering_angle < 0.05:
            samples_stable.append([0, image_dir, steering_angle])
        else:
            samples_stable.append([0, image_dir, steering_angle])
            samples_stable.append([1, image_dir, -steering_angle])

# data_right

with open('./data_right/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if 0.45 < float(line[3]) < 0.9:
            image_dir = line[0]
            steering_angle = float(line[3])
            samples_right.append([0, image_dir, steering_angle])
            samples_right.append([1, image_dir, -steering_angle])

# data_left

with open('./data_left/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if -0.9 < float(line[3]) < -0.45:
            image_dir = line[0]
            steering_angle = float(line[3])
            samples_left.append([0, image_dir, steering_angle])
            samples_left.append([1, image_dir, -steering_angle])
            
samples_stable.extend(samples_left)
samples_stable.extend(samples_right)

# data collecting
samples = samples_stable
train_samples, validation_samples = train_test_split(samples, test_size=0.2)

#### Data Preprocess and Generator ####

def crop_image(image):
    return image[60:140,:,:]

def generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1: # Loop forever so the generator never terminates
        shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]

            images = []
            angles = []
            for batch_sample in batch_samples:
                name = batch_sample[1]
                if batch_sample[0]:
                    center_image = cv2.flip(cv2.imread(name), 1)
                else:
                    center_image = cv2.imread(name)
                # trim image to only see section with road
                center_image = crop_image(center_image)
                center_angle = batch_sample[2]
                images.append(center_image)
                angles.append(center_angle)

            X_train = np.array(images)
            y_train = np.array(angles)
            yield shuffle(X_train, y_train)

# compile and train the model using the generator function
train_generator = generator(train_samples, batch_size=32)
validation_generator = generator(validation_samples, batch_size=32)

#### Model Achitecture ####
from keras.models import Sequential, Model
from keras.layers import Lambda, Flatten, Dense, Dropout
from keras.layers.convolutional import Convolution2D
import tensorflow as tf

def resize_image(image, new_size=(66, 200)):
    return tf.image.resize_images(image, size=new_size, method=3, align_corners=False)

drop_prob = 0.5

model = Sequential()
# Preprocess incoming data, resize image to fit navidia architecture
model.add(Lambda(resize_image, input_shape=(80,320,3), output_shape=(66,200,3)))
# Preprocess incoming data, centered around zero with small standard deviation 
model.add(Lambda(lambda x: x/127.5 - 1.))
model.add(Convolution2D(24,5,5,subsample=(2,2),activation='relu'))
model.add(Convolution2D(36,5,5,subsample=(2,2),activation='relu'))
model.add(Convolution2D(48,5,5,subsample=(2,2),activation='relu'))
model.add(Convolution2D(64,3,3,activation='relu'))
model.add(Convolution2D(64,3,3,activation='relu'))
model.add(Flatten())
model.add(Dropout(drop_prob))
model.add(Dense(512,activation='relu'))
model.add(Dropout(drop_prob))
model.add(Dense(128,activation='relu'))
model.add(Dense(1))

#### Train Model ####
model.compile(loss='mse', optimizer='adam')
model.fit_generator(train_generator, samples_per_epoch= len(train_samples), 
                    validation_data=validation_generator, nb_val_samples=len(validation_samples), 
                    nb_epoch=4)

#### Save Model ####
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Saved model to disk")
