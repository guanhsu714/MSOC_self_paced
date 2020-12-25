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

    ol = Overlay("/home/xilinx/r09525049/prefixsum/prefixsum.bit")
    ip = ol.prefixsum_0

    numSamples = 128

    inBuffer = allocate(shape=(numSamples,), dtype=np.int32)
    outBuffer = allocate(shape=(numSamples,), dtype=np.int32)
    
   
    
    
    
    
    for i in range(numSamples):
        inBuffer[i] = i
    
    timeKernelStart = time()
    

    ip.write(0x10, inBuffer.device_address)
    ip.write(0x18, outBuffer.device_address)
    ip.write(0x00, 0x01)
    while (ip.read(0x00) & 0x4) == 0x0:
        continue
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
    for i in range(numSamples):
        print(str(i) + " = " + str(outBuffer[i]) + "\n")
        
    
    
      
        
    # In Jupyter, press Tab + Shift keys to show plot then redo run
    


    print("============================")
    print("Exit process")