#include <stdio.h>
#include <stdlib.h>
int main() {
    char str[100];  // Assuming a maximum length of 100 characters
    printf("Enter a string: ");
        fgets(str, sizeof(str), stdin);
    printf("Original String: %s", str);
    // AND each character with 127
     printf("\nAnd\n");
    for (int i = 0; str[i] != '\0'; ++i) {
        str[i] = str[i] & 127;
        printf("\n%d",str[i]);
    }
     printf("\nAnd Result: %s", str);

// AND each character with 127
 printf("\nOR\n");
    for (int i = 0; str[i] != '\0'; ++i) {
        str[i] = str[i] | 127;
        printf("\n%d",str[i]);
    }
     printf("\nOR Result: %s", str);

    // XOR each character with 127
     printf("\nXOR\n");
    for (int i = 0; str[i] != '\0'; ++i) {
        str[i] = str[i] ^ 127;
         printf("\n%d",str[i]);
    }
    printf("\nXOR Result: %s", str);
    return 0;
}
