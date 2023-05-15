import tensorflow as tf
import numpy as np

'''
K�sz�ts egy met�dust ami a cifar100 adatb�zisb�l bet�lti a train �s test adatokat. (tf.keras.datasets.cifar100.load_data())
Majd a tanit�, �s tesztel� adatokat normaliz�lja, �s vissza is t�r vel�k.


Egy p�lda a kimenetre: train_images, train_labels, test_images, test_labels
f�ggv�ny neve: cifar100_data
'''



# %%
def cifar100_data():
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar100.load_data()
    return  (train_images/ 255.0, train_labels), (test_images/ 255.0, test_labels)
#(train_images, train_labels), (test_images, test_labels) =cifar100_data()
#train_images.shape

# %%
'''
K�sz�ts egy konvol�ci�s neur�lis h�l�t, ami k�pes felismerni a k�pen mi van a 100 oszt�ly k�z�l.
A h�l� kimenete legyen 100 elem�, �s a softmax aktiv�ci�s f�ggv�nyt haszn�lja.
H�lon bel�l tetsz�leges sz�m� r�teg lehet..


Egy p�lda a kimenetre: model,
return type: keras.engine.sequential.Sequential
f�ggv�ny neve: cifar100_model
'''


# %%
def cifar100_model():
    model =tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D((2, 2)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dense(100, activation='softmax'))
    return model
#m=cifar100_model()