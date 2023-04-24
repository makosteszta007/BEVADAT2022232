# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as skl
from typing import Tuple

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error

# %%
'''
Készíts egy függvényt, betölti majd vissza adja az iris adathalmazt.


Egy példa a kimenetre: iris
return type: sklearn.utils.Bunch
függvény neve: load_iris_data
'''

# %%
#1
def load_iris_data() -> skl.utils.Bunch:
    return load_iris()

#irisData = load_iris_data()
#print(irisData)

# %%
'''
Készíts egy függvényt, ami a betölti az virágokhoz tartozó levél méretket egy dataframebe, majd az elsõ 5 sort visszaadja.
Minden oszlop tartalmazza, hogy az milyen mérethez tartozik.

Egy példa a bemenetre: iris
Egy példa a kimenetre: iris_df
return type: pandas.core.frame.DataFrame
függvény neve: check_data
'''

# %%
#2
def check_data(iris) -> pd.core.frame.DataFrame:
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names).head(5)
    return iris_df

#check_data(irisData)

#3
def linear_train_data(iris) -> Tuple[np.ndarray, np.ndarray]:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    X = df[['sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].values
    y = df['sepal length (cm)'].values
    return X, y

#linear_train_data(irisData)

#4
def logistic_train_data(iris) -> Tuple[np.ndarray, np.ndarray]:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    X = df.loc[np.where(iris.target < 2)].values
    y = iris.target[np.where(iris.target < 2)]
    return X,y

#X,y = logistic_train_data(irisData)

#5
def split_data(X, y) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    split = train_test_split(X, y, test_size=0.2, random_state=42)
    return split

#X_train, X_test, y_train, y_test = split_data(X,y)
#6
def train_linear_regression(X_train, y_train) -> skl.linear_model._base.LinearRegression:
    model = LinearRegression().fit(X_train, y_train)
    return model

#lin_model = train_linear_regression(X_train, y_train)


#7
def train_logistic_regression(X_train, y_train) -> skl.linear_model._logistic.LogisticRegression:
    model = LogisticRegression(solver='liblinear', random_state=42).fit(X_train, y_train)
    return model

#log_model = train_logistic_regression(X_train, y_train)


#8
def predict(model, X_test) -> np.ndarray:
    y_pred =  model.predict(X_test)
    return y_pred

#y_pred_lin = predict(lin_model, X_test)
#print(predict(lin_model, X_test))

#y_pred_log = predict(log_model, X_test)
#print(predict(log_model, X_test))


#9
def plot_actual_vs_predicted(y_test, y_pred) -> plt.Figure:
    scatter_plot, ax = plt.subplots()
    
    ax.scatter(y_test, y_pred)

    ax.set_title("Actual vs Predicted Target Values")
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    
    return scatter_plot


#plot_actual_vs_predicted(y_test, y_pred_lin)

#10
def evaluate_model(y_test, y_pred) -> float:
    mse = mean_squared_error(y_test, y_pred)
    return mse

#evaluate_model(y_test, y_pred_lin)

