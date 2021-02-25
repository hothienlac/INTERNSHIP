import pandas as pd
from sklearn.model_selection import train_test_split
# from tensorflow import one_hot

from posture_estimator.posture_estimator_random_forest import PostureEstimator

DATA_PATH = './data/combined/data.csv'


def main():
    data = pd.read_csv(DATA_PATH)

    features = list(data.columns.values)
    features.remove('position')

    X = data[features].values
    y = data['position'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # y_train = one_hot(y_train, 3)
    # y_test = one_hot(y_test, 3)

    pose_estimator = PostureEstimator(new_model=True)
    pose_estimator.fit(X_train, y_train)
    print('EVALUATE MODEL')
    pose_estimator.evaluate_model(X_test, y_test)

    pose_estimator.save_model()



if __name__ == '__main__':
    main()
