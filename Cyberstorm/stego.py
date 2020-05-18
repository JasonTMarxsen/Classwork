######################################################################
# Name: Jason Marxsen
# Date: 5/8/2020
# Description: Program that does a lot of Stegonography in Python 3
######################################################################
from sys import stdin, stdout, argv

SENTINEL = bytearray(b'\x00\xff\x00\x00\xff\x00')

def storBit():
    off = argv[3][2:]
    if(argv[4][1] == "i"):
        interval = argv[4][2:]
        if(argv[5][1] == "w"):        
            stegg = argv[5][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[5]))
        if(argv[6][1] == "h"):
            message = argv[6][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[6]))
    else:
        interval = 1
        if(argv[4][1] == "w"):
            stegg = argv[4][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[4]))
        if(argv[5][1] == "h"):
            message = argv[5][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[5]))
        

    #actual storage
    wrapS = open(stegg, 'rb')
    wrapB = wrapS.read()
    wrapB = bytearray(wrapB)

    h = open(message, 'rb')
    hB = h.read()
    hB = bytearray(hB)

    off = int(off)
    interval = int(interval)

    i = 0
    while(i<len(hB)):
        for j in range(8):
            W[off] &= 0b11111110
            W[off] |= ((hB[i] & 0b10000000)>>7)
            hB[i] << 1 & 0xff
            offset+=interval

    j=0

    while(j<len(SENTINEL)):
        for j in range(8):
            W[off] &= 0b11111110
            W[off] |= ((SENTINEL[i] & 0b10000000)>>7)
            SENTINEL[i] << 1 & 0xff
            offset+=interval
        

    stdout.buffer.write(wrapB)

def storByte():
    off = argv[3][2:]
    if(argv[4][1] == "i"):
        interval = argv[4][2:]
        if(argv[5][1] == "w"):        
            stegg = argv[5][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[5]))
        if(argv[6][1] == "h"):
            message = argv[6][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[6]))
    else:
        interval = 1
        if(argv[4][1] == "w"):
            stegg = argv[4][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[4]))
        if(argv[5][1] == "h"):
            message = argv[5][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[5]))

    #actual storage
    wrapS = open(stegg, 'rb')
    wrapB = wrapS.read()
    wrapB = bytearray(wrapB)

    h = open(message, 'rb')
    hB = h.read()
    hB = bytearray(hB)

    off = int(off)
    interval = int(interval)

    i = 0
    while(i<len(hB)):
        wrapB[off] = hB[i]
        off+=interval
        i+=1

    j=0

    while(j<len(SENTINEL)):
        wrapB[off] = SENTINEL[j]
        off+=interval
        j+=1
        

    stdout.buffer.write(wrapB)
    

def retBit():
    off = argv[3][2:]
    if(argv[4][1] == "i"):
        interval = argv[4][2:]
        if(argv[5][1] == "w"):        
            stegg = argv[5][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[5]))
    else:
        interval = 1
        if(argv[4][1] == "w"):
            stegg = argv[4][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[4]))
    
    #actual retrieval
    wrap = open(stegg, 'rb')
    wrapB = wrap.read()
    wrap.close()
    wrapB = bytearray(wrapB)

    off = int(off)
    interval = int(interval)

    h = bytearray()

    while(off<len(wrapB)):
        b = 0
        for j in range(8):
            b |=(wrapB[off] & 0x01)
            if(j<7):
                b = b << 1 & 0xff
                off+=interval
        h.append(b)
        if(len(h)>=7):
            check = h[-6:]
            if(check==SENTINEL):
                #print("Sentinel found at Byte {}".format(off))
                h = h[:-6]   
                break           
        off+=interval
    stdout.buffer.write(h)
    
    

def retByte():
    off = argv[3][2:]
    if(argv[4][1] == "i"):
        interval = argv[4][2:]
        if(argv[5][1] == "w"):        
            stegg = argv[5][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[5]))
    else:
        interval = 1
        if(argv[4][1] == "w"):
            stegg = argv[4][2:]
        else:  
            raise ValueError("Invalid argument {}".format(argv[4]))

    #actual retrieval
    wrap = open(stegg, 'rb')
    wrapB = wrap.read()
    wrap.close()
    wrapB = bytearray(wrapB)

    off = int(off)
    interval = int(interval)

    h = bytearray()

    while(off<len(wrapB)):
        h.append(wrapB[off])
        if(len(h)>=7):
            check = h[-6:]
            if(check==SENTINEL):
                #print("Sentinel found at Byte {}".format(off))
                h = h[:-6]   
                break           
        off+=interval
    stdout.buffer.write(h)
    
    

def procedureDecider():
    if(argv[1][1] == "s"):

        if(argv[2][1] == "b"):
            storBit()

        elif(argv[2][1] == "B"):
            storByte()
        else:    
            raise ValueError("Invalid argument {}".format(argv[2]))

    elif(argv[1][1] == "r"):

        if(argv[2][1] == "b"):
            retBit()

        elif(argv[2][1] == "B"):
            retByte()
        else:
            raise ValueError("Invalid argument: {}".format(argv[2]))
    else:
        raise ValueError("Invalid argument {}".format(argv[1]))

failure = False

for i in argv:
    if(len(i)<2):
        print("Invalid Arguments found: {}".format(i))
        failure = True
        break

if(failure == False):
    procedureDecider()
