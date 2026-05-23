## Question 3

In this question we will apply `LinearRegression` on the following feature matrix $X$ and target vector $y$ using
  1. Normal equation
  2. sklearn's `LinearRegression`
     
<img src="image_q3_1.png" alt="Image 1" width="300">
<br>
<img src="image_q3_10.png" alt="Image 2" width="300">
<br>
We can clearly see that $X$ is singular as the third column is `2` times the second column. Hence we won't be able to get solution using the Normal Equation.

<img src="image_q3_2.png" alt="Image 3" width="300">
<br>
<img src="image_q3_3.png" alt="Image 4" width="300">
<br>
As we can see above, $X$ which is the feature matrix is singular and has rank '2' (full rank = `3`), and hence $X$ is not invertible and we cannot calculate the  value of the optimal parameters or solve the normal equation of $X$ and $y$. This is a problem that arises when we have a multicollinearity in our feature matrix. Multicollinearity is a phenomenon in which one feature can be linearly predicted from the others with a substantial degree of accuracy. This is a problem because it makes the feature matrix $X$ singular and not invertible.


<br>
Let us now use sklearn's implementation of `LinearRegression` to solve the same problem.
<br>
<img src="image_q3_4.png" alt="Image 5" width="300">
<br>

We can see that the `LinearRegression` model from the scikit-learn library is able to handle this problem and still give us the optimal parameters. 
<br>
<br>
Let us dive into sklearn's code and see why this is the case.
<br>
Sklearn's Linear Regression uses the non-negative least squares (`nnls`) function from `scipy.optimize` to solve the linear regression problem, the `lsqr` function from `scipy.sparse.linalg` which uses the Paige and Saunders algorithm which is an iterative algorithm to approximate the solution as well as the `lstsq` function from `scipy.linalg` for different scenarios. 


Importing `scipy.optimize.nnls` and `scipy.sparse.linalg.lsqr`
<br>
<img src="https://github.com/ES335-2024/assignment-2-es-335-2024-students-ensemble/blob/master/image_q3_11.png" alt="Image 6" width="500">
<br>
The `LinearRegression` function uses `scipy.optimize.nnls` in the case in which we want positive parameters.
<br>
<img src="https://github.com/ES335-2024/assignment-2-es-335-2024-students-ensemble/blob/master/image_q_13.png" alt="Image 7" width="500">
<br>
`scipy.sparse.linalg.lsqr` in case $X$ (feature matrix) is sparse
<br>
<img src="https://github.com/ES335-2024/assignment-2-es-335-2024-students-ensemble/blob/master/image_q_14.png" alt="Image 8" width="500">
<br>
<img src="https://github.com/ES335-2024/assignment-2-es-335-2024-students-ensemble/blob/master/image_q_15.png" alt="Image 9" width="500">
<br>
and in all other cases it uses `scipy.linalg.lstsq` function.
<br>
<img src="https://github.com/ES335-2024/assignment-2-es-335-2024-students-ensemble/blob/master/image_q3_12.png" alt="Image 10" width="500">
<br>
<br>
When the feature matrix is singular, the optimal parameters cannot be calculated using the normal equation as shown above. For the cases of `scipy.optimize.nnls` and `scipy.linalg.lstsq`, the functions calculates the Moore-Penrose pseudo-inverse of the feature matrix and uses it to calculate the optimal parameters.
The Moore-Penrose pseudo-inverse is calculated using the reduced singular value decomposition (SVD) of the feature matrix. The reduced SVD is a factorization of the feature matrix into three matrices U, S, and V such that the feature matrix is equal to the product of $U$, $S$, and $V^T$, $U$ is of shape $(n, m)$, $V$ is of shape $(m, m)$ and $S$ is a diagonal matrix of shape $(m, m)$. The Moore-Penrose pseudo-inverse is calculated as the product of $VS^{-1}U^T$. The Moore-Penrose pseudo-inverse is then used to calculate the optimal parameters using the normal equation. The optimal parameters are calculated as the product of the Moore-Penrose pseudo-inverse and the target vector. The functions then uses the optimal parameters to calculate the predicted target vector. The predicted target vector is calculated as the product of the feature matrix and the optimal parameters. Hence, we do not get an error using the Linear Regression model when the feature matrix is singular. Following is how the Moore-Penrose pseudo-inverse is calculated using the reduced SVD of the feature matrix:
<br>
<img src="https://github.com/ES335-2024/assignment-2-es-335-2024-students-ensemble/blob/master/image_q_16.png" alt="Image 11" width="700">
