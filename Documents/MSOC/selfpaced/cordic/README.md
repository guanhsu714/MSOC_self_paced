
project		-cordic
reference	-pp4fpga
+code
|  	+---src							: This folder contains C++ design files and header file.
	|       cordic.cpp
	|       cordic.h
	|       cordic_original.cpp
	|
	+---tb							: This folder contains a C++ design file that serves as the test bench. 
	|       cordic_tb.cpp
	|    
	+---python						: This folder contains python file for demo.
	|		cordic.py
|
+impl
|	cordic_csynth.rpt
|
+script
|	script.tcl
|