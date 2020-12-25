#define SIZE 128
void prefixsum(int in[SIZE], int out[SIZE]) {
//#pragma HLS array_partition variable=out cyclic factor=4 dim=1
//#pragma HLS array_partition variable=in cyclic factor=4 dim=1
	int a;
   a = in[0];
  for(int i=1; i < SIZE; i++) {
//#pragma HLS UNROLL factor=4
#pragma HLS PIPELINE II=1
	  a = a + in[i];
	  out[i] = a;
  }
}
