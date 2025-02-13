#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    
    int process_count = 1;
    pid_t a, b, c;

    pid_t original_pid = getpid();

    a = fork();
    if (a == 0) {
        if (getpid() % 2 != 0) {
            fork();
        }
    } else if (a > 0) {
        process_count++;
    }

    b = fork();
    if (b == 0) {
        if (getpid() % 2 != 0) {
            fork();
        }
    } else if (b > 0) {
        process_count++;
    }

    c = fork();
    if (c == 0) {
        if (getpid() % 2 != 0) {
            fork();
        }
    } else if (c > 0) {
        process_count++;
    }

    if (getpid() == original_pid){
        while (wait(NULL) > 0)
            ;
        printf("Total number of processes created: %d\n", process_count);
    }

    return 0;
}