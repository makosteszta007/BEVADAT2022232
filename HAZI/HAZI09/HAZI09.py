import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix


class KMeansOnDigits:
    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state

    def load_dataset(self):
        self.digits = load_digits()

    def predict(self):
        self.model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        self.clusters = self.model.fit_predict(self.digits.data)

  