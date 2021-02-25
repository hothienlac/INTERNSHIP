import numpy as np

class MyGaussianNB: 
    def fit(self, X, y):
        samples = len(y)  # <=> X.shape[0]
        self.classes, counts = np.unique(y, return_counts=True)
        self.prior_prob = dict(zip(self.classes, counts/samples))
        
        self.means = {}
        self.stds = {}
        
        for c in self.classes:
            idx = np.argwhere(y==c)  # return index of class c in y
            x_with_class_c = X[idx, :]
            self.means[c] = np.mean(x_with_class_c, axis=0).flatten()
            self.stds[c] = np.std(x_with_class_c, axis=0).flatten()
            
    def predict(self, X):
        result = []
        for raw in X:
            class_probs = self.__compute_class_probs(raw)
            c = max(class_probs, key=class_probs.get)
            result.append(c)
        return result
    
    def __norm_pdf(self, x, mean, std):
        exp = np.exp(-((x-mean)**2/(2* std**2)))
        return (1/(std * np.sqrt(2 * np.pi))) * exp
    
    
#     x is a vector
    def __compute_class_probs(self, x):
        p_of_class = {}
        for c in self.classes:
            p_of_class[c] = self.prior_prob[c]
            for i, v in enumerate(x):
                p_of_class[c] *= self.__norm_pdf(v, self.means[c][i],self.stds[c][i])
        return p_of_class