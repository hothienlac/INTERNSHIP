import tensorflow as tf
physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)


from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense, BatchNormalization, Activation, Dropout
from tensorflow.keras import Model
from tensorflow.keras.models import load_model


MODEL_PATH = './model'
ACTIVATION_FUNCTION = 'relu'
DROPOUT_RATIO = 0.1


def block(x, units):
    x = Dense(units)(x)
    x = BatchNormalization()(x)
    x = Activation(ACTIVATION_FUNCTION)(x)
    x = Dropout(DROPOUT_RATIO)(x)
    return x 


def get_model():
    input = Input(shape=(20,))
    x = block(input, 128)
    x = block(x, 64)
    x = Dense(3)(x)
    output = Activation('softmax')(x)

    model = Model(inputs=input, outputs=output)
    return model



class PostureEstimator:

    def __init__(self, new_model=False):
        if new_model:
            self.__create_new_model__()
        else:
            self.__load_model__()
    

    def __create_new_model__(self):
        self.model = get_model()
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    

    def __load_model__(self):
        self.model = load_model(MODEL_PATH)

    
    def save_model(self):
        self.model.save(MODEL_PATH)


    def fit(self, X_train, y_train, epochs=500, batch_size=1024):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
    

    def evaluate_model(self, X_test, y_test):
        self.model.evaluate(X_test, y_test)

    
    def predict(self, data):
        return self.model.predict(data)
