# Q7

## Parameter Values in Linear Regression
![LR_Param](Q7_LR_param.png)

## Feature Importance Values in Random Forest
![RF_FI](Q7_RF_FeatureImp.png)

## Comparison between the Feature Importance values and Linear Regression Parameter values
![RFLR](Q7_RFLR.png)
Orange Bars: Random Forest <br>
Blue Bars: Linear Regression

## Top 10 Feature Importance values and Linear Regression Parameter values
![LR_t10](Q7_LR_Top10.png)
![RF_t10](Q7_RF_Top10.png)
<br>
![LR_t10_names](Q7_LR_top10names.png)
![RF_t10_names](Q7_RF_top10names.png)

## Inference 
* The list of parameters by importance is as given.
* The first observation is that the top 10 features with highest importance and the top 10 features with highest Linear regression parameter values are not the same.
* This is also reflected in the thought that the way Linear Regression and Random Forest work is completely different.
* One more major observation is that the RF Feature importance is given only to a few features, whereas the parameter value for the Linear regression is given to almost all the features.
* We can also see that the feature importance roughly follows the trend of parameter values for features greater than index 300.
