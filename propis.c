#include <stdio.h>
#include <stdlib.h>


char* digits[10] ={"null", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

void propis(double num) {
    char* buffer = malloc(sizeof(num) * 3);
    sprintf(buffer, "%f", num);
        
    char *p = buffer;
    for (char c = *p; c != '\0'; c = *++p) {
        if ( c == '.' ) {
            printf("%s ", "dot"); 
        }
        else {
            printf("%s ", digits[c - '0']);
        }

    }
}


int main(void) {
    double num;
    if (scanf("%lf", &num)) {
       propis(num);
    }
    return 0;
}