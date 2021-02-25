'''

import tensorflow as tf
from sklearn.metrics import accuracy_score
import numpy as np

from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense, BatchNormalization, Activation, Dropout
from tensorflow.keras import Model
from tensorflow.keras.models import load_model
from tensorflow import one_hot



class DeepNeuralNetwork:

    ACTIVATION_FUNCTION = 'relu'
    DROPOUT_RATIO = 0.1


    def __init__(self, model=None):
        if model:
            self.model = model
            return

        physical_devices = tf.config.list_physical_devices('GPU') 
        tf.config.experimental.set_memory_growth(physical_devices[0], True)

        input = Input(shape=(22,))
        x = self.block(input, 256)
        x = self.block(input, 256)
        x = self.block(x, 64)
        x = Dense(3)(x)
        output = Activation('softmax')(x)

        self.model = Model(inputs=input, outputs=output)
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


    def block(self, x, units):
        x = Dense(units)(x)
        x = BatchNormalization()(x)
        x = Activation(self.ACTIVATION_FUNCTION)(x)
        x = Dropout(self.DROPOUT_RATIO)(x)
        return x


    def fit(self, X_train, y_train, epochs=500, batch_size=1024):
        y_train = one_hot(y_train, 3)
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=0)


    def predict(self, data):
        return np.argmax(self.model.predict(data, verbose=0), axis=1)


    def evaluate(self, X_test, y_test):
        y_pred    = self.predict(X_test)
        accuracy  = accuracy_score(y_test, y_pred)
        
        return accuracy


    def save(self, path):
        self.model.save(path+'.h5')
    

    @staticmethod
    def load(path):
        model = load_model(path+'.h5')
        return DeepNeuralNetwork(model)

'''
