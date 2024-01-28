#include <stdio.h>



int main(void) {
    
    float eps = 1.0;
    int counter = 0;
    for ( ; 1.0 + eps / 2.0 > 1.0; eps /= 2.0 ) {
        counter += 1;

    }
    printf("%d", counter);

}