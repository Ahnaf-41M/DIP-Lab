%% Image Subtraction
%The colors in the image will be subtracted and produce a different Image
I=imread('D:\NSTU\DIP-materials\lab-programs\image\rice.png');

% figure,imshow(I); title('Original Image');
% background=imopen(I,strel('disk',15));
% imgSub=imsubtract(I,background);
% %imshow(imgSub,[]);
% figure,imshow(imgSub); title('Subtracted Image');

%% Subtract a constant value from an image

figure,imshow(I); title('Original Image');
imgSub=imsubtract(I,50);
figure,imshow(imgSub); title('Subtracted Image');

%% More related functions
%imabsdiff, imadd, imcomplement, imdivide, imlincomb, immultiply, ippl