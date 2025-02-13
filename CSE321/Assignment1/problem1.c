#include <stdio.h>

void main(){
    int a, b, result;

    printf("Input first number: ");
    scanf("%d", &a);
    printf("Input second number: ");
    scanf("%d", &b);

    if(a>b){
        result = a - b;
        printf("%d", result);
    }
    else if (a<b){
        result = a + b;
        printf("%d", result);
    }
    else{
        result = a * b;
        printf("%d", result);
    }
}