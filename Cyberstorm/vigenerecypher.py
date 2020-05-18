###########################################################
# Name: Jason Marxsen
# Date: 3/29/2020
# Description: Encodes and Decodes in Viginere Cypher
###########################################################
from sys import stdin, argv
import string

listAlphaL = list(string.ascii_lowercase)
listAlphaU = list(string.ascii_uppercase)
listLetter = list(string.ascii_letters)

if(len(argv)<2):
    print("Must have a mode (-e or -d) and key in arguments to run program. Exiting.")
    print("Example: python vigenerecypher.py -e \"key\"")
    exit(1)

#Is it upper or lower?
def lowerUpper(letter):
    if(letter.isupper()):
        return 1
    return 0

#Number to Letter Functions
def letToNum(letter):
    number = 0
    global listAlphaU
    global listAlphaL
    for i in range(0,26):
        if(letter == listAlphaU[i]):
            number = i
            return number
        if(letter == listAlphaL[i]):
            number = i
            return number

def numToLet(number, upper):
    letter = ""
    global listAlphaU
    global listAlphaL

    if(upper == 1):
        letter = listAlphaU[number]
    elif(upper == 0):
        letter = listAlphaL[number]
    return letter
        

#Encoding and Decoding
def encode(text, key):
    finished = ""
    addNumber = 0
    i = 0
    global listLetter

    keyPlace = 0
    keyLength = len(key)
    
    while (i<len(text)):
        working = text[i]
        #print(working)

        if(working not in listLetter):
            finished+=working
            i+=1
        else:
            numWorking = letToNum(working)
            lowUp = lowerUpper(working)
            numKey = letToNum(key[keyPlace])

            modCharNum = numWorking + numKey
            if(modCharNum > 25):
                modCharNum-=26

            modChar = numToLet(modCharNum, lowUp)
            finished+=modChar
            if(keyPlace+1 == keyLength):
                keyPlace = 0
            else:
                if(key[keyPlace+1] not in listLetter):
                    while(key[keyPlace+1] not in listLetter):
                        keyPlace+=1
                keyPlace+=1
            i+=1
    return finished

def decode(text, key):
    finished = ""
    addNumber = 0
    i = 0
    global listLetter

    keyPlace = 0
    keyLength = len(key)
    
    while (i<len(text)):
        working = text[i]
        #print(working)

        if(working not in listLetter):
            finished+=working
            i+=1
        else:
            numWorking = letToNum(working)
            lowUp = lowerUpper(working)
            numKey = letToNum(key[keyPlace])

            modCharNum = numWorking - numKey
            if(modCharNum > 25):
                modCharNum+=26

            modChar = numToLet(modCharNum, lowUp)
            finished+=modChar
            if(keyPlace+1 == keyLength):
                keyPlace = 0
            else:
                if(key[keyPlace+1] not in listLetter):
                    while(key[keyPlace+1] not in listLetter):
                        keyPlace+=1
                keyPlace+=1
            i+=1
    return finished

#Main Code
style = argv[1]
key = argv[2]

normal = stdin.read().rstrip("\n")

if(style == "-e"):
    modified = encode(normal, key)
if(style == "-d"):
    modified = decode(normal, key)

print(modified)
