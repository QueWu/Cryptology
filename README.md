# Cryptology
Chaos based cryptographic excersise.

A:
It is required to design a Hash function which generates a 16-bit key from a PIN
composed of 4 integers. Using a quadratic linear congruential random number generator
and a Merseene prime number of 2^31-1, write a function that outputs the key using
pseudo- or real-code of your choice.

B:
Use the above hash function to write another function which generates a cipher of length
N using the Blum-Blum-Shub generator for a Blum Integer BI using pseudo- or real-code
of your choice.

C:
Design a function using pseudo- or real-code of your choice to generate a Matthews
cipher for r = 4 which inputs the size of the array n (type: integer) required and the key
x_0 (type: integer) and outputs a stream of numbers of type float.

D:
Inspect the output of Matthews function and compute the Lyapunov dimension for different
keys x0_2 is (0,1) using an appropriate function.

E:
Design a function using pseudo- or real-code of your choice that reads a plaintext
file (in binary) specified during run-time, encrypts the input using function Cipher and
outputs the ciphertext to a file (in binary) specified during run time using the Matthew
cipher.

F:
Design a function that reads a ciphertext file (in binary) specified during run-time
and outputs the plaintext to a file (in binary) specified during run time.

G:
Re-engineer the software to produce a single program that can both encrypt and
decrypt using an appropriate switch (option).

H:
"Invent" three chaotic ciphers using a programming language of your choice. In each case:
-   compute the Lyapunov exponent;
-   observe the histogram of the output from the cipher and post-process the algorithm
     so that it is uniformly distributed to give a maximum entropy cipher;
-   compare the Information Entropy of the post-processed cipher with the original cipher;
-   estimate the cycle length of the maximum entropy cipher.

I:
Design a Steganography function 'watermark' using a coding language of your choice 
to watermark a grey-level image with another binary image based on the method proposed. 
