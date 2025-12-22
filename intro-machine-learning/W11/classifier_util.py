from sklearn.svm import SVC, LinearSVC

class RandomClassifier:
    def __init__(self, random_state=1, C=0.1):
        self.classifier1 = LinearSVC(random_state=random_state, C=C)

    def fit(self, X, y):
        self.classifier1.fit(X, y)
        return None

    def predict(self, X):
        return self.classifier1.predict(X)



class RandomClassifier2:
    def __init__(self, **kwargs):
        self.classifier2 = SVC(**kwargs)

    def fit(self, X, y):
        self.classifier2.fit(X, y)
        return None   # suppress Jupyter fold-out box

    def predict(self, X):
        return self.classifier2.predict(X)

    def decision_function(self, X):
        return self.classifier2.decision_function(X)

