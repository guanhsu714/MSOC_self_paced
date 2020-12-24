#include "histogram.h"


void histogram(int in[INPUT_SIZE], int hist[VALUE_SIZE]) {
  int a = 0;
  int o = in[0];
  int val;
  #pragma HLS DEPENDENCE variable=hist intra RAW false
  for(int i = 0; i < INPUT_SIZE; i++) {
    #pragma HLS PIPELINE II=2
   /* val = in[i];
    hist[val] = hist[val] + 1;*/
	val = in[i];
	if(o == val) {
      a = a + 1;
    } else {
      hist[o] = a;
      a = hist[o] + 1;
    }
    o = val;
  }
  hist[o] = a;
}
