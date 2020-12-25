# coding: utf-8

# In[ ]:


from __future__ import print_function

import sys
import numpy as np
from time import time
import matplotlib.pyplot as plt 
import math
from math import sqrt 
import random

sys.path.append('/home/xilinx')
from pynq import Overlay
from pynq import allocate

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/r09525049/histogram/histogram.bit")
    ip = ol.histogram_0

    numSamples = 5

    inBuffer0 = allocate(shape=(numSamples,), dtype=np.int32)
    inBuffera = allocate(shape=(10,), dtype=np.int32)
    inBufferb = allocate(shape=(10,), dtype=np.int32)
    inBuffer1 = allocate(shape=(numSamples,), dtype=np.int32)
    inBuffer2 = allocate(shape=(numSamples,), dtype=np.int32)
    inBuffer3 = allocate(shape=(numSamples,), dtype=np.int32)
    outBuffer = allocate(shape=(1,), dtype=np.float32)
    
    def ref (int a[10],int b[10], float out)
        float diff
        float diff2
        float acc;
        for i in range(10):
            diff = a[i] - b[i];
            diff2 = diff*diff
            acc+=diff2
        out = acc
          
    for i in range(5):
        inBuffer0[i] = i
        inBuffer1[i] = i+5
        inBuffer2[i] = i+10
        inBuffer3[i] = i+15
    for i in range(10):
        inBuffera[i] = i
        inBufferb[i] = i+10
    float out_r = 0.0
    ref(inBuffera,inBufferb,out_r)
    timeKernelStart = time()
    

    ip.write(0x10, inBuffer.device_address)
    ip.write(0x18, outBuffer.device_address)
    ip.write(0x00, 0x01)
    while (ip.read(0x00) & 0x4) == 0x0:
        continue
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
    for i in range(256):
        print("i = "+str(i) + " n = " + str(outBuffer[i]) + "\n")
        
    
    
      
        
    # In Jupyter, press Tab + Shift keys to show plot then redo run
    


    print("============================")
    print("Exit process")