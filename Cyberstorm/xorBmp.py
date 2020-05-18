###############################################################################################
# Name: Jason Marxsen
# Date: 5/7/2020
# Description: Xor decryptor designed to decrypt by xoring two files of equal length (Python 3)
###############################################################################################
import sys

size = 1024
cur = 0

ki = 'key.bmp'
kif = open(ki,'rb')

while(1<2):
    translate = sys.stdin.buffer.read()
    translateb = bytearray(translate)

    keyCont = kif.read()
    keyLen = len(keyCont)

    keyPr = bytearray(keyCont)

    if(keyCont==b''):
        break

    keyL = []
    for key in keyPr:
        keyL.append(key)

    traL = []
    for item in translateb:
        traL.append(item)

    i = 0
    translator=bytearray() 
    while(i<len(traL)):
        if(i==len(keyL)):
            for key in keyPr:            
                keyL.append(key)
        comp = (traL[i] ^ keyL[i])
        translator.append(comp)
        i+=1

    cur+=4096

trans = bytes(translator)
#trans = trans.decode('latin-1')

sys.stdout.buffer.write(trans)
