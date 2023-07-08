#include <stdio.h>
#include <string.h>

int main(void){
	char vps[51];
	int time = 0, len;
	scanf("%d", &time);
	
	for (int i = 0; i < time; i++){
		int count = 0;
		scanf("%s", vps);
		len = strlen(vps);
		for (int j = 0; j < len; j++){
			if (count < 0) break; 
			if (vps[j] == '(') count++;
			else if (vps[j] == ')') count--;
		}
		if (count == 0) printf("YES\n");
		else printf("NO\n");
	}
	
	return 0;
}