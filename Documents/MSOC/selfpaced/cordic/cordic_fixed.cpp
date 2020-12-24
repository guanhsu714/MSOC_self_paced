// The file cordic.h holds definitions for the data types and constant values
#include "cordic.h"

// The cordic_phase array holds the angle for the current rotation
// cordic_phase[0] =~ 0.785
// cordic_phase[1] =~ 0.463



void cordic(volatile float* theta, volatile float* s,volatile float* c)
{
/*#pragma HLS INTERFACE axis register both port=theta
#pragma HLS INTERFACE axis register both port=s
#pragma HLS INTERFACE axis register both port=c
#pragma HLS INTERFACE s_axilite port=return
*/
	/*THETA_TYPE theta_tmp;
	COS_SIN_TYPE s_tmp;
	COS_SIN_TYPE c_tmp;*/

	THETA_TYPE theta_t;

	intfp theta_conv, out_s, out_c;
	//theta_tmp = theta ->read();

for(int i=0;i<N;i++){
	//theta_conv.data = theta[i];
	//theta_t = theta_conv.f;
	theta_t = theta[i];
	COS_SIN_TYPE current_cos = 0.60735;
	COS_SIN_TYPE current_sin = 0.0;


  for (int j = 0; j < NUM_ITERATIONS; j++) {
#pragma HLS pipeline II=1

      COS_SIN_TYPE cos_shift = current_cos >> j;
      COS_SIN_TYPE sin_shift = current_sin >> j;

    if(theta_t >= 0) {
        current_cos = current_cos - sin_shift;
        current_sin = current_sin + cos_shift;

        theta_t =  theta_t - cordic_phase[j];
    } else {
        current_cos = current_cos + sin_shift;
        current_sin = current_sin - cos_shift;

        theta_t =  theta_t + cordic_phase[j];
    }
  }
  //out_s.f = current_sin;
  //out_c.f = current_cos;
 /* s_tmp.data = out_s.data;
  c_tmp.data = out_c.data;

	s_tmp.last = 1;
	c_tmp.last = 1;*/


  //s = current_sin;  c = current_cos;
  /*s->write(s_tmp);
  c->write(c_tmp);*/
  //s[i] = out_s.data;
  //c[i] = out_c.data;
  s[i] = current_sin;
  c[i] = current_cos;

}
return;
}
