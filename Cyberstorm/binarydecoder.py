#########################################
# Name: Jason Marxsen
# Date: 3/29/2020
# Description: Decrypts and Encrypts Binary
#########################################
DEBUG = 0
from sys import stdin

def decode(binary, n):
    decoded = ""
    i = 0
    if(n==7):
        while(i < len(binary)):
            bits = binary[i:i+n]
            bits = int(bits, 2)
            if(bits != 8): 
                bits = chr(bits)
                decoded+=bits
            else:
                decoded = decoded[:-1]
            i+=n
    elif(n==8):
        while(i < len(binary)):
            bits = binary[i:i+n]
            bits = int(bits, 2)
            if(bits != 8): 
                bits = chr(bits)
                decoded+=bits
            else:
                decoded = decoded[:-1]
            i+=n
    return decoded
    

#reads a line from input, then strips the new line from the beginning
binary = stdin.read().rstrip('/n')
decBin = ""
if(DEBUG == 1):
    print(binary)

if(len(binary)%7==0):
    print('7-bit ASCII:')
    decBin = decode(binary, 7)
elif(len(binary)%8==0):
    print('8-bit ASCII:')
    decBin = decode(binary, 8)
else:
    print("None of the above")
    print(len(binary))

print(decBin)



if(DEBUG == 1): 
    print(str(len(binary))+" bits long")
