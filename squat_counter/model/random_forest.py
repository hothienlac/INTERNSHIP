from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib



class RandomForest(RandomForestClassifier):

    def __init__(self):
        super().__init__(n_estimators = 100)


    def evaluate(self, X_test, y_test):
        y_pred    = self.predict(X_test)
        accuracy  = accuracy_score(y_test, y_pred)
        
        return accuracy


    def save(self, path):
        joblib.dump(self, path)


    @staticmethod
    def load(path):
        return joblib.load(path)
