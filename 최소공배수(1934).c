#include <stdio.h>

int gcd_count(int a, int b){
	while (b != 0){
		int remain = a % b;
		a = b;
		b = remain;
	}
	
	return a;
}

int main(void){
	int testcase, n1, n2, gcd, lcm;
	scanf("%d", &testcase);
	
	for (int i = 0; i < testcase; i++){
		scanf("%d %d", &n1, &n2);
		gcd = gcd_count(n1, n2);
		lcm = n1 * n2 / gcd;
		printf("%d\n", lcm);
	}
	
	return 0;
}