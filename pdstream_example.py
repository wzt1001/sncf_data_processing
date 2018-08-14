import os
import sys
import gzip
import struct
import numpy as np
import zlib

def pbstreamreader(posefile):
    print "Reading .pbstream data"
    idnumber = '0x7b1d1f7b5bf501db'
    filehandle = open(posefile, 'rb')
    # make sure the data 
    size = readthefile(filehandle)
    if idnumber!= size:
        print "unknown string"
        return         
        
    #get the total size of the data 
    size = readthefile(filehandle)
    print int(size,0)
    
    compressed_trajectory_data = readdatafromfile(filehandle,int(size,0))
    
    trajectory_data = zlib.decompress(compressed_trajectory_data,16+zlib.MAX_WBITS)
    
    # read the entire data of the file 
    data = struct.unpack_from('b',trajectory_data)
    print data
    
    
    
    filehandle.close()

def readthefile(fileobj):
    size =0
    byte=None
    word = []
    for i in range(0,8):
        byte = fileobj.read(1).encode("hex")
        word.append(byte)
    word = word[::-1]          
    word = '0x'+''.join(word)
    return word

def readdatafromfile(fileobj, size):
    return fileobj.read(size)

    
    
def main():
    if len(sys.argv)!=2:
        print "Incorrect usage. generateassetsfrombag.py <path/to/the/*.pbstream>"
        return
    pbstreamreader(sys.argv[1])
      
    
if __name__=='__main__':
    main()
