function watermark()
    clear;
    ratio = 0.01;
    seed = 2603;    %use the key as seed
    
    f1 = imread('host', 'bmp');
    f2 = imread('watermk', 'bmp');
    n = size(f1, 1);
    f1=im2double(f1); f1=1-f1; 
    f2=im2double(f2);

    subplot(2,3,1), imshow(f1);
    subplot(2,3,2), imshow(f2);
    
    rand('state',seed);
    p=rand(n,n);
    subplot(2,3,3), imshow(p);
    
    %Transform into Fourier space
    f=f1;
    f=fft2(f);
    p=fft2(p);
    pp=abs(p).^2;   %Compute the power spectrum
    
    for i=1:n
        for j=1:n
            temp=pp(i,j);
            if temp==0
            pp(i,j)=1;
            else
                pp(i,j)=pp(i,j);
            end
        end
    end
    
    f=p.*f./pp;
    
    %Inverse Fourier transform
    f=ifft2(f);
    f=real(f);      %Compute the real value
    f=f./max(max(f));       %Normalise the data
    
    %Display image in min/max range of array 
    subplot(2,3,4), imshow(f,[min(min(f)) max(max(f))]);
    f3=r*f+f2;      %Watermark image and display
    subplot(2,3,5), imshow(f3);
    
    %Recover watermark and normalise
    f4=f3-f2;
    f4=f4./max(max(f));
    f=f4;
    
    %Convert to Fourier space
    f=fft2(f);
    
    %Regenerate noise field
    seed=1234;
    rand('state',seed);
    p=rand(n,n);
    p=fft2(p);
    
    %Filter the data, inverse fft, take real part and normalise.
    f=conj(p).*f;
    f=ifft2(f);
    f=real(f);
    f=f./max(max(f));
    
    %Display reconstruction within min/max range of data
    subplot(2,3,6), imshow(f,[min(min(f)) max(max(f))]);
