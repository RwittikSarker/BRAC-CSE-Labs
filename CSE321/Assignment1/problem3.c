#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

void check_password(char password[]){
    bool has_lowercase = false, has_uppercase = false, has_digit = false, has_special = false;
    char result[100] = "";

    for(int i=0; i<strlen(password); i++){
        if(islower(password[i])){
            has_lowercase = true;
        }
        else if(isupper(password[i])){
            has_uppercase = true;
        }
        else if(isdigit(password[i])){
            has_digit = true;
        }
        // _ , $, #, @
        else if(password[i] == '_' || password[i] == '$' || password[i] == '#' || password[i] == '@'){
            has_special = true;
        }
    }

    if(has_lowercase && has_uppercase && has_digit && has_special){
        printf("OK\n");
    }
    // Uppercase character missing, Digit missing, Special character missing
    else{
        if(!has_lowercase){
            strcat(result, "Lowercase character missing,");
        }
        if(!has_uppercase){
            strcat(result, "Uppercase character missing,");
        }
        if(!has_digit){
            strcat(result, "Digit missing,");
        }
        if(!has_special){
            strcat(result, "Special character missing,");
        }
        result[strlen(result)-1] = '\0';
        printf("%s\n", result);
    }

}

int main(){
    char password[100];

    printf("Enter password: ");
    scanf("%s",password);

    check_password(password);

    return 0;
}