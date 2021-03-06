import math
import binascii
import os
from itertools import islice

def hex2dec(hexVal):
    decVal = int(hexVal, 16)
    return decVal

def encode_line(line, mb):   # mb is the message bit
    decLine = hex2dec(line)
    if decLine % 2 != int(mb) and mb == '0':
        encDecLine = decLine - 1
    elif decLine % 2 != int(mb) and mb == '1':
        encDecLine = decLine + 1
    else:
        encDecLine = decLine
    return hex(encDecLine)[2:]
    
def embed_msg_len(msg):
    mLenBin = bin(len(msg))[2:].xfill(4)
    
    
etxVal = "00000011"         # This is the value to know when the end of the message is.
message = input("Enter the message to encode: ").encode()
msgLenBin = bin(len(message))[2:].zfill(4)
binMessage = bin(int(binascii.hexlify(message), 16))[2:].zfill(len(message)*8)
fileName = input("Enter the file name: ").encode()
inputFile = open(fileName, 'r')
outputFile = open('EncodedImg.txt', 'w')
with inputFile as inf:
    with outputFile as opf:
        i = 0
        j = 0
        opf.write(inf.readline())
        for line in islice(inf, 1, None):
            if i < 4:      # The first 4 blue values encoded will be the binary representation of the message length.
                encodedLine = encode_line(line, msgLenBin[i])
                opf.write(encodedLine + "\n")
                i += 1
            elif j < len(message) * 8:
                encodedLine = encode_line(line, binMessage[j])
                opf.write(encodedLine + "\n")
                j += 1
            else:
                opf.write(line)
                 
inputFile.close()
outputFile.close()
