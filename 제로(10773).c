#include <stdio.h>
#include <stdlib.h>

int main(void){
	int time, idx = 0;
	long long total = 0;
	scanf("%d", &time);
	
    int* number = (int*)calloc(time, sizeof(int));

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