#import random
#rng = random.Random()

#def LCG():
#    

def Hash(PIN):
    return ((2**31-1) * PIN + 7**5) % 2**16


print(Hash(6281))

#for i in range(50):
