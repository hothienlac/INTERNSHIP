import numpy as np
import joblib
from sklearn.metrics import accuracy_score



class GaussianNaiveBayes:

    def fit(self, X, y):
        number_of_samples = len(y)

        self.classes, counts    = np.unique(y, return_counts=True)
        self.prior_prob         = dict(zip(self.classes, counts / number_of_samples))

        self.means = {}
        self.stds  = {}

        for c in self.classes:
            idx = np.argwhere(y == c)
            x_with_class_c  = X[idx, :]
            self.means[c]   = np.mean(x_with_class_c, axis=0).flatten()
            self.stds[c]    = np.std(x_with_class_c, axis=0).flatten()


    def predict(self, X):
        result = []
        for raw in X:
            class_probs = self.__compute_classes_prob(raw)
            c = max(class_probs, key=class_probs.get)
            result.append(c)
        return result
    

    def evaluate(self, X_test, y_test):
        y_pred    = self.predict(X_test)
        accuracy  = accuracy_score(y_test, y_pred)
        
        return accuracy
    

    def save(self, path):
        joblib.dump(self, path)


    @staticmethod
    def load(path):
        return joblib.load(path)


    @staticmethod
    def __norm_pdf(x, mean, std):
        exp = np.exp(-((x-mean)**2/(2* std**2)))
        return (1/(std * np.sqrt(2 * np.pi))) * exp


    def __compute_classes_prob(self, x):
        classes_prob = {}
        for c in self.classes:
            classes_prob[c] = self.prior_prob[c]
            for i, v in enumerate(x):
                classes_prob[c] *= GaussianNaiveBayes.__norm_pdf(v, self.means[c][i],self.stds[c][i])
        return classes_prob
