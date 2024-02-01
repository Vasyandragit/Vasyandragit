#include <stdio.h>
#include <string.h>


void arr_swap(char arr1[], char arr2[]) {
    
    char temp[20];
    strcpy(temp, arr2);
    strcpy(arr2, arr1);
    strcpy(arr1, temp);
    
}

int main(void) {
    char u1[20], u2[20];
    scanf("%s %s", &u1, &u2);
    if (strlen(u2) < strlen(u1)) {
        arr_swap(u1, u2);
    }

    while ( strlen(u1) < strlen(u2) ) {
        u1[strlen(u1)] = ' ';
    }
    
    if ( strcmp(u1, u2) < 0 ) {
        printf("%s %s", u1, u2);
    }
    else {
        printf("%s %s", u2, u1);
    }

}   