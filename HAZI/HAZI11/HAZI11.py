import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets, layers, models
from tensorflow import keras

def cifar100_data():
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar100.load_data()
    
    train_images = train_images / 255.0
    test_images = test_images/ 255.0
    
    return train_images, train_labels, test_images, test_labels

def cifar100_model():
    model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(128, (3, 3), padding='same', activation='relu'),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(100, activation='softmax')
    ])
    return model


def model_compile(model):
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])
    
    return model

def model_fit(model, epochs, train_images, train_labels):
    return model.fit(train_images, train_labels,epochs)

def model_evaluate(model, test_images, test_labels):
    
    test_loss, test_acc = model.evaluate(test_images,  test_labels)

    return test_loss, test_acc

