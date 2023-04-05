import pandas as pd
import seaborn as sns
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
import math

class KNNClassifier:
    @staticmethod
    def load_csv(csv_path:str) ->Tuple[pd.DataFrame,pd.Series]:
        dataset = pd.read_csv(csv_path)
        dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)
        x,y = dataset.iloc[:,:-1], dataset.iloc[:,-1]
        return x,y


    def __init__(self,k:int,test_split_ratio:float)->None:
        self.k = k
        self.test_split_ratio = test_split_ratio
        
    @property
    def k_neighbors(self)->int:
        return self.k

    def train_test_split(self,features:pd.DataFrame,labels:pd.Series) -> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        x_train,y_train = features.iloc[:train_size,:], labels.iloc[:train_size]
        x_test,y_test = features.iloc[train_size:train_size+test_size,:], labels.iloc[train_size:train_size + test_size]
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test


    def euclidean(self, element_of_x: pd.DataFrame) -> pd.Series:
        return ((self.x_train - element_of_x) ** 2).sum(axis=1).pow(0.5)




    def predict(self,x_test:pd.DataFrame) -> pd.Series:
        labels_pred = []
        for _, x_test_element in x_test.iterrows():
            distances = self.euclidean(x_test_element)
            distances = pd.DataFrame({'dist': distances, 'label': self.y_train})
            distances = distances.sort_values('dist').iloc[:self.k]
            label_pred = mode(distances['label'], keepdims=False).mode
            labels_pred.append(label_pred)
        self.y_preds = pd.Series(labels_pred)

    def accuracy(self) -> float:
        self.y_test.reset_index(drop=True,inplace=True)
        self.y_preds.reset_index(drop=True,inplace=True)
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100

    def confusion_matrix(self) -> pd.DataFrame:
        conf_matrix = confusion_matrix(self.y_test, self.y_preds)
        return pd.DataFrame(conf_matrix)
    
    def best_k(self) -> Tuple[int, float]:
        accuracies = []
        for k in range(1, 21):
            self.k = k
            self.predict(self.x_test)
            acc = self.accuracy()
            accuracies.append((k, acc))
        best_k, best_acc = max(accuracies, key=lambda x: x[1])
        return best_k, round(best_acc, 2)
