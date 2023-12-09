%% Image Filtering (spatial)
I=imread('D:\NSTU\DIP-materials\lab-programs\image\pattern_blur.tif');
h=ones(3,3)/9; 
I2=imfilter(I,h); 
imshow(I); 
title('original image'); 
figure 
imshow(I2); 
title('filtered image');