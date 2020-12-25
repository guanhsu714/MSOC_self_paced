
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

    ol = Overlay("/home/xilinx/r09525049/cordic/design_1.bit")
    ipCordic = ol.cordic_0

    def abs_double(x):
        if x<0.0:
            return -x
    numSamples = 90

    inBuffer0 = allocate(shape=(numSamples,), dtype=np.float32)
    outBuffer0 = allocate(shape=(numSamples,), dtype=np.float32)
    outBuffer1 = allocate(shape=(numSamples,), dtype=np.float32)
    for i in range(1,numSamples):
        inBuffer0[i] = i*math.pi/180;

    timeKernelStart = time()
    
    #ipCordic.write(0x80, len(inBuffer0) * 4)
    ipCordic.write(0x10, inBuffer0.device_address)
    ipCordic.write(0x18, outBuffer0.device_address)
    ipCordic.write(0x20, outBuffer1.device_address)
    ipCordic.write(0x00, 0x01)
    while (ipCordic.read(0x00) & 0x4) == 0x0:
        continue
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
    Total_Error_Sin = 0.0
    Total_Error_Cos = 0.0
    error_sin = 0.0
    error_cos = 0.0
    zs = 0.0
    zc = 0.0
    for i in range(numSamples):
        zc = math.cos(inBuffer0[i])
        zs = math.sin(inBuffer0[i])
        #print(inBuffer0[i],outBuffer0[i],zs,outBuffer1[i],zc)
        error_sin =(outBuffer0[i]-zs)*(outBuffer0[i]-zs)
        error_cos =(outBuffer1[i]-zc)*(outBuffer1[i]-zc)
        Total_Error_Sin=Total_Error_Sin+error_sin
        Total_Error_Cos=Total_Error_Cos+error_cos
    Total_Error_Sin = sqrt(Total_Error_Sin/numSamples)
    Total_Error_Cos = sqrt(Total_Error_Cos/numSamples)
    # In Jupyter, press Tab + Shift keys to show plot then redo run
    print("Total_Error_Sin = "+str(Total_Error_Sin))
    print("Total_Error_Cos = "+str(Total_Error_Cos))

    print("============================")
    print("Exit process")

