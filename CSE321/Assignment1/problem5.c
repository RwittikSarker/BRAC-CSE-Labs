#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    char *start, *end;

    printf("Enter your input: ");
    scanf("%s", str);

    start = str;
    end = str + strlen(str) - 1;

    while (start < end) {
        if (*start != *end) {
            printf("Not Palindrome");
            return 0;
        }
        start++;
        end--;
    }

    printf("Palindrome");
    return 0;
}
