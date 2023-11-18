#include <stdio.h>


int main(){
    FILE *data = fopen("data.txt", "r");

    if(data == NULL){
        fprintf(stderr, "Unable to open the file.\n");
        return 1;
    }

    int heads = 0, tails = 0;
    int hstreak = 0, tstreak = 0; // Current Streak
    int hhstreak = 0, htstreak = 0; // Highest Streak


    int flip, size = 0;

    while((flip = fgetc(data)) != EOF){
        if(flip == '\n'){
        continue;
        }
        if(flip == 49){
            tails++;
            hstreak = 0;
            tstreak++;
            if(tstreak > htstreak){
                htstreak = tstreak;
            }
        } else{
            heads++;
            tstreak = 0;
            hstreak++;
            if(hstreak > hhstreak){
                hhstreak = hstreak;
            }
        }
        size++;
    }

    fclose(data);

    float hpercent = (float)heads / size * 100, tpercent = (float)tails / size * 100;

    printf("Number of times coin was flipped: %d\n", size);
    printf("Number of Heads: %d, Number of Tails: %d\n", heads, tails);
    printf("Percent if Heads: %.2f%, Percent of Tails %.2f%\n", hpercent, tpercent);
    printf("Highest consequtive Heads throws in a row: %d, "
    "Highest consequtive Tails throws in a row: %d\n", hhstreak, htstreak);

    return 0;
}
