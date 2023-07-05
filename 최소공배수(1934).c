#include <stdio.h>

int gcd(int a, int b){
	while (b != 0){
		int remain = a % b;
		a = b;
		b = remain;
	}
	
	return a;
}

int main(void){
	int testcase, n1, n2, lcm;
	scanf("%d", &testcase);
	
	for (int i = 0; i < testcase; i++){
		scanf("%d %d", &n1, &n2);
		lcm = n1 * n2 / gcd(n1, n2);
		printf("%d\n", lcm);
	}
	
	return 0;
}