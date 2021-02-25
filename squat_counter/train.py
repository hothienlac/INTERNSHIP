# from model.deep_neural_network import DeepNeuralNetwork
from model.gaussian_naive_bayes import GaussianNaiveBayes
from model.random_forest import RandomForest

import pandas as pd
from sklearn.model_selection import train_test_split



class Train:
    
    def __init__(self, args):
        self.data = pd.read_csv(args.data)
        self.data = self.data[self.data['score'] > 0.75]
        self.features = list(self.data.columns.values)
        self.features.remove('posture')
        self.features.remove('score')

        self.model = Train.get_model(args.model)
        self.model_output = args.model_output

        if not self.model_output:
            self.model_output = f'./model/{args.model}.model'


    def run(self):
        X = self.data[self.features].values
        y = self.data['posture'].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        print('Training...')
        self.model.fit(X_train, y_train)
        print('Training complete')

        print('Evaluating...')
        evaluate_score = self.model.evaluate(X_test, y_test)
        print(f'Model Accuracy: {evaluate_score}.')

        self.model.save(self.model_output)
        print('Model saved!')


    @staticmethod
    def get_model(model):
        model_dictionary = {
            # 'deep_neural_network': DeepNeuralNetwork,
            'gaussian_naive_bayes': GaussianNaiveBayes,
            'random_forest': RandomForest,
        }

        return model_dictionary[model]()
