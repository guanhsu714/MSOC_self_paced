#define SIZE 8
typedef int BaseType;

void matrix_vector(BaseType M[SIZE][SIZE], BaseType V_In[SIZE], BaseType V_Out[SIZE]) {
#pragma HLS array_partition variable=M dim=2 cyclic factor=2
#pragma HLS array_partition variable=V_In cyclic factor=2
	BaseType i, j;
data_loop:
	for (i = 0; i < SIZE; i++) {
//#pragma HLS unroll factor=2
#pragma HLS PIPELINE II=1
		BaseType sum = 0;
	dot_product_loop:

		for (j = 0; j < SIZE; j++) {
//#pragma HLS PIPELINE II=1
#pragma HLS unroll factor=2
			sum += V_In[j] * M[i][j];
		}
		V_Out[i] = sum;
	}
}
