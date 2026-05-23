import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from tree.base import DecisionTree
from metrics import *
from tqdm import trange

np.random.seed(42)
num_average_time = 100  # Number of times to run each experiment to calculate the average values


# Function to create fake data (take inspiration from usage.py)
def fake_data(N, M, discrete_input=True, discrete_output=True):
    """
    Function to create fake data
    """
    if discrete_input:
        X = pd.DataFrame(np.random.randint(M, size=(N, M)), dtype="category")
    else:
        X = pd.DataFrame(np.random.randn(N, M))
        
    if discrete_output:
        y = pd.Series(np.random.randint(M, size=N), dtype="category")
    else:
        y = pd.Series(np.random.randn(N))
    return X, y

# Function to calculate average time (and std) taken by fit() and predict() for different N and P for 4 different cases of DTs
def time_taken(X, y, N, M, discrete_input=True, discrete_output=True):
    """
    Function to calculate average time (and std) taken by fit() and predict() for different N and P for 4 different cases of DTs
    """
    fit_time = []
    predict_time = []
    for i in trange(num_average_time):
        X, y = fake_data(N, M, discrete_input, discrete_output)
        start = time.time()
        tree = DecisionTree(criterion="information_gain")
        tree.fit(X, y)
        end = time.time()
        fit_time.append(end - start)
        start = time.time()
        y_hat = tree.predict(X)
        end = time.time()
        predict_time.append(end - start)
    return np.mean(fit_time), np.std(fit_time), np.mean(predict_time), np.std(predict_time)

# Function to plot the results
def plot_results(change, change_name, fit_time_mean, fit_time_std, predict_time_mean, predict_time_std, title):
    """
    Function to plot the results
    """
    plt.figure()
    plt.plot(change, fit_time_mean, label="fit time")
    plt.fill_between(change, fit_time_mean - fit_time_std, fit_time_mean + fit_time_std, alpha=0.2)
    plt.plot(change, predict_time_mean, label="predict time")
    plt.fill_between(change, predict_time_mean - predict_time_std, predict_time_mean + predict_time_std, alpha=0.2)
    plt.xlabel(change_name)
    plt.ylabel("Time")
    plt.title(title)
    plt.legend()
    plt.savefig("Q4_plots/" + title + ".png")
# Run the experiments
    
# Varying N for all 4 cases
    
N = [(i+1) for i in range(0, 51, 2)]
M = 10
    
# Experiment 1: Varying N for Real Input and Real Output

fit_time_mean = []
fit_time_std = []
predict_time_mean = []
predict_time_std = []
for n in N:
    X, y = fake_data(n, M, discrete_input=False, discrete_output=False)
    ftm, fts, ptm, pts = time_taken(X, y, n, M, discrete_input=False, discrete_output=False)
    fit_time_mean.append(ftm)
    fit_time_std.append(fts)
    predict_time_mean.append(ptm)
    predict_time_std.append(pts)

fit_time_mean = np.array(fit_time_mean)
fit_time_std = np.array(fit_time_std)
predict_time_mean = np.array(predict_time_mean)
predict_time_std = np.array(predict_time_std)

plot_results(N, "N", fit_time_mean, fit_time_std, predict_time_mean, predict_time_std, "Varying N Real Input and Real Output")

# Experiment 2: Varying N for Real Input and Discrete Output

fit_time_mean = []
fit_time_std = []
predict_time_mean = []
predict_time_std = []
for n in N:
    X, y = fake_data(n, M, discrete_input=False, discrete_output=True)
    ftm, fts, ptm, pts = time_taken(X, y, n, M, discrete_input=False, discrete_output=True)
    fit_time_mean.append(ftm)
    fit_time_std.append(fts)
    predict_time_mean.append(ptm)
    predict_time_std.append(pts)

fit_time_mean = np.array(fit_time_mean)
fit_time_std = np.array(fit_time_std)
predict_time_mean = np.array(predict_time_mean)
predict_time_std = np.array(predict_time_std)

plot_results(N, "N", fit_time_mean, fit_time_std, predict_time_mean, predict_time_std, "Varying N Real Input and Discrete Output")

# Experiment 3: Varying N for Discrete Input and Discrete Output

fit_time_mean = []
fit_time_std = []
predict_time_mean = []
predict_time_std = []
for n in N:
    X, y = fake_data(n, M, discrete_input=True, discrete_output=True)
    ftm, fts, ptm, pts = time_taken(X, y, n, M, discrete_input=True, discrete_output=True)
    fit_time_mean.append(ftm)
    fit_time_std.append(fts)
    predict_time_mean.append(ptm)
    predict_time_std.append(pts)

fit_time_mean = np.array(fit_time_mean)
fit_time_std = np.array(fit_time_std)
predict_time_mean = np.array(predict_time_mean)
predict_time_std = np.array(predict_time_std)

plot_results(N, "N", fit_time_mean, fit_time_std, predict_time_mean, predict_time_std, "Varying N Discrete Input and Discrete Output")

# Experiment 4: Varying N for Discrete Input and Real Output

fit_time_mean = []
fit_time_std = []
predict_time_mean = []
predict_time_std = []
for n in N:
    X, y = fake_data(n, M, discrete_input=True, discrete_output=False)
    ftm, fts, ptm, pts = time_taken(X, y, n, M, discrete_input=True, discrete_output=False)
    fit_time_mean.append(ftm)
    fit_time_std.append(fts)
    predict_time_mean.append(ptm)
    predict_time_std.append(pts)

fit_time_mean = np.array(fit_time_mean)
fit_time_std = np.array(fit_time_std)
predict_time_mean = np.array(predict_time_mean)
predict_time_std = np.array(predict_time_std)

plot_results(N, "N", fit_time_mean, fit_time_std, predict_time_mean, predict_time_std, "Varying N Discrete Input and Real Output")

# Varying M for all 4 cases

N = 20
M = [(i+1) for i in range(0, 51, 2)]

# Experiment 5: Varying M for Real Input and Real Output

fit_time_mean = []
fit_time_std = []
predict_time_mean = []
predict_time_std = []
for m in M:
    X, y = fake_data(N, m, discrete_input=True, discrete_output=True)
    ftm, fts, ptm, pts = time_taken(X, y, N, m, discrete_input=True, discrete_output=True)
    fit_time_mean.append(ftm)
    fit_time_std.append(fts)
    predict_time_mean.append(ptm)
    predict_time_std.append(pts)

fit_time_mean = np.array(fit_time_mean)
fit_time_std = np.array(fit_time_std)
predict_time_mean = np.array(predict_time_mean)
predict_time_std = np.array(predict_time_std)

plot_results(M, "M", fit_time_mean, fit_time_std, predict_time_mean, predict_time_std, "Varying M Real Input and Real Output")

# Experiment 6: Varying M for Real Input and Discrete Output

fit_time_mean = []
fit_time_std = []
predict_time_mean = []
predict_time_std = []
for m in M:
    X, y = fake_data(N, m, discrete_input=True, discrete_output=False)
    ftm, fts, ptm, pts = time_taken(X, y, N, m, discrete_input=True, discrete_output=False)
    fit_time_mean.append(ftm)
    fit_time_std.append(fts)
    predict_time_mean.append(ptm)
    predict_time_std.append(pts)

fit_time_mean = np.array(fit_time_mean)
fit_time_std = np.array(fit_time_std)
predict_time_mean = np.array(predict_time_mean)
predict_time_std = np.array(predict_time_std)

plot_results(M, "M", fit_time_mean, fit_time_std, predict_time_mean, predict_time_std, "Varying M Real Input and Discrete Output")

# Experiment 7: Varying M for Discrete Input and Discrete Output

fit_time_mean = []
fit_time_std = []
predict_time_mean = []
predict_time_std = []
for m in M:
    X, y = fake_data(N, m, discrete_input=False, discrete_output=False)
    ftm, fts, ptm, pts = time_taken(X, y, N, m, discrete_input=False, discrete_output=False)
    fit_time_mean.append(ftm)
    fit_time_std.append(fts)
    predict_time_mean.append(ptm)
    predict_time_std.append(pts)

fit_time_mean = np.array(fit_time_mean)
fit_time_std = np.array(fit_time_std)
predict_time_mean = np.array(predict_time_mean)
predict_time_std = np.array(predict_time_std)

plot_results(M, "M", fit_time_mean, fit_time_std, predict_time_mean, predict_time_std, "Varying M Discrete Input and Discrete Output")

# Experiment 8: Varying M for Discrete Input and Real Output

fit_time_mean = []
fit_time_std = []
predict_time_mean = []
predict_time_std = []
for m in M:
    X, y = fake_data(N, m, discrete_input=False, discrete_output=True)
    ftm, fts, ptm, pts = time_taken(X, y, N, m, discrete_input=False, discrete_output=True)
    fit_time_mean.append(ftm)
    fit_time_std.append(fts)
    predict_time_mean.append(ptm)
    predict_time_std.append(pts)

fit_time_mean = np.array(fit_time_mean)
fit_time_std = np.array(fit_time_std)
predict_time_mean = np.array(predict_time_mean)
predict_time_std = np.array(predict_time_std)

plot_results(M, "M", fit_time_mean, fit_time_std, predict_time_mean, predict_time_std, "Varying M Discrete Input and Real Output")