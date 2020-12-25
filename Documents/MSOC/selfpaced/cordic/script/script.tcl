############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 1986-2019 Xilinx, Inc. All Rights Reserved.
############################################################
open_project cordic_fixed
set_top cordic
add_files cordic.h
add_files cordic.cpp
add_files -tb cordic_tb.cpp
open_solution "solution1"
set_part {xc7z020-clg484-1} -tool vivado
create_clock -period 10 -name default
config_export -format ip_catalog -rtl verilog
source "./cordic_fixed/solution1/directives.tcl"
csim_design
csynth_design
cosim_design -tool riviera
export_design -rtl verilog -format ip_catalog
