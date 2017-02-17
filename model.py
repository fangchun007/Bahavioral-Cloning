import csv
import cv2
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

######### Data collecting and tidying #########

samples = []

with open('./data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for line in reader:
        image_dir = line[0]
        steering_angle = float(line[3])
        samples.append([image_dir,steering_angle])
train_samples, validation_samples = train_test_split(samples, test_size=0.2)

#### Data Preprocess and Generator ####

def crop_image(image):
    return image[60:140,:,:]

def generator(samples, batch_size=64):
    num_samples = len(samples)
    while 1: # Loop forever so the generator never terminates
        shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]

            images = []
            angles = []
            for batch_sample in batch_samples:
                name = './data/' + batch_sample[0]
                center_image = cv2.imread(name)
                center_image = crop_image(center_image)
                center_angle = batch_sample[1]
                images.append(center_image)
                angles.append(center_angle)

            X_train = np.array(images)
            y_train = np.array(angles)
            yield shuffle(X_train, y_train)

# compile and train the model using the generator function
train_generator = generator(train_samples, batch_size=64)
validation_generator = generator(validation_samples, batch_size=64)

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
#model.add(Dropout(drop_prob))
#model.add(Dense(512,activation='relu'))
#model.add(Dropout(drop_prob))
model.add(Dense(128,activation='relu'))
model.add(Dense(1))

#### Train Model ####
model.compile(loss='mse', optimizer='adam')
model.fit_generator(train_generator, samples_per_epoch= len(train_samples), 
                    validation_data=validation_generator, nb_val_samples=len(validation_samples), 
                    nb_epoch=3)

#### Save Model ####
model_json = model.to_json()
with open("model.json", "w", encoding="utf-8") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Saved model to disk")
