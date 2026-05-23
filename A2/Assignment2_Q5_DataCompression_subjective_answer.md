# Q5. Data Compression

## Original Image:

![Original Image](Q5_dog.png)

## Patch with 1 colour

![onecol](Q5_col1.png)<br>
Original Patch with 1 colour
<br><br>
![col1_5](Q5_col1_5.png)<br>
Patch with 1 colour reconstructed from compression of r = 5
<br><br>
![col1_10](Q5_col1_10.png)<br>
Patch with 1 colour reconstructed from compression of r = 10
<br><br>
![col1_25](Q5_col1_25.png)<br>
Patch with 1 colour reconstructed from compression of r = 25
<br><br>
![col1_50](Q5_col1_50.png)<br>
Patch with 1 colour reconstructed from compression of r = 50
<br><br>
![col1_loss](Q5_col1_loss.png)<br>
The plot of the reconstruction loss against the rank r for patch with 1 colour
<br><br>
![col1_size](Q5_col1_size.png)<br>
The plot of the size of the space required to store the compressed image against the rank r for patch with 1 colour

## Patch with 2 colours

![twocol](Q5_col2.png)<br>
Original Patch with 2 colour
<br><br>
![col2_5](Q5_col2_5.png)<br>
Patch with 2 colour reconstructed from compression of r = 5
<br><br>
![col2_10](Q5_col2_10.png)<br>
Patch with 2 colour reconstructed from compression of r = 10
<br><br>
![col2_25](Q5_col2_25.png)<br>
Patch with 2 colour reconstructed from compression of r = 25
<br><br>
![col2_50](Q5_col2_50.png)<br>
Patch with 2 colour reconstructed from compression of r = 50
<br><br>
![col2_loss](Q5_col2_loss.png)<br>
The plot of the reconstruction loss against the rank r for patch with 2 colours
<br><br>
![col2_size](Q5_col2_size.png)<br>
The plot of the size of the space required to store the compressed image against the rank r for patch with 2 colours

## Patch with 5 colours

![onecol](Q5_col5.png)<br>
Original Patch with 5 colour
<br><br>
![col5_5](Q5_col5_5.png)<br>
Patch with 5 colour reconstructed from compression of r = 5
<br><br>
![col5_10](Q5_col5_10.png)<br>
Patch with 5 colour reconstructed from compression of r = 10
<br><br>
![col5_25](Q5_col5_25.png)<br>
Patch with 5 colour reconstructed from compression of r = 25
<br><br>
![col5_50](Q5_col5_50.png)<br>
Patch with 5 colour reconstructed from compression of r = 50
<br><br>
![col5_loss](Q5_col5_loss.png)<br>
The plot of the reconstruction loss against the rank r for patch with 5 colours
<br><br>
![col5_size](Q5_col5_size.png)<br>
The plot of the size of the space required to store the compressed image against the rank r for patch with 5 colours

## Observations

* A major observation is that the amount of space required to store the matrices corresponding to the compressed data increases with the value of 'r', as we can see from the plot.
* Another observation is that the loss of the reconstructed image decreases with an increase in the value of r.
* We can also see this from the visual inspection of the images and their quality. We can see that the quality of image improves with the increasing value of r.
* Another major observation is that for the same value of r, the value of loss increases with an increase in the number of colours in the patch; that is, for the part of the image with just one colour, the loss is lesser compared to the part of the image with 2 and 5 colours.



