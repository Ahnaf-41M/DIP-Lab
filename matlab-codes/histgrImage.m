%% Histogram of an image

I=imread('D:\NSTU\DIP-materials\lab-programs\image\onion.png');
I_gray=rgb2gray(I);
imhist(I_gray);
imhist(I_gray,128);
imhist(I_gray,32);

% R=I(:,:,1);
% %imhist(R);
% G=I(:,:,2);
% B=I(:,:,3);
% subplot(1,3,1),imhist(R),title(R);
% subplot(1,3,2),imhist(G),title(G);
% subplot(1,3,3),imhist(B),title(B);

%% Draw histogram of an image without using built-in function