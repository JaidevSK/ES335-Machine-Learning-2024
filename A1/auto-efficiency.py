import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from tree.base import DecisionTree
from metrics import *

np.random.seed(42)

# Reading the data
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
data = pd.read_csv(url, delim_whitespace=True, header=None,
                 names=["mpg", "cylinders", "displacement", "horsepower", "weight",
                        "acceleration", "model year", "origin", "car name"])

# Clean the above data by removing redundant columns and rows with junk values

# drop "car name" column
data.drop("car name", axis=1, inplace=True)

# drop rows with NA
data = data.dropna()

# drop rows with "?"
data.drop(data[data["horsepower"] == "?"].index, inplace=True)

# convert "horsepower" column to float
data["horsepower"] = data["horsepower"].astype("float64")

# convert "origin" column to category
data["origin"] = data["origin"].astype("category")

# convert "model year" column to category
data["model year"] = data["model year"].astype("category")

# convert "cylinders" column to category
data["cylinders"] = data["cylinders"].astype("category")

X = data.drop('mpg', axis=1)
y = data['mpg']

dt = DecisionTree(max_depth=5)
dt.fit(X, y)

y_hat_our = dt.predict(X)


# Compare the performance of your model with the decision tree module from scikit learn
dt_sk = DecisionTreeRegressor(max_depth=5)

dt_sk.fit(X, y)

y_pred_sk = dt_sk.predict(X)

print("RMSE (our): ", rmse(y_hat_our, y))
print("RMSE (sklearn): ", rmse(y_pred_sk, y))

print("MAE (our): ", mae(y_hat_our, y))
print("MAE (sklearn): ", mae(y_pred_sk, y))