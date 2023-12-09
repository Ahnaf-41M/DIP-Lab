%% Log transformation: S=c*log(1+r)

  I=imread('D:\NSTU\DIP-materials\lab-programs\image\onion.png');
 
  figure,imshow(I); title('Original Image');
% Convert datatype to Double
% (for allowing fractional values)
  r = double(I);
 
% Constant determining the
% nature of the log curve
  C = 1;
 
% Performing log transformation
  S = C * log(1 + r);
  T = 255/(C * log(256));
 
% Converting the datatype back
% to integer for displaying
  B = uint8(T * S);
  figure,imshow(B); title('Log Transformation');
  