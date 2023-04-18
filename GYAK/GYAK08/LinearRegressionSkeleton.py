import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from matplotlib import pyplot as plt



class LinearRegression:
    def __init__(self, epochs, lr ):
        self.epochs = epochs
        self.lr=lr
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        self.X = df['petal length (cm)'].values
        self.y = df['petal width (cm)'].values

    def fit(self):

       self. X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X , self.y, test_size=0.2, random_state=42)


    def predict(self):
        # Building the model
        m = 0
        c = 0

        n = float(len(self.X_train)) # Number of elements in X

        # Performing Gradient Descent 
        losses = []
        for i in range(self.epochs): 
            self.y_pred = m*self.X_train + c  # The current predicted value of Y

            residuals = self.y_train - self.y_pred
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(self.X_train * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            m = m - self.lr * D_m  # Update m
            c = c - self.lr * D_c  # Update c
        
        plt.plot(losses)

        pred = []
        for X in self.X_test:
            self.y_pred = m*X + c
            pred.append(self.y_pred)
        print(pred)
        print(self.y_test)

        self.y_pred = m*self.X_test + c



    def evaluate(self):
        # Calculate the Mean Absolue Error
        print("Mean Absolute Error:", np.mean(np.abs(self.y_pred - self.y_test)))

        # Calculate the Mean Squared Error
        print("Mean Squared Error:", np.mean((self.y_pred - self.y_test)**2))

        plt.scatter(self.X_test, self.y_test)
        plt.plot([min(self.X_test), max(self.X_test)], [min(self.y_pred), max(self.y_pred)], color='red') # predicted
        plt.show()


        
        
