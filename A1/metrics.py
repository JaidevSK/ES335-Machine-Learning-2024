from typing import Union
import pandas as pd
import numpy as np


def accuracy(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the accuracy
    """

    """
    The following assert checks if sizes of y_hat and y are equal.
    Students are required to add appropriate assert checks at places to
    ensure that the function does not fail in corner cases.
    """
    assert y_hat.size == y.size

    if isinstance(y, np.ndarray):
        y = pd.Series(y)

    c=0
    for i in range(y.size):
        if y_hat.iloc[i]==y.iloc[i]:
            c+=1
    return c/y.size


def precision_help(y_hat, y, cls):
    """
    Function to calculate precision for a specific class
    """
    assert y_hat.size == y.size
    true_positives = sum((y_hat == cls) & (y == cls))
    all_predicted_positives = (y_hat == cls).sum()
    return true_positives / all_predicted_positives if all_predicted_positives > 0 else 0

def precision(y_hat: pd.Series, y: pd.Series, cls: Union[int, str]) -> float:
    """
    Function to calculate average precision for multi-class classification
    """
    unique_classes = y.unique()
    precisions = [precision_help(y_hat, y, cls) for cls in unique_classes]
    return sum(precisions) / len(unique_classes)


def recall(y_hat: pd.Series, y: pd.Series, cls: Union[int, str]) -> float:
    """
    Function to calculate the recall
    """
    assert y_hat.size == y.size
    c=0
    for i in range(y.size):
        if y.iloc[i]==y_hat.iloc[i] and y.iloc[i]==cls:
            c+=1
    return c/y.value_counts()[cls]


def rmse(y: pd.Series, y_hat: pd.Series) -> float:
    """
    Function to calculate the root-mean-squared-error(rmse)
    """
    assert y.size == y_hat.size
    ms = mse(y, y_hat)
    return np.sqrt(ms)


def mse(y: pd.Series, y_hat: pd.Series=None) -> float:
    """
    Function to calculate the mean-squared-error(mse)
    """

    if y_hat is None:
        y_hat = y.mean()

        # make sure y_hat and y have the same size
        y_hat = np.array([y_hat for _ in range(y.size)])
        
    assert y.size == y_hat.size
    ms=np.square(y-y_hat).mean()
    return ms



def mae(y: pd.Series, y_hat: pd.Series) -> float:
    """
    Function to calculate the mean-absolute-error(mae)
    """
    assert y.size == y_hat.size
    m_ae=np.abs(y-y_hat).mean()
    return m_ae