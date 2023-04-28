import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
from sklearn import metrics



class KMeansOnDigits:

    def __init__(self,n_clusters,random_state) -> None:
        self.n_clusters = n_clusters
        self.random_state = random_state
        
    def load_digits(self):
        from sklearn.datasets import load_digits
        self.digits = load_digits()

    def predict(self):
        kmeans = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
        clusters = kmeans.fit_predict(self.digits.data)
        self.clusters = clusters
    
    def get_labels(self):
        result = np.zeros_like(self.clusters)
        for cluster in np.unique(self.clusters):
            mask = (self.clusters == cluster)
            subarr_labels = self.digits.target[mask]
            mode_label = np.bincount(subarr_labels).argmax()
            result[mask] = mode_label
            
        self.labels = result
    
    def calc_accuracy(self) -> float:
        self.accuracy = round(accuracy_score(self.digits,self.labels), 2)
    
    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)
