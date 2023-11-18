#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	srand(time(NULL));

	int i = 0, flips = 0, randint;
	printf("How many times do you want to flip a coin? ");
	scanf("%d", &flips);
	FILE *data = fopen("data.txt", "w");

	while(i<flips){
		randint = rand() % 2;
		fprintf(data, "%d\n", randint);
        i++;
	}

	fclose(data);

	return 0;
}
