
project		-fft
reference	-pp4fpga
+code
|  	+---src							: This folder contains C++ design files and header file.
	|       fft.cpp
	|       fft.h
	|       fft_original.cpp
	|		cos_sin.h
	|
	+---tb							: This folder contains a C++ design file that serves as the test bench. 
	|       fft_tb.cpp
	|    
	+---python						: This folder contains python file for demo.
	|		fft.py
|
+impl
|	fft_csynth.rpt
|
+script
|	script.tcl
|
+testdata
|	out.fft.gold.dat
|