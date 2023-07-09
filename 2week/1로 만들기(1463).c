#include <stdio.h>
#include <stdlib.h>

int main(void){
    int n, cnt = 0;
    scanf("%d", &n);

    int* dp = (int*)calloc(n+1, sizeof(int));

    for (int i = 2; i <= n; i++){
        int* list = (int*)calloc(3, sizeof(int)); cnt = 0;
        list[cnt] = dp[i-1];
        if (i % 3 == 0) list[++cnt] = dp[i/3];
        if (i % 2 == 0) list[++cnt] = dp[i/2];
        
        int min = list[0];
        for (int j = 1; j <= cnt; j++){
            if (min > list[j]) min = list[j];
        }

        dp[i] = min + 1;
    }

    printf("%d", dp[n]);

    return 0;
}