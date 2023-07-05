#include <stdio.h>

int main(void){
	int arr[1001], n, k, cnt = 0;
	scanf("%d %d", &n, &k);
	
	for (int i = 0; i <= n; i++){
		arr[i] = 1;
	}
	
	for (int i = 2; i <= n; i++){
		if (arr[i] == 1){
			for (int j = i; j <= n; j += i){
				if (arr[j] == 1){
					cnt++;
					arr[j] = 0;
					if (cnt == k){
						printf("%d ", j);
						break;
					}
				}
			}
			if (cnt == k) break;
		}
	}
	
	return 0;
}