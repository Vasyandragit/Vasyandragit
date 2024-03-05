#include <stdio.h>
#include <stdlib.h>


char* digits[10] ={"null", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

/*char* propis(double num) {
    char* buffer = malloc(sizeof(char) * 33);
    printf("%s", num, buffer);
    printf("%s", buffer);
}*/


int main(void) {
    double num;
    if (scanf("%lf", &num)) {
        char* buffer = malloc(sizeof(char) * 33);
        sprintf(buffer, "%f", num);
        
        char *p = buffer;
        for (char c = *p; c != '\0'; c = *++p) {
            
            if ( c == '.' ) {
                printf("%s ", "dot"); 
            }
            else {
                printf("%s ", digits[(int)c]);
            }

        }
    }
    return 0;
}