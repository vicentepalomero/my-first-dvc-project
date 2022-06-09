import pandas as pd
from typing import Dict, Text
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score, make_scorer


class UnsupportedClassifier(Exception):
    
    def __init__(self, estimator_name):

        self.msg = f'Unsupported estimator {estimator_name}'
        super().__init__(self.msg)


def get_supported_estimator() -> Dict:

    return {
        'logreg': LogisticRegression,
        'svm': SVC,
        'knn': KNeighborsClassifier
    }


def train(df: pd.DataFrame, target_column: Text,
          estimator_name: Text, param_grid: Dict, cv: int):

    estimators = get_supported_estimator()

    if estimator_name not in estimators.keys():
        raise UnsupportedClassifier(estimator_name)

    estimator = estimators[estimator_name]()
    f1_scorer = make_scorer(f1_score, average='weighted')
    clf = GridSearchCV(estimator=estimator,
                       param_grid=param_grid,
                       cv=cv,
                       verbose=1,
                       scoring=f1_scorer)
    y_train = df.loc[:, target_column].values.astype('int32')
    X_train = df.drop(target_column, axis=1).values.astype('float32')
    clf.fit(X_train, y_train)

    return clf
