
## Question 2

In this question, we are using a Matrix $A$, which is of shape $(n\times n)$, and a vector $B$ of shape $(n\times 1)$, to solve $Ax = B$. 
This can be solved in 2 ways.
  1. $x = A^{-1} B$, for which we have to compute $A^{-1}=$ `np.linalg.inv(A)` and multiplying it with $B$.
  2. Using `np.linalg.solve(A, B)`.

![Image 1](image_q2_1.png)

Here we have chosen $n$ to be `1000`, and to properly distinguish between the two methods we are solving $Ax=B$ `1000` times.

![Image 2](image_q2_2.png)

Problem: solve for $x: Ax=B$, where $A$ is $n \times n$ matrix, $B$ is $n \times 1$ vector, and $x$ is $n \times 1$ vector.

We can observe from above that `np.linalg.inv` method takes far more time than `np.linalg.solve` method for large matrices or if the calculations are repeated many times. The `np.linalg.solve` method does not calculate the inverse of $A$, it uses LU-Decomposition which factorizes $A$ then solves for $x$ using forward and backward substitution. Whereas, `np.linalg.inv` method calculates the inverse of the matrix $A$ using `np.linalg.solve` to solve $A A^{-1}=I$, where $I$ is the Identity matrix. Solving $A A^{-1}=I$ takes more operations as well as time than solving $A x=B$ directly because here $x$ is a vector of shape $(n, 1)$ whereas $A^{-1}$ is a matrix of shape $(n, n)$. Further, after calculating $A^{-1}$, we need to multiply it with B to get the solution vector $x$, which again takes more time and takes more operations. Hence, `np.linalg.solve` method is preferred over `np.linalg.inv` method for solving linear equations. We also believe that lesser the number of floating point operations, lesser the error in the solution. Hence, np.linalg.solve method is likely to be more accurate than `np.linalg.inv` method but this is not a major concern as both methods are highly accurate.
