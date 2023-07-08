#include <stdio.h>
#include <stdlib.h>

int main(void){
	int n, max = 0;
	scanf("%d", &n);
	
	int* arr = (int*)calloc(n, sizeof(int));
	int* cnt = (int*)calloc(n, sizeof(int));
	
	for (int i = 0; i < n; i++){
		scanf("%d", &arr[i]);
	}
	
	for (int i = 0; i < n; i++){
		cnt[i] = 1;
		for (int j = 0; j <= i; j++){
			if (arr[i] > arr[j] && cnt[i] < cnt[j] + 1){
				cnt[i] = cnt[j]+1;
			}
		}
		if (cnt[i] > max) max = cnt[i];
	}

	printf("%d", max);
	
	return 0;
}