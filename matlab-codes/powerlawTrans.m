%% Power law transformation: S=cr^gamma

  I=imread('D:\NSTU\DIP-materials\lab-programs\image\onion.png');
 
  figure,imshow(I); title('Original Image');
  % Convert datatype to Double
% (for allowing fractional values)
 r = double(I);
 
% The below value represents gamma
 G = 0.6;
 
% Applying the Power Law Transformation
 S = C * (r .^G);
 T = 255/(C * (255 .^G));
 
% Converting the datatype back
% to integer for displaying
 O = uint8(T * S);
 figure,imshow(O); title('Power Law Transformation');
 