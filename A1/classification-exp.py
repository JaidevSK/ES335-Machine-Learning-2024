import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tree.base import DecisionTree
from metrics import *
from sklearn.datasets import make_classification

np.random.seed(42)

# Code given in the question
X, y = make_classification(
    n_features=2, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=2, class_sep=0.5)

# For plotting
plt.scatter(X[:, 0], X[:, 1], c=y)

# Write the code for Q2 a) and b) below. Show your results.

# a) Show the usage of your decision tree on the above dataset. The first 70% of the data should be used for training purposes and the remaining 30% for test purposes. Show the accuracy, per-class precision and recall of the decision tree you implemented on the test dataset.

train_size = int(0.7 * len(X))
X_train = X[:train_size]
X_test = X[train_size:]
y_train = y[:train_size]
y_test = y[train_size:]

# convert to pandas dataframe
X_train = pd.DataFrame(X_train)
X_test = pd.DataFrame(X_test)
y_train = pd.Series(y_train, dtype="category")
y_test = pd.Series(y_test, dtype="category")

tree = DecisionTree(criterion="information_gain")
tree.fit(X_train, y_train)
y_hat = tree.predict(X_test)
tree.plot()
print("Criteria :", "information_gain")
print("Accuracy: ", accuracy(y_hat, y_test))
for cls in y_test.unique():
    print(cls, "Precision: ", precision(y_hat, y_test, cls))
    print(cls, "Recall: ", recall(y_hat, y_test, cls))

tree = DecisionTree(criterion="gini_index")
tree.fit(X_train, y_train)
y_hat = tree.predict(X_test)
tree.plot()
print("Criteria :", "gini_index")
print("Accuracy: ", accuracy(y_hat, y_test))
for cls in y_test.unique():
    print(cls, "Precision: ", precision(y_hat, y_test, cls))
    print(cls, "Recall: ", recall(y_hat, y_test, cls))

# b) Use 5 fold cross-validation on the dataset. Using nested cross-validation find the optimum depth of the tree.

def KFold(X, y, k=5):
    X = np.array(X)
    y = np.array(y)
    X_split = np.array_split(X, k)
    y_split = np.array_split(y, k)
    for i in range(k):
        X_test = X_split[i]
        y_test = y_split[i]
        X_train = np.concatenate(X_split[:i] + X_split[i+1:])
        y_train = np.concatenate(y_split[:i] + y_split[i+1:])
        yield pd.DataFrame(X_train), pd.Series(y_train), pd.DataFrame(X_test), pd.Series(y_test)

def nested_cross_validation(X, y, k=5):
    best_depth = 0
    best_accuracy = 0
    for depth in range(1, 11):
        acc = 0
        for X_train, y_train, X_test, y_test in KFold(X, y, k):
            tree = DecisionTree(criterion="information_gain", max_depth=depth)
            tree.fit(X_train, y_train)
            y_hat = tree.predict(X_test)
            acc += accuracy(y_hat, y_test)
        acc /= k
        if acc > best_accuracy:
            best_accuracy = acc
            best_depth = depth
    return best_depth

print(f"best depth: {nested_cross_validation(X, y)}")