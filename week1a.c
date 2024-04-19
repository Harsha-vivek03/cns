#include <stdio.h>
#include <stdlib.h>
int main() {
    char str[100];  // Assuming a maximum length of 100 characters
    printf("Enter a string: ");
    scanf("%s",&str);
    printf("Original String: %s", str);
    for (int i = 0; str[i] != '\0'; ++i) {
        str[i] = str[i] ^ 0;
        printf("\n%d",str[i]);
    }
    printf("XOR Result: %s", str);
    return 0;
}
