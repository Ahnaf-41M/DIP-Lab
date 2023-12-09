%% Image read, display, size,resize and write functions

I=imread('D:\NSTU\DIP-materials\lab-programs\image\onion.png');
[r,c]=size(I);
figure
imshow(I);
title('Original Image')
%j=imresize(I,0.5);
j=imresize(I,[50,50]);
imwrite(j,'test.jpg');
figure
imshow(j);
title('Resized Image')
