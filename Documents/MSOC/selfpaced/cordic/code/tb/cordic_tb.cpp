/*
This is traditional CORDIC computation of sine and cosine.
The current code is based on [FXT: cordic-circ-demo.cc]
Correctly calculates cos and sine between 0-90 degrees (0-100).
INPUT:
	double theta: Input angle 
	long n: Number of iterations. 
OUTPUT:
	double &s: Reference to the sine part
	double &c: Reference to the cos part 
	error_sin= [abs(s-zs)/zs]*100;
	error_cos= [abs(c-zc)/zc]*100;
	Total_Error_Sin = sum(error_sin)
	Total_error_Cos = sum(error_cos)
*/
#include <math.h>
#include "cordic.h"
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;
//#define M_PI 3.1415926536897932384626

double abs_double(double var){
	if ( var < 0)
	var = -var;
	return var;


}
int main(int argc, char **argv)
{	

	//stream_t radian, c, s;
    FILE *fp;
    //value_t radian_data;
    COS_SIN_TYPE c_data, s_data;
    intfp rad_conv, c_conv, s_conv;
	//COS_SIN_TYPE s;			//sine
	//COS_SIN_TYPE c;			//cos
	//THETA_TYPE radian; 		//radian versuin of degree
    /*int32_t s[90];
    int32_t c[90];
    int32_t radian[90];*/
    float s[90];
    float c[90];
    float radian[90];
	//zs=sin, zc=cos using math.h in VivadoHLS
	double zs, zc; 			// sine and cos values calculated from math.

	//Error checking
	double Total_Error_Sin=0.0;
	double Total_error_Cos=0.0;
	double error_sin=0.0, error_cos=0.0;

	fp=fopen("out.dat","w");
	/*radian_data.data = 0;
	radian_data.keep = 0xF;
	radian_data.strb = 0;
	radian_data.user = 0;
	radian_data.last = 1;
	radian_data.id = 0;
	radian_data.dest = 0;*/
	for(int i=1;i<NUM_DEGREE;i++) {
		//rad_conv.f = (float)i*M_PI/180;
		//radian[i] = rad_conv.data;
		radian[i] = (float)i*M_PI/180;
	}


	cordic(radian, s, c);
	for(int i=1;i<NUM_DEGREE;i++) {

			/*radian_data.data = rad_conv.data;
			radian.write(radian_data);*/


			zs = sin((double)(i*M_PI/180));
			zc = cos((double)(i*M_PI/180));
			/*c_conv.data = c[i];
			s_conv.data = s[i];
			c_data = c_conv.f;
			s_data = s_conv.f;*/
			error_sin=(abs_double((double)s[i]-zs)/zs)*100.0;
			error_cos=(abs_double((double)c[i]-zc)/zc)*100.0;
			Total_Error_Sin=Total_Error_Sin+error_sin;
			Total_error_Cos=Total_error_Cos+error_cos;

			printf("degree=%d, radian=%f, cos=%f, sin=%f\n", i, radian[i],c[i], s[i]);
	}

	fclose(fp);

	printf ("Total_Error_Sin=%f, Total_error_Cos=%f, \n", Total_Error_Sin, Total_error_Cos);
	return 0;
}
