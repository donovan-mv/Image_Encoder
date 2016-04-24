from cv2 import *
import numpy as np
import types

def encode(img, fo='C:/Users/Desktop/foo.txt', key=11):
    #print type(img)
    try:
        img2=img.copy()
    except AttributeError as e:
        print "ERROR: Enter a valid file name"
        return img
    i=0
    j=0
    code=0
    ch=''
    key1=int(key/10)
    key2=key-int(key/10)*10
    with open(fo, 'r') as f:
        f.seek(0,0)
        while True:
            ch=f.read(1)
            #print type(ch)
            if type(ch) is types.StringType:
                if ch == '':
                    img2[j, i]=254
                    break
                #print ch
                code=ord(ch)
                img2[j,i]=code
                #print "{} {} {} {}".format(ch, code, j, i)
                i+=key1
                if i >= img2.shape[1]:
                    j+=key2
                    i=0
                if j >= img2.shape[0]:
                    print "ERROR: Image too small"
                    break
            else:
                print "Error reading chars from file"
                break
    return img2

def decode(img, out, key):
    try:
        img2=img.copy()
    except:
        print "ERROR: Enter a valid file name"
        return -1
    #imshow('img2', img2)
    i=0
    j=0
    key1=int(key/10)
    key2=key-int(key/10)*10
    #print out
    #print len(out)
    if len(out) != 0:
        with open(out, 'w') as dec:
            while j<img2.shape[0]:
                i=0
                while i<img2.shape[1]:
                    #print chr(img2[j,i])
                    #print dec.tell()
                    if img2[j, i] == 254:
                        j=img2.shape[1]
                        break
                    dec.write(chr(img2[j,i]))
                    i+=key1
                j+=key2
        return 0
    else:
        return -2

if __name__ == '__main__': #ensures that the following code is executed only if the module is run in entirety
    img=imread('C:/Users/Donovan/Pictures/blank.jpg',0)
    en=encode(img,'C:/Users/Donovan/Desktop/data.txt',34)
    imwrite('C:/Users/Donovan/Desktop/encode.png', en)
    print "encoding was successful"
    decode(imread('C:/Users/Donovan/Desktop/encode.png', -1),'C:/Users/Donovan/Desktop/decode.txt', 34)
    print "decoding was successful"
    imshow('Encoded image', en)
    waitKey(0)
    destroyAllWindows()



