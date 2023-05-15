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

# %%
'''
K�sz�ts egy met�dust, ami a bemeneti h�lot compile-olja.
Optimizer: Adam
Loss: SparseCategoricalCrossentropy(from_logits=False)

Egy p�lda a bemenetre: model
Egy p�lda a kimenetre: model
return type: keras.engine.sequential.Sequential
f�ggv�ny neve: model_compile
'''


# %%
def model_compile(model):
    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                metrics=['accuracy'])
    return model
# %%
'''
K�sz�ts egy met�dust, ami a bemeneti h�l�t feltan�tja.

Egy p�lda a bemenetre: model,epochs, train_images, train_labels
Egy p�lda a kimenetre: model
return type: keras.engine.sequential.Sequential
f�ggv�ny neve: model_fit
'''
def model_fit(model,epochs, train_images, train_labels):
    model.fit(train_images, train_labels, epochs=epochs)
    return model

# %%
'''
K�sz�ts egy met�dust, ami a bemeneti h�l�t ki�rt�keli a teszt adatokon.

Egy p�lda a bemenetre: model, test_images, test_labels
Egy p�lda a kimenetre: test_loss, test_acc
return type: float, float
f�ggv�ny neve: model_evaluate
'''
def model_evaluate(model, test_images, test_labels):
    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
    return (test_loss,test_acc)

