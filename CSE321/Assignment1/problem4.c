#include <stdio.h>
#include <string.h>

int main(){
    char email[100];
    char domain[10];

    printf("Enter email: ");
    scanf("%s",email);

    strncpy(domain, &email[strlen(email) - 9], 9);
    domain[9] = '\0';

    if(strcmp(domain, "@kaaj.com") == 0){
        printf("Email address is outdated");
    }
    if(strcmp(domain, "sheba.xyz") == 0){
        printf("Email address is okay");
    }

    return 0;
}