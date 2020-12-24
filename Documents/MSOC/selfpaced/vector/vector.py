
# coding: utf-8

# In[ ]:


from __future__ import print_function

import sys
import numpy as np
from time import time
import matplotlib.pyplot as plt 
import math
from math import sqrt 

sys.path.append('/home/xilinx')
from pynq import Overlay
from pynq import allocate

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/r09525049/vector/matrix_vector.bit")
    ip = ol.matrix_vector_0

    numSamples = 8

    inBuffer0 = allocate(shape=(numSamples,numSamples/2), dtype=np.int32)
    inBuffer1 = allocate(shape=(numSamples,numSamples/2), dtype=np.int32)
    inBuffer2 = allocate(shape=(numSamples/2,), dtype=np.int32)
    inBuffer3 = allocate(shape=(numSamples/2,), dtype=np.int32)
    outBuffer0 = allocate(shape=(numSamples,), dtype=np.int32)
    gold_M = allocate(shape=(numSamples,numSamples), dtype=np.int32)
    gold_V = allocate(shape=(numSamples,), dtype=np.int32)
    
    
    inBuffer2 = [0,2,4,6]
    inBuffer3 = [1,3,5,7]
    
    for i in range(numSamples):
        for j in range(numSamples/2):
            inBuffer0[i,j] = i+2*j
            inBuffer1[i,j] = i+2*j+1
    
    for i in range(numSamples):
        gold_V[i] = i
        for j in range(numSamples):
            gold_M[i,j] = i+j
    for i in range(numSamples):
        sum = 0
        for j in range(numSamples):
            sum+=gold_V[j]*gold_M[i,j]
        gold[i] = sum
    timeKernelStart = time()
    

    ip.write(0x10, inBuffer0.device_address)
    ip.write(0x18, inBuffer1.device_address)
    ip.write(0x20, inBuffer2.device_address)
    ip.write(0x28, inBuffer3.device_address)
    ip.write(0x30, outBuffer0.device_address)
    ip.write(0x00, 0x01)
    while (ip.read(0x00) & 0x4) == 0x0:
        continue
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
    gold = allocate(shape=(numSamples,), dtype=np.int32)
    error = 0
    for i in range(numSamples):
        if gold[i]!=outBuffer0[i]:
            error += 1
        
      
        
    # In Jupyter, press Tab + Shift keys to show plot then redo run
    print("Total_Error = "+str(error))


    print("============================")
    print("Exit process")

