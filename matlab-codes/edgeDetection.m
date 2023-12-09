%% Edge detection

I=imread('D:\NSTU\DIP-materials\lab-programs\image\saturn.png');
I=rgb2gray(I);

sEdge=edge(I,'sobel');
prEdge=edge(I,'prewitt');
roEdge=edge(I,'roberts');

subplot(2,2,1);
imshow(I);
title('Original Image');

subplot(2,2,2);
imshow(sEdge);
title('Sobel');

subplot(2,2,3);
imshow(prEdge);
title('Prewitt');

subplot(2,2,4);
imshow(roEdge);
title('Roberts');

