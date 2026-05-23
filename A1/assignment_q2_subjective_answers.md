#  Answer 2

a) The first 70% of the data was used for training purposes and the remaining 30% for test purposes. The accuracy, per-class precision and recall of the decision tree we implemented on the test dataset is as given below:

```
Criteria : information_gain
Accuracy:  0.9
Precision 0:  0.9019138755980861
Recall 0:  0.8333333333333334
Precision 1:  0.9019138755980861
Recall 1:  0.9444444444444444

Criteria : gini_index
Accuracy:  0.9
Precision 0:  0.9019138755980861
Recall 0:  0.8333333333333334
Precision 1:  0.9019138755980861
Recall 1:  0.9444444444444444
```

b) By using the nested cross-validation technique, the optimal depth of the tree was found to be:

```
Optimal depth:  6
```