%% Boundary extraction
I=imread('F:\lab-programs\image\kids.tif');
s=strel('disk', 2.0);
f=imerode(I,s);
subplot(2,1,1);
imshow(I);
title('Original Image');

subplot(2,1,2);
imshow(I-f);
title('Boundary extracted image');