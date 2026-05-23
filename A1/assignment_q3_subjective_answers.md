# Answer 3

The Auto MPG dataset was used for this question.

- drop the `car name` column
- drop the rows with missing values
- drop the rows with `horsepower` as `?`
- convert the `horsepower` column to `float`
- convert the `dtype` of columns `origin`, `cylinders` and `model year` to `category`

- `X` = all columns except `mpg`
- `y` = `mpg` column

This dataset was used to train the decision tree for `max_depth=5`.

Here are the Root Mean Squared Error(RMSE) and Mean Absolute Error(MAE) values for the comparison of our decision tree with the `sklearn` decision tree:

```
RMSE (our):  6.212348187743267
RMSE (sklearn):  2.178138849149237
MAE (our):  4.334702689365902
MAE (sklearn):  1.5952216438662674
```