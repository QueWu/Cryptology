'''It is required to design a Hash function which generates a 16-bit key from a PIN
composed of 4 integers. Using a quadratic linear congruential random number generator
and a Merseene prime number of 2^31-1, write a function that outputs the key using
pseudo- or real-code of your choice'''

import random
rng = random.Random()

m = 2**31-1     # Merseene prime number
def LCG(seed):
    a = rng.randrange(2**16)
    b = rng.randrange(2**16)
    c = rng.randrange(2**16)
    randNo = (seed**a+b*seed+c) % m # Quadratic theme
    return randNo

def Hash(PIN):
    return (m * PIN + LCG(PIN)) % 2**16

'''Use the above hash function to write another function which generates a cipher of length
N using the Blum-Blum-Shub generator for a Blum Integer BI using pseudo- or real-code
of your choice.'''

def BBS(key, BI, N):
    bbsArr = []
    bbsArr.append(key)     # Use the key as the seed
    for i in range(N):
        bbsArr.append(bbsArr[i]**2 % BI)
    return bbsArr

'''Design a function using pseudo- or real-code of your choice to generate a Matthews
cipher for r = 4 which inputs the size of the array n (type: integer) required and the key
x_0 (type: integer) and outputs a stream of numbers of type float'''

def Matthews(n,key):
    cipher = []
    r = 4
    x = float(key)
    for i in range(n):
        x = x%10**6     # Wrap around
        x = (r+1)*(1.0/r+1)**r*x*(1-x)**r
        cipher.append(x)
    return cipher

'''Inspect the output of Matthews function and compute the Lyapunov dimension for different
keys x0_2 is (0,1) using an appropriate function.'''

import math
def LyapunovDim(cipher):
    sigmN = 0
    sigmM = 0
    for i in range(1,len(cipher)):
        sigmN = sigmN + math.log(math.fabs(cipher[i]/float(cipher[i-1])))
    sigmN = 1/len(cipher)*sigmN
    for i in range(1,len(cipher)-1):
        sigmM = sigmM + math.log(math.fabs(cipher[i]/float(cipher[i-1])))
    sigmM = 1/(len(cipher)-1)*sigmM

    if(sigmM > sigmN):
        dim = 1 - sigmN/sigmM
    else:
        dim = 1 - sigmM/sigmN
    return dim

import random
def inspect():
    randSeed = []
    for i in range(3):  # Generate three keys [0,1)
        randSeed.append(random.random())
    for i in range(len(randSeed)):
        mattCipher = Matthews(1000, randSeed[i])
        plotter(mattCipher)
        print(LyapunovDim(mattCipher))

'''Design a function using pseudo- or real-code of your choice that reads a plaintext
file (in binary) specified during run-time, encrypts the input using function Cipher and
outputs the ciphertext to a file (in binary) specified during run time using the Matthew
cipher'''

import struct
def Encrypt(key):
    import struct
    binTx = ''
    binCipher = ''
    binCipherTx = ''
    inFile = open("message.txt", 'r')
    inTx = inFile.read()
    inFile.close()

    cipher = Matthews(len(inTx), key)
    # Format the plaintext to 32bit binary
    for i in inTx:
        binTx += format(ord(i), '032b')
    # Format the cipher floating point number to 32bit binary
    for i in range(len(cipher)):
        binCipher += ''.join(bin(j).replace('0b', '').rjust(8, '0') for j in struct.pack('!f',  cipher[i]))
    binCipher = binCipher.strip()
    for i in range(len(binTx)):     #XOR operation equivilent
        binCipherTx += str(int(bool(int(binTx[i])) != bool(int(binCipher[i]))))

    outFile = open("encrypted.txt", 'w')
    outFile.write(binCipherTx)
    outFile.close()

'''Design a function that reads a ciphertext file (in binary) specified during run-time
and outputs the plaintext to a file (in binary) specified during run time'''

import struct
def Decrypt(key):
    import struct
    binTx = ''
    binCipher = ''
    inFile = open("encrypted.txt", 'r')
    inTx = inFile.read()
    inFile.close()

    cipher = Matthews(len(inTx), key)
    # Format the cipher floating point number to 32bit binary
    for i in range(len(cipher)):    
        binCipher += ''.join(bin(j).replace('0b', '').rjust(8, '0') for j in struct.pack('!f', cipher[i]))
    binCipher = binCipher.strip()
    for i in range(len(inTx)):     #XOR operation equivilent
        binTx += str(int(bool(int(inTx[i])) != bool(int(binCipher[i]))))
        
    outFile = open("decrypted.txt", 'w')
    outFile.write(binTx)
    outFile.close()
    
'''Re-engineer the software to produce a single program that can both encrypt and
decrypt using an appropriate switch (option)'''

def Encrypt_Decrypt(key, option):
    #option 0 for encrypt, 1 for decrypt
    import struct
    binTx = ''
    binCipher = ''
    binCipherTx = ''

    if(option == 0):
        inFile = open("message.txt", 'r')
        inTx = inFile.read()
        inFile.close()

        cipher = Matthews(len(inTx), key)
        for i in range(len(cipher)):    # Format the cipher floating point number to 32bit binary
            binCipher += ''.join(bin(j).replace('0b', '').rjust(8, '0') for j in struct.pack('!f', cipher[i]))
        binCipher = binCipher.strip()

        for i in inTx:      # Format the plaintext to 32bit binary
            binTx += format(ord(i), '032b')

        for i in range(len(binTx)):     #XOR operation equivilent
            binCipherTx += str(int(bool(int(binTx[i])) != bool(int(binCipher[i]))))
        outFile = open("encrypted.txt", 'w')
        outFile.write(binCipherTx)
        outFile.close()
    elif(option == 1):
        inFile = open("encrypted.txt", 'r')
        inTx = inFile.read()
        inFile.close()

        cipher = Matthews(len(inTx), key)
        for i in range(len(cipher)):    # Format the cipher floating point number to 32bit binary
            binCipher += ''.join(bin(j).replace('0b', '').rjust(8, '0') for j in struct.pack('!f', cipher[i]))
        binCipher = binCipher.strip()

        for i in range(len(inTx)):     #XOR operation equivilent
            binTx += str(int(bool(int(inTx[i])) != bool(int(binCipher[i]))))

        outFile = open("decrypted.txt", 'w')
        outFile.write(binTx)
        outFile.close()
    else:
        print("Invalid option, either 0 or 1")
    
''' "Invent" three chaotic ciphers using a programming language of your choice. In each case:
-   compute the Lyapunov exponent;
-   observe the histogram of the output from the cipher and post-process the algorithm
     so that it is uniformly distributed to give a maximum entropy cipher;
-   compare the Information Entropy of the post-processed cipher with the original cipher;
-   estimate the cycle length of the maximum entropy cipher.'''

''' "Template" mapping: x[n+1] = (r*x[n])*(1-x[n])
    Cipher 1: x[n+1] = (r*x[n])*(1-x[n]*(1+x[n]**2)/2)
    Cipher 2: x[n+1] = (r*x[n])*(1-x[n]/r*(1+log(1+x[n], 10)**2)/2)
    Cipher 3: x[n+1] = (r*x[n])*(1-x[n]/2*tan(x[n]/2)**2) '''

def LyapunovExp(inCipher):
    n = len(inCipher)
    exp = 0
    i = 1
    devArr = []
    for i in range(n):
        devArr.append(math.log(math.fabs((inCipher[i]-inCipher[i-1]))))
    exp = sum(devArr)/(n-1)
    return exp
    
def cycleEst(inCipher, inWindow): # window it with 16,32 and 64 etc
    import struct
    longStr = ''
    bitMap = {}     # Use a binary bit map and shift it (right)
    for i in range(len(inCipher)):
        newKey = ''.join(bin(j).replace('0b', '').rjust(inWindow//4, '0') for j in struct.pack('!f', cipher[i]))
        longStr += newKey
        bitMap[newKey] = 0
    for i in range(len(longStr)):
        window = longStr[i:i+inWindow]  # moving window
        if(window in bitMap):
            bitMap[window] = i-1
    return sum(bitMap.values())/len(bitMap.values()) # average performance

def infoEnpy(inCipher):
    pdf = plt.hist(inCipher)[0]
    tray = 0
    for i in range(len(pdf)):
        tray += pdf[i]*math.log(pdf[i],2)
    return tray

