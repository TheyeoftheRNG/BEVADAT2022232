import pandas as pd
import seaborn as sns
from typing import Tuple
from scipy.stats import mode
import math
from sklearn.metrics import confusion_matrix
import random


class knnClassifier:

    def __init__(self, k: int, test_split_ratio: float) -> None:
        self.k = k
        self.test_split_ratio = test_split_ratio

    def load_csv(self, csv_path: str) -> Tuple[pd.DataFrame, pd.Series]:
        random.seed(42)
        dataset = pd.read_csv(csv_path, header=None)
        dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)
        x, y = dataset.iloc[:, :4], dataset.iloc[:, -1]
        return x, y

    def train_test_split(self, features: pd.DataFrame, labels: pd.Series) -> None:
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"
        self.x_train, self.y_train = features.iloc[:train_size, :], labels.iloc[:train_size]
        self.x_test, self.y_test = features.iloc[train_size:train_size + test_size, :], labels.iloc[
                                                                                        train_size:train_size + test_size]

    def euclidean(self, element_of_x: pd.Series) -> pd.Series:
        return [math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, element_of_x)])) for x in self.x_train]

    def predict(self, x_test: pd.DataFrame) -> pd.Series:
        labels_pred = []
        for _, x_test_element in x_test.iterrows():
            distances = self.euclidean(x_test_element)
            distances = pd.concat([distances, self.y_train], axis=1).sort_values(by=0).reset_index(drop=True)
            label_pred = mode(distances.iloc[:self.k, 1], keepdims=False).mode[0]
            labels_pred.append(label_pred)
        self.y_preds = pd.Series(labels_pred, dtype=int)

    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds).sum()
        return true_positive / len(self.y_test) * 100

    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.y_test, self.y_preds)
        sns.heatmap(conf_matrix, annot=True)
