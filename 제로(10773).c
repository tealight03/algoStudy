#include <stdio.h>

int main(void){
	int time, number[100000] = { 0 }, idx = 0;
	long long total = 0;
	scanf("%d", &time);
	
	for (int i = 0; i < time; i++){
		scanf("%d", &number[idx]);
		if (number[idx] == 0) {
			total -= number[--idx];
			continue;
		}
		total += number[idx];
		idx++;
	}
	printf("%lld\n", total);
	
	return 0;
}