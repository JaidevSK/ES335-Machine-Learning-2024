"""
You can add your own functions here according to your decision tree implementation.
There is no restriction on following the below template, these fucntions are here to simply help you.
"""

import pandas as pd
import numpy as np
from scipy.special import xlogy
from metrics import *


def check_ifreal(y: pd.Series) -> bool:
    """
    Function to check if the given series has real or discrete values
    """

    if isinstance(y, int) or isinstance(y, float):
        return True

    if isinstance(y, pd.Series):
        if y.dtype in ("category", "object"):
            return False
        
        return True
    
    return False

def entropy(Y: pd.Series) -> float:
    """
    Function to calculate the entropy
    """
    val_counts = Y.value_counts()
    p = val_counts/val_counts.sum()
    entropy = -np.sum(xlogy(p, p)/np.log(2))

    return entropy


def gini_index(Y: pd.Series) -> float:
    """
    Function to calculate the gini index
    """
    val_counts = Y.value_counts()
    p = val_counts/val_counts.sum()
    gini = 1 - np.sum(np.square(p))

    return gini


def variance(y: pd.Series) -> float:
    """
    Function to calculate the variance
    """
    return np.var(y)


def information(y: pd.Series, y_children: pd.Series, criterion=None) -> float:
    """
    Function to calculate the information gain
    """
    discrete = not check_ifreal(y)

    weights = [len(y_child)/len(y) for y_child in y_children]
    
    if discrete:
        if criterion in ("information_gain", None):
            info = entropy(y) - np.sum([w*entropy(y_child) for w, y_child in zip(weights, y_children)])
        elif criterion == "gini_index":
            info = gini_index(y) - np.sum([w*gini_index(y_child) for w, y_child in zip(weights, y_children)])
    else:
        info = mse(y) - np.sum([w*mse(y_child) for w, y_child in zip(weights, y_children)])
        # if criterion in ("information_gain", None):
        #     info = mse(y) - np.sum([w*mse(y_child) for w, y_child in zip(weights, y_children)])
        # elif criterion == "gini_index":
        #     info = variance(y) - np.sum([w*variance(y_child) for w, y_child in zip(weights, y_children)])

    return info


def opt_split_attribute(X: pd.DataFrame, y: pd.Series, criterion, features: pd.Series):
    """
    Function to find the optimal attribute to split about.
    If needed you can split this function into 2, one for discrete and one for real valued features.
    You can also change the parameters of this function according to your implementation.

    features: pd.Series is a list of all the attributes we have to split upon

    return: attribute to split upon
    """

    # According to wheather the features are real or discrete valued and the criterion, find the attribute from the features series with the maximum information gain (entropy or varinace based on the type of output) or minimum gini index (discrete output).

    pass


def split_data(X: pd.DataFrame, y: pd.Series, attribute, value):
    """
    Funtion to split the data according to an attribute.
    If needed you can split this function into 2, one for discrete and one for real valued features.
    You can also change the parameters of this function according to your implementation.

    attribute: attribute/feature to split upon
    value: value of that attribute to split upon

    return: splitted data(Input and output)
    """

    # Split the data based on a particular value of a particular attribute. You may use masking as a tool to split the data.

    pass
