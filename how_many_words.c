#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


int word_counter(char* word) {
    int8_t counter = 1;
    
    char* p = word;
    for (char c = *p; c != '\0'; *p++) {
        if ( c == ' ' ) {
            counter++;
        }
    }
    return counter;
}

int main(void) {
    char* word = malloc(sizeof(char*) * 1000);

    if ( scanf("%s", &word) ) {
        printf("%d", word_counter(word));
    }

}