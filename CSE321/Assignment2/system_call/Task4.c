#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

void sort_desc(int arr[], int n) {
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n-i-1; j++) {
            if(arr[j] < arr[j+1]) {
                int temp1 = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp1;
            }
        }
    }
}

void check_odd_even(int arr[], int n) {
    for(int i = 0; i < n; i++) {
        char result[] = "even";
        if (arr[i] % 2 != 0){
            strcpy(result, "odd");
        }
        printf("%d is %s\n", arr[i], result);
    }
}

int main(int argc, char *argv[]) {
    if(argc < 2) {
        printf("Please provide numbers as command line arguments\n");
        return 0;
    }

    int n = argc - 1;
    int *numbers = malloc(n * sizeof(int));
    
    for(int i = 0; i < n; i++) {
        numbers[i] = atoi(argv[i + 1]);
    }

    pid_t pid = fork();

    if(pid == 0) {
        printf("Child process sorting the array:\n");
        sort_desc(numbers, n);
        for(int i = 0; i < n; i++) {
            printf("%d ", numbers[i]);
        }
        printf("\n");
        exit(0);
    } else {
        wait(NULL);
        printf("\nParent process checking odd/even:\n");
        check_odd_even(numbers, n);
    }

    free(numbers);
    return 0;
}
