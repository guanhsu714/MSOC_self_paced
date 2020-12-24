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

    ol = Overlay("/home/xilinx/r09525049/fft/fft.bit")
    ip = ol.fft_0

    numSamples = 1024

    Buffer0 = allocate(shape=(numSamples,), dtype=np.float32)
    Buffer1 = allocate(shape=(numSamples,), dtype=np.float32)
    
    f = open("out.fft.dat", "w");
    
    
    
    
    
    for i in range(numSamples):
        Buffer0[i] = i
        Buffer1[i] = 0.0
    
    timeKernelStart = time()
    

    ip.write(0x10, Buffer0.device_address)
    ip.write(0x18, Buffer1.device_address)
    ip.write(0x00, 0x01)
    while (ip.read(0x00) & 0x4) == 0x0:
        continue
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
    for i in range(numSamples):
        f.write(str(i))
        f.write("\t")
        f.write(str(Buffer0[i]))
        f.write("\t")
        f.write(str(Buffer1[i]))
        f.write("\n")
        #f.write(str(i))
    
    #error = 0
    f.close() 
      
        
    # In Jupyter, press Tab + Shift keys to show plot then redo run
    #print("Total_Error = "+str(error))


    print("============================")
    print("Exit process")