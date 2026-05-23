# Question 6

## Encoding:
* 1 : Walking
* 2 : Walking Up
* 3 : Walking Down
* 4 : Sitting
* 5 : Standing
* 6 : Laying

## Results for classification using Decision Tree
![DT_CM](Q6_DT_cm.png)
![DT_CR](Q6_DT_cr.png)

## Results for classification using Random Forest
![RF_CM](Q6_RF_cm.png)
![RF_CR](Q6_RF_cr.png)

## Results for classification using Linear Regression (Clipping and Rounding)
![LR_clip_CM](Q6_LR_clip_cm.png)
![LR_clip_CR](Q6_LR_clip_cr.png)

## Results for classification using Linear Regression (Minimax Scalar)
![LR_minimax_CM](Q6_LR_minmax_cm.png)
![LR_minimax_CR](Q6_LR_minmax_cr.png)

## Results for classification using Linear Regression (Sigmoid)
![LR_sigmoid_CM](Q6_LR_sigmoid_cm.png)
![LR_sigmoid_CR](Q6_LR_sigmoid_cr.png)


## Accuracies Comparison
| Model | Accuracy |
| --- | ----------- |
| Decision Tree | 69.44% |
| Random Forest | 72.22% |
| Linear Regression (With Clipping) | 19.44% |
| Linear Regression (With Minimax) | 19.44% |
| Linear Regression (With Sigmoid) | 19.44% |

## Analysis
* Linear Regression has an accuracy of 69.44%, which is not very great. The reasons for this were discussed in Assignment 1. (Mainly the confusion between Static and Dynamic activities)
* Random forest is better than decision tree because it is an ensemble method and it takes the average of all the decision trees. There is no scope of overfitting. 
* The observation is that linear regression does not work for classification.
* The main reason being that the values to be predicted are of the form as given in the encoding. This essentially means that Walking Up has "Double" the value of Walking, etc. Walking Up + Walking values equal to Walking Down. The values of static acitivities are less than dynamic ones. The value of static activity "Laying" is double of dynamic activity "Walking Down". The value of Walking Up is lesser than walking down but greater than walking. A better encoding will be One Hot or One Cold method.
* Parameters estimated will have bias of the train data offsets and patterns and thus will not be able to predict the test data well.
* Parameter learnt are of large magnitude: linear regression, this shows that the model is overfitting to the train data trends.
