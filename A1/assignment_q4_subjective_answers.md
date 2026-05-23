#  Answer 4

The decision tree was trained on the dataset and then tested. The plots of the time taken for 100 iterations of training and testing of the decision tree for the four cases is as attached below:

| Varying $N$ | Varying $M$ |
| :-: | :-: |
| Discrete Input and Discrete Output | Discrete Input and Discrete Output |
| ![Varying N Discrete Input and Discrete Output.png](https://github.com/ES335-2024/assignment-1-ml-students-ensemble/blob/master/Q4_plots/Varying%20N%20Discrete%20Input%20and%20Discrete%20Output.png) | ![Varying M Discrete Input and Discrete Output.png](https://github.com/ES335-2024/assignment-1-ml-students-ensemble/blob/master/Q4_plots/Varying%20M%20Discrete%20Input%20and%20Discrete%20Output.png) |
| Discrete Input and Real Output | Discrete Input and Real Output |
| ![Varying N Discrete Input and Real Output.png](https://github.com/ES335-2024/assignment-1-ml-students-ensemble/blob/master/Q4_plots/Varying%20N%20Discrete%20Input%20and%20Real%20Output.png) | ![Varying M Discrete Input and Real Output.png](https://github.com/ES335-2024/assignment-1-ml-students-ensemble/blob/master/Q4_plots/Varying%20M%20Discrete%20Input%20and%20Real%20Output.png) |
| Real Input and Discrete Output | Real Input and Discrete Output |
| ![Varying N Real Input and Discrete Output.png](https://github.com/ES335-2024/assignment-1-ml-students-ensemble/blob/master/Q4_plots/Varying%20N%20Real%20Input%20and%20Discrete%20Output.png) | ![Varying M Real Input and Discrete Output.png](https://github.com/ES335-2024/assignment-1-ml-students-ensemble/blob/master/Q4_plots/Varying%20M%20Real%20Input%20and%20Discrete%20Output.png) |
| Real Input and Real Output | Real Input and Real Output |
| ![Varying N Real Input and Real Output.png](https://github.com/ES335-2024/assignment-1-ml-students-ensemble/blob/master/Q4_plots/Varying%20N%20Real%20Input%20and%20Real%20Output.png) | ![Varying M Real Input and Real Output.png](https://github.com/ES335-2024/assignment-1-ml-students-ensemble/blob/master/Q4_plots/Varying%20M%20Real%20Input%20and%20Real%20Output.png) |

**_NOTE:_**  Even though the values of $N$ and $M$ change in the same manner...
- In the case of Discrete Input, change in the value of $M$ has a greater effect on the time taken for training compared to the change in the value of $N$. This can be because the tree would be learning more from each characteristic in each node that is not a leaf node.
- In the case of Real Input, change in the value of $N$ has a greater effect on the time taken for training compared to the change in the value of $M$. This can be because the tree would be learning more from data points.

## Observations
The algorithm design is similar to `ID3`. The theoretical time for prediction is almost of the order of the depth of the tree as we are traversing through the depth of the tree at each level only once. It is constant with respect to the other parameters. From the plots, we can see that the time complexity of prediction is constant in the parameters such as $N$ and $M$. Coming to the part of the training, we can see that for each characteristic in each node that is not a leaf node, a decision tree computes a quality function depending on each split of the data. As long as there are levels (depth) to go through, this will continue. The depth of a balanced tree would be in $O(\log{N})$ in the ideal scenario. However, the decision tree performs locally optimum splits with no regard for balancing. As a result, the worst-case scenario for depth to be in $O(N)$ is conceivable, which is essentially the case when each split separates the data into $1$ and $n-1$ examples, where $n$ is the number of examples for the current node. To sum up, decision trees have a theoretical time complexity of $O(N^2M)$ to $O(NM\log{N})$ in terms of $N$ and $M$. If the depth is maintained constant as mentioned in the question, then the time complexity is of the order of around $O(NM)$.

The dependence on $N$ for the case of:
- Discrete input and Discrete output, the dependence on $N$ is almost linear, and hence, order of $N$.
- Discrete input and Real output, the dependence on $N$ is again almost linear and therefore, order of $N$.
- Real input and Discrete output, the dependence on $N$ appears to be of the form of quadratic and some order of $N$ to $N\log{N}$.
- Real input and Real output, the dependence on $N$ is in between the order of $N$ and order of $N\log{N}$.


The dependence on $M$ for the case of:
- Discrete input and Discrete output, the dependence on $M$ is almost linear, and hence, order of $M$.
- Discrete input and Real output, the dependence on $M$ is again almost linear and therefore, order of $M$.

**_NOTE:_**  In the case of Discrete Input, the standard deviation of the time taken for training is higher when we vary $M$ compared to when we vary $N$.

- Real input and Discrete output, the dependence on $M$ appears to be of the form of quadratic and some order of $M$.
- Real input and Real output, the dependence on $M$ seems to be a combination of linear and quadratic and hence, order of $M$.

**_NOTE:_**  In the case of Real Input, the standard deviation of the time taken for training is higher when we vary $N$ compared to when we vary $M$. This is when the depth of the tree is maintained constant.

The overall order for the case of:
- Discrete input and Discrete output, is almost of order $MN$.
- Discrete input and Real output, is almost of order $MN$.
- Real input and Discrete output, is almost of order $MN\log{N}$ to $MN$.
- Real input and Real output, is almost of order $MN\log{N}$ to $MN$.

So, we can observe that the tree training is almost of order of $MN$ when the depth is maintained a constant. But since the depth is of the order of $\log{N}$ to order of $N$ in the worst case, the overall time complexity is of the order of $MN\log{N}$ to $MN^2$.

The time complexity for prediction at constant depth is constant, as we can see from the plot. So, the time complexity in the case of variable depth would be of the order of `depth` which is $\log{N}$ to $N$. So, the overall time complexity for prediction is of the order of $\log{N}$ to $N$. This matches the theoretical time complexity of decision trees.