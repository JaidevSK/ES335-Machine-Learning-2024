# Q5: Using ALS

## Image Reconstruction- Here, ground truth pixel values are missing for particular regions within the image- you don't have access to them

## Using Alternating Least Squares algorithm

### When a continous patch is missing
The following plots show the results obtained with Alternating Least Squares:
 #### When a patch of size 30x30 is missing:

 ![Original Image](Q5_original.png)

####  Results

![Q5_als_30](Q5_als_30.png)
In this case, we can see that the ALS method was able to reconstruct the original image from the given image with a 30x30 patch missing.

Similar procedure was done for patches of different sizes as given below:
<br><br>
Patch Size = 20x20
![Q5_als_20](Q5_als_20.png)

<br><br>
Patch Size = 40x40
![Q5_als_40](Q5_als_40.png)

<br><br>
Patch Size = 60x60
![Q5_als_60](Q5_als_60.png)

<br><br>
Patch Size = 80x80
![Q5_als_80](Q5_als_80.png)



### Plots

![als_psnr](Q5_als_psnr.png)
This plot describes the relation between the PSNR of the reconstructed image and the number of missing pixels in the ALS algorithm.

![als_rmse](Q5_als_rmse.png)
This plot describes the relation between the RMSE of the reconstructed image and the number of missing pixels in the ALS algorithm.

## When a random subset of pixels is missing

#### The count of randomly missing pixels is 30x30:

####  Results

![Q5_als_30r](Q5_als_30r.png)
In this case, we can see that the ALS method was able to reconstruct the original image from the given image with a random subset of 30x30 size of pixels missing.

Similar procedure was done for patches of different sizes as given below:
<br><br>
Size of random subset = 20x20
![Q5_als_20r](Q5_als_20r.png)

<br><br>
Size of random subset = 40x40
![Q5_als_40r](Q5_als_40r.png)

<br><br>
Size of random subset = 60x60
![Q5_als_60r](Q5_als_60r.png)

<br><br>
Size of random subset = 80x80
![Q5_als_80r](Q5_als_80r.png)



## Plots

![als_psnr](Q5_als_psnrr.png)
This plot describes the relation between the PSNR of the reconstructed image and the number of randomly missing pixels in the ALS algorithm.

![als_rmse](Q5_als_rmser.png)
This plot describes the relation between the RMSE of the reconstructed image and the number of randomly missing pixels in the ALS algorithm.

## Major Observation:
* One of the major observations is that the PSNR increases with a decrease in the patch size of pixels missing.
* This also implies that the MS or RMSE loss increases with an increase in the patch size of pixels missing.
* This trend can also be seen in the plots with random pixels missing: The PSNR increases with a decrease  in the number of missing pixels, while the RMSE increases with an increase in number of missing pixels.
* This can also be analysed visually, we can see this from the comparison between original and reconstructed image.
* Another major observation is that the PSNR values for the case when we have randomly missing pixels is much  higher than the one with an entire patch missing of same size.
* This observation is also supported from the plots of RMSE, which are much larger for continuous patches compared to randomly missing pixels.
