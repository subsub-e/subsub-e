#include<stdio.h>
int main(){
	double eps = 1;
	int decimal_precision = 0;
	while(1){
		eps = eps / 10;
		if(eps == 0){
			printf("decimal precision: 10^(-%d)\n",
				decimal_precision);
			return 0;
		}
		decimal_precision++;
	}
}
