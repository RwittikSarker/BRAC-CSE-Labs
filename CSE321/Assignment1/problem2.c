#include <stdio.h>
#include <string.h>

int main(){
    FILE *fptr1;
    FILE *fptr2;
    char read_string[100];

    fptr1 = fopen("with_spaces.txt", "r");
    fgets(read_string, 100, fptr1);
    fclose(fptr1);

    fptr2 = fopen("without_spaces.txt", "w");

    char* token = strtok(read_string, "  ");
    while (token != NULL) {
        fprintf(fptr2, token);
        fprintf(fptr2, " ");
        token = strtok(NULL, " ");
    }
    fclose(fptr2);

    return 0;
}