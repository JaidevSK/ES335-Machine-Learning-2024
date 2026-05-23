# Image Reconstruction- Here, ground truth pixel values are missing for particular regions within the image- you don't have access to them.

## Below is the sample picture we are using in the entire assignment.
![image1](dog.jpg)
## Below is the cropped image of the original image.
![image](crop.png)

We ran nested cross validation to obtain an ideal value of r from 2 to 100 and the suitable value of the rank (r) was found to be 92. Then, we performed the required task of reconstructing the missing portion by applying Gradient Descent till convergence with a tolerance as 1e-5. 

## Description of the Gradient Descent Algorithm: 
The model processes a batch of data, computes the loss, backpropagates to compute gradients, and then updates the model parameters using an optimizer. This process is repeated for multiple iterations (epochs) to train the model, or untill convergence.

## Case 1: A rectangular block of 30X30 is assumed missing from the image.

Metrics - RMSE and PSNR
![Q5_Gradient_Descent_RMSE_loss](rmseVSps_GD.png)
![Q5_Gradient_Descent_PSNR](psnr_rect.png)

## Reconstructed Images:

Required plots (selected regions, original and reconstructed images)
![image](20_rect.png)
![image1](30_rect.png)
![image1](40_rect.png)
![image1](60_rect.png)
![image1](80_rect.png)

## Case 2: A random subset of 900 (30X30) pixels is missing from the image.

Metrics - RMSE and PSNR
![img](rmse_random.png)
![img](psnr_random.png)

## Reconstructed Images:

Required plots (selected regions, original and reconstructed images)
![image](20_rand.png)
![image1](30_rand.png)
![image1](40_rand.png)
![image1](60_rand.png)
![image1](80_rand.png)



## Observations: 
For N = 30, the RMSE is almost same for the case when a rectangular patch of pixels is missing and the case where a random subset of points are missing. This is despite the fact that the reconstructed image for the former seems poorer than the latter. The probable reasons are that only a small patch of pixels differ between the two images, and that since the pixel values are normalised between 0-1, the potential range of pixel differences is relatively small.
However, as the number of missing points are increased from 900->1600->3600->6400, the RMSE significantly rises (almost doubles between N = 30 and N = 80) when the missing pixels are part of a rectangular patch. On the other hand, the RMSE remains almost constant as N is increased, in the case where a random subset of points are missing.
This suggests that for the same rank, ease of reconstuction is much higher for randomly missing points, compared to when they are all part of a same patch.
The PSNR for N = 30, for both the cases at N = 30 is around 29dB, indicating reasonable reconstruction or compression quality.
As N is increased, for rectangular missing patches, it falls from 29dB to 23dB, while for random missing points, it remains in the 29db range.


## Reconstruction using RFF + Linear regression:

### Reconstructed Images:

![img1](1.jpeg)
![img1](random_recon_rff.png)

Metrics - RMSE and PSNR
![img1](mse_rfff_nr.png)
![img1](psnr_rfff_nr.png)

# Comparison between RFF + Linear Regression and Gradient Descent:

The quality of the image reconstructed via gradient descent is significantly better than using random fourier features. Linear regression with random Fourier features is inherently a linear model. The effectiveness of linear regression with random Fourier features depends on the choice of features. It may be the that the random features are not adequately representing the structure of the data, and thus the inear regression model does not perform as well as the gradient descent model.

