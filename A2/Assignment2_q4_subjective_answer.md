# Question 4

## Part 1

Image Super Resolution: Enhancing the resolution of an image by a factor of 2 by using RFF + Linear Regression

![Orginal Image](dog2_original.png)<br>
This is the original image of the dog of resolution 100 x 100 pixels.

We then used Random Fourier Features for the reconstruction of the 200x200 image as result.

### Results

![Results after 2 Iterations](Q4_1_2.png)<br>
This is the reconstructed 200 x 200 image after 2 iterations of training.

![Results after 10 Iterations](Q4_1_10.png)<br>
This is the reconstructed 200 x 200 image after 10 iterations of training.

![Results after 20 Iterations](Q4_1_20.png)<br>
This is the reconstructed 200 x 200 image after 20 iterations of training.

![Results after 30 Iterations](Q4_1_30.png)<br>
This is the reconstructed 200 x 200 image after 30 iterations of training.

![Results after 40 Iterations](Q4_1_40.png)<br>
This is the reconstructed 200 x 200 image after 40 iterations of training.

![Results after 50 Iterations](Q4_1_50.png)<br>
This is the reconstructed 200 x 200 image after 50 iterations of training.

![Results after 60 Iterations](Q4_1_60.png)<br>
This is the reconstructed 200 x 200 image after 60 iterations of training.

![Results after 70 Iterations](Q4_1_70.png)<br>
This is the reconstructed 200 x 200 image after 70 iterations of training.

![Results after 80 Iterations](Q4_1_80.png)<br>
This is the reconstructed 200 x 200 image after 80 iterations of training.

![Results after 90 Iterations](Q4_1_90.png)<br>
This is the reconstructed 200 x 200 image after 90 iterations of training.

![Results after 100 Iterations](Q4_1_100.png)<br>
This is the reconstructed 200 x 200 image after 100 iterations of training.

![Training MSE loss against the number of iterations of training](Q4_1_trainMSE.png)<br>
Training MSE loss against the number of iterations of training.

![Training PSNR against the number of iterations of training](Q4_1_trainPSNR.png)<br>
Training PSNR against the number of iterations of training.

## Part 2

* Start with a 400x400 image (ground truth high resolution).
* Resize it to a 200x200 image (input image)
* Use RFF + Linear regression to increase the resolution to 400x400 (predicted high resolution image)
* Compute the following metrics:
  * RMSE on predicted v/s ground truth high resolution image
  * Peak SNR


![Orginal Image](Q4_2_original.png)<br>
This is the original image of resolution 400 x 400 pixels.

![Resized Image](Q4_2_resized.png)<br>
This is the resized image of resolution 200 x 200 pixels.

## Results

![Results after 10 Iterations](Q4_2_10.png)<br>
This is the reconstructed 400 x 400 image after 10 iterations of training.

![Results after 20 Iterations](Q4_2_20.png)<br>
This is the reconstructed 400 x 400 image after 20 iterations of training.

![Results after 30 Iterations](Q4_2_30.png)<br>
This is the reconstructed 400 x 400 image after 30 iterations of training.

![Results after 40 Iterations](Q4_2_40.png)<br>
This is the reconstructed 400 x 400 image after 40 iterations of training.

![Results after 50 Iterations](Q4_2_50.png)<br>
This is the reconstructed 400 x 400 image after 50 iterations of training.

![Results after 60 Iterations](Q4_2_60.png)<br>
This is the reconstructed 400 x 400 image after 60 iterations of training.

![Results after 70 Iterations](Q4_2_70.png)<br>
This is the reconstructed 400 x 400 image after 70 iterations of training.

![Results after 80 Iterations](Q4_2_80.png)<br>
This is the reconstructed 400 x 400 image after 80 iterations of training.

![Results after 90 Iterations](Q4_2_90.png)<br>
This is the reconstructed 400 x 400 image after 90 iterations of training.

![Results after 100 Iterations](Q4_2_100.png)<br>
This is the reconstructed 400 x 400 image after 100 iterations of training.

![Training MSE loss against the number of iterations of training](Q4_2_trainMSE.png)<br>
Training MSE loss against the number of iterations of training.

![Training PSNR against the number of iterations of training](Q4_2_trainPSNR.png)<br>
Training PSNR against the number of iterations of training.

![Testing MSE loss against the number of iterations of Testing](Q4_2_testMSE.png)<br>
Testing MSE loss against the number of iterations of Testing.

![Testing PSNR against the number of iterations of Testing](Q4_2_testPSNR.png)<br>
Testing PSNR against the number of iterations of Testing.



## Part 3
* Completing Image with Random Missing Data.
* Display the reconstructed images for each missing data percentage and show the metrics calculated above
* What do you conclude?

### Results

#### 10% datapoints removed

![Orginal Image](dog2_original.png)<br>
This is the original image of the dog of resolution 100 x 100 pixels.

![Image after 10% datapoints removed](Q4_3_10_original.png)<br>
Image after removing 10% of datapoints randomly.

![Results after 10% data removed 10 Iterations](Q4_3_10_10.png)<br>
Reconstructed image after 10 iterations for image with 10% of datapoints removed randomly.

![Results after 10% data removed 20 Iterations](Q4_3_10_20.png)<br>
Reconstructed image after 20 iterations for image with 10% of datapoints removed randomly.

![Results after 10% data removed 30 Iterations](Q4_3_10_30.png)<br>
Reconstructed image after 30 iterations for image with 10% of datapoints removed randomly.

![Results after 10% data removed 40 Iterations](Q4_3_10_40.png)<br>
Reconstructed image after 40 iterations for image with 10% of datapoints removed randomly.

![Results after 10% data removed 50 Iterations](Q4_3_10_50.png)<br>
Reconstructed image after 50 iterations for image with 10% of datapoints removed randomly.

![Results after 10% data removed 60 Iterations](Q4_3_10_60.png)<br>
Reconstructed image after 60 iterations for image with 10% of datapoints removed randomly.

![Results after 10% data removed 70 Iterations](Q4_3_10_70.png)<br>
Reconstructed image after 70 iterations for image with 10% of datapoints removed randomly.

![Results after 10% data removed 80 Iterations](Q4_3_10_80.png)<br>
Reconstructed image after 80 iterations for image with 10% of datapoints removed randomly.

![Results after 10% data removed 90 Iterations](Q4_3_10_90.png)<br>
Reconstructed image after 90 iterations for image with 10% of datapoints removed randomly.

![Results after 10% data removed 100 Iterations](Q4_3_10_100.png)<br>
Reconstructed image after 100 iterations for image with 10% of datapoints removed randomly.

![Training MSE loss against the number of iterations of training for image with 10% of datapoints removed randomly.](Q4_3_10_trainMSE.png)<br>
Training MSE loss against the number of iterations of training for image with 10% of datapoints removed randomly.

![Training PSNR against the number of iterations of training for image with 10% of datapoints removed randomly.](Q4_3_10_trainPSNR.png)<br>
Training PSNR against the number of iterations of training for image with 10% of datapoints removed randomly.


#### 20% datapoints removed

![Orginal Image](dog2_original.png)<br>
This is the original image of the dog of resolution 100 x 100 pixels.

![Image after 20% datapoints removed](Q4_3_20_original.png)<br>
Image after removing 20% of datapoints randomly.

![Results after 20% data removed 10 Iterations](Q4_3_20_10.png)<br>
Reconstructed image after 10 iterations for image with 20% of datapoints removed randomly.

![Results after 20% data removed 50 Iterations](Q4_3_20_50.png)<br>
Reconstructed image after 50 iterations for image with 20% of datapoints removed randomly.

![Results after 10% data removed 100 Iterations](Q4_3_10_100.png)<br>
Reconstructed image after 100 iterations for image with 10% of datapoints removed randomly.

![Training MSE loss against the number of iterations of training for image with 20% of datapoints removed randomly.](Q4_3_20_trainMSE.png)<br>
Training MSE loss against the number of iterations of training for image with 20% of datapoints removed randomly.

![Training PSNR against the number of iterations of training for image with 20% of datapoints removed randomly.](Q4_3_20_trainPSNR.png)<br>
Training PSNR against the number of iterations of training for image with 20% of datapoints removed randomly.



#### 30% datapoints removed

![Orginal Image](dog2_original.png)<br>
This is the original image of the dog of resolution 100 x 100 pixels.

![Image after 30% datapoints removed](Q4_3_30_original.png)<br>
Image after removing 30% of datapoints randomly.

![Results after 30% data removed 10 Iterations](Q4_3_30_10.png)<br>
Reconstructed image after 10 iterations for image with 30% of datapoints removed randomly.

![Results after 30% data removed 50 Iterations](Q4_3_30_50.png)<br>
Reconstructed image after 50 iterations for image with 30% of datapoints removed randomly.

![Results after 30% data removed 100 Iterations](Q4_3_30_100.png)<br>
Reconstructed image after 100 iterations for image with 30% of datapoints removed randomly.

![Training MSE loss against the number of iterations of training for image with 30% of datapoints removed randomly.](Q4_3_30_trainMSE.png)<br>
Training MSE loss against the number of iterations of training for image with 30% of datapoints removed randomly.

![Training PSNR against the number of iterations of training for image with 30% of datapoints removed randomly.](Q4_3_30_trainPSNR.png)<br>
Training PSNR against the number of iterations of training for image with 30% of datapoints removed randomly.



#### 40% datapoints removed

![Orginal Image](dog2_original.png)<br>
This is the original image of the dog of resolution 100 x 100 pixels.

![Image after 40% datapoints removed](Q4_3_40_original.png)<br>
Image after removing 40% of datapoints randomly.

![Results after 40% data removed 10 Iterations](Q4_3_40_10.png)<br>
Reconstructed image after 10 iterations for image with 40% of datapoints removed randomly.

![Results after 40% data removed 50 Iterations](Q4_3_40_50.png)<br>
Reconstructed image after 50 iterations for image with 40% of datapoints removed randomly.

![Results after 40% data removed 100 Iterations](Q4_3_40_100.png)<br>
Reconstructed image after 100 iterations for image with 40% of datapoints removed randomly.

![Training MSE loss against the number of iterations of training for image with 40% of datapoints removed randomly.](Q4_3_40_trainMSE.png)<br>
Training MSE loss against the number of iterations of training for image with 40% of datapoints removed randomly.

![Training PSNR against the number of iterations of training for image with 40% of datapoints removed randomly.](Q4_3_40_trainPSNR.png)<br>
Training PSNR against the number of iterations of training for image with 40% of datapoints removed randomly.



#### 50% datapoints removed

![Orginal Image](dog2_original.png)<br>
This is the original image of the dog of resolution 100 x 100 pixels.

![Image after 50% datapoints removed](Q4_3_50_original.png)<br>
Image after removing 50% of datapoints randomly.

![Results after 50% data removed 10 Iterations](Q4_3_50_10.png)<br>
Reconstructed image after 10 iterations for image with 50% of datapoints removed randomly.

![Results after 50% data removed 50 Iterations](Q4_3_50_50.png)<br>
Reconstructed image after 50 iterations for image with 50% of datapoints removed randomly.

![Results after 50% data removed 100 Iterations](Q4_3_50_100.png)<br>
Reconstructed image after 100 iterations for image with 50% of datapoints removed randomly.

![Training MSE loss against the number of iterations of training for image with 50% of datapoints removed randomly.](Q4_3_50_trainMSE.png)<br>
Training MSE loss against the number of iterations of training for image with 50% of datapoints removed randomly.

![Training PSNR against the number of iterations of training for image with 50% of datapoints removed randomly.](Q4_3_50_trainPSNR.png)<br>
Training PSNR against the number of iterations of training for image with 50% of datapoints removed randomly.




#### 60% datapoints removed

![Orginal Image](dog2_original.png)<br>
This is the original image of the dog of resolution 100 x 100 pixels.

![Image after 60% datapoints removed](Q4_3_60_original.png)<br>
Image after removing 60% of datapoints randomly.

![Results after 60% data removed 10 Iterations](Q4_3_60_10.png)<br>
Reconstructed image after 10 iterations for image with 60% of datapoints removed randomly.

![Results after 60% data removed 50 Iterations](Q4_3_60_50.png)<br>
Reconstructed image after 50 iterations for image with 60% of datapoints removed randomly.

![Results after 60% data removed 100 Iterations](Q4_3_60_100.png)<br>
Reconstructed image after 100 iterations for image with 60% of datapoints removed randomly.

![Training MSE loss against the number of iterations of training for image with 60% of datapoints removed randomly.](Q4_3_60_trainMSE.png)<br>
Training MSE loss against the number of iterations of training for image with 60% of datapoints removed randomly.

![Training PSNR against the number of iterations of training for image with 60% of datapoints removed randomly.](Q4_3_60_trainPSNR.png)<br>
Training PSNR against the number of iterations of training for image with 60% of datapoints removed randomly.


#### 70% datapoints removed

![Orginal Image](dog2_original.png)<br>
This is the original image of the dog of resolution 100 x 100 pixels.

![Image after 70% datapoints removed](Q4_3_70_original.png)<br>
Image after removing 70% of datapoints randomly.

![Results after 70% data removed 10 Iterations](Q4_3_70_10.png)<br>
Reconstructed image after 10 iterations for image with 70% of datapoints removed randomly.

![Results after 70% data removed 50 Iterations](Q4_3_70_50.png)<br>
Reconstructed image after 50 iterations for image with 70% of datapoints removed randomly.

![Results after 70% data removed 100 Iterations](Q4_3_70_100.png)<br>
Reconstructed image after 100 iterations for image with 70% of datapoints removed randomly.

![Training MSE loss against the number of iterations of training for image with 70% of datapoints removed randomly.](Q4_3_70_trainMSE.png)<br>
Training MSE loss against the number of iterations of training for image with 70% of datapoints removed randomly.

![Training PSNR against the number of iterations of training for image with 70% of datapoints removed randomly.](Q4_3_70_trainPSNR.png)<br>
Training PSNR against the number of iterations of training for image with 70% of datapoints removed randomly.




#### 80% datapoints removed

![Orginal Image](dog2_original.png)<br>
This is the original image of the dog of resolution 100 x 100 pixels.

![Image after 80% datapoints removed](Q4_3_80_original.png)<br>
Image after removing 80% of datapoints randomly.

![Results after 80% data removed 10 Iterations](Q4_3_80_10.png)<br>
Reconstructed image after 10 iterations for image with 80% of datapoints removed randomly.

![Results after 80% data removed 50 Iterations](Q4_3_80_50.png)<br>
Reconstructed image after 50 iterations for image with 80% of datapoints removed randomly.

![Results after 80% data removed 100 Iterations](Q4_3_80_100.png)<br>
Reconstructed image after 100 iterations for image with 80% of datapoints removed randomly.

![Training MSE loss against the number of iterations of training for image with 80% of datapoints removed randomly.](Q4_3_80_trainMSE.png)<br>
Training MSE loss against the number of iterations of training for image with 80% of datapoints removed randomly.

![Training PSNR against the number of iterations of training for image with 80% of datapoints removed randomly.](Q4_3_80_trainPSNR.png)<br>
Training PSNR against the number of iterations of training for image with 80% of datapoints removed randomly.




#### 90% datapoints removed

![Orginal Image](dog2_original.png)<br>
This is the original image of the dog of resolution 100 x 100 pixels.

![Image after 90% datapoints removed](Q4_3_90_original.png)<br>
Image after removing 90% of datapoints randomly.

![Results after 90% data removed 10 Iterations](Q4_3_90_10.png)<br>
Reconstructed image after 10 iterations for image with 90% of datapoints removed randomly.

![Results after 90% data removed 50 Iterations](Q4_3_90_50.png)<br>
Reconstructed image after 50 iterations for image with 90% of datapoints removed randomly.

![Results after 90% data removed 100 Iterations](Q4_3_90_100.png)<br>
Reconstructed image after 100 iterations for image with 90% of datapoints removed randomly.

![Training MSE loss against the number of iterations of training for image with 90% of datapoints removed randomly.](Q4_3_90_trainMSE.png)<br>
Training MSE loss against the number of iterations of training for image with 90% of datapoints removed randomly.

![Training PSNR against the number of iterations of training for image with 90% of datapoints removed randomly.](Q4_3_90_trainPSNR.png)<br>
Training PSNR against the number of iterations of training for image with 90% of datapoints removed randomly.


## Conclusion and Discussion

* We can observe that as the number of training iterations increase, we get more and more improvement in the image quality as seen visually (Qualitatively).
* We can also see that as the number of iterations increase, we get reduction in the MSE loss till some extent after which, there is not much loss in the MSE.
* Similar is the case with PSNR, which increases to some extent; however after certain number of iterations, the increase in PSNR is not as "profitable".
* We can aslo see that as more and more % of datapoints are randomly removed from the training data, the quality diminishes. The quality of the reconstructed image is no longer as good as the original one for more % of points missing.
* We can also see this observation from the metrics plot of PSNR as well as from the visual quality of the image.

| Percentage of Image Degraded | Testing MSE (After 100 iterations) | Testing PSNR (After 100 iterations) |
| ----------- | ----------- | ----------- |
| 10%      | 0.0018512862734496593 | 27.32526397705078 | 
| 20%      | 0.002360109006986022 | 26.270679473876953 | 
| 30%      | 0.0023435333278030157 | 26.301288604736328 | 
| 40%      | 0.002807890996336937 | 25.516197204589844 | 
| 50%      | 0.004794816952198744 | 23.192279815673828 | 
| 60%      | 0.009465990588068962 | 20.238340377807617 | 
| 70%      | 0.024813979864120483 | 16.053035736083984 | 
| 80%      | 0.06913217902183533 |  11.603198051452637 | 
| 90%      | 0.1364450454711914 | 8.650422096252441 | 
