project		-matrixvector  
reference	-pp4fpga  
+code  
|  	+---src							: This folder contains C++ design files and header file.  
	|       matrixvector.cpp  
	|       matrixvector_original.cpp  
	|  
	+---tb							: This folder contains a C++ design file that serves as the test bench.   
	|       matrixvector_tb.cpp  
	|    
	+---python						: This folder contains python file for demo.  
	|		matrixvector.py  
|  
+impl  
|	matrixvector_csynth.rpt  
|  
+script  
|	script.tcl  
|  
+testdata  
|	out.matrix_vector.gold.dat  
|  