from sklearn.ensemble import RandomForestClassifier
import joblib


MODEL_PATH = './random_forest.joblib'


class PostureEstimator:

    def __init__(self, new_model=False):
        if new_model:
            self.__create_new_model__()
        else:
            self.__load_model__()
    

    def __create_new_model__(self):
        self.model = RandomForestClassifier(n_estimators=200, criterion='entropy', random_state = 0)
    

    def __load_model__(self):
        self.model = joblib.load("./random_forest.joblib")


    def save_model(self):
        joblib.dump(self.model, MODEL_PATH)


    def fit(self, X_train, y_train, epochs=500, batch_size=1024):
        self.model.fit(X_train, y_train)
    

    def evaluate_model(self, X_test, y_test):
        print(self.model.score(X_test, y_test))

    
    def predict(self, data):
        return self.model.predict(data)