#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
	int i, n,seed;
	int count;
	srand(time(NULL));
	printf("\n%s\n%s",
		"Some randomly distributed integers will be printed.",
		"How many do you want to See? ");
	scanf("%d", &n);
	count = 0;
	while(1){
		count++;
		printf("%12d", rand());
		if (count == n) break;
		if(count % 5 != 0) continue;
		putchar('\n');
	}
	printf("\n\n");
	return 0;
}
