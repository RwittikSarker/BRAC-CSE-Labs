#include <stdio.h>
#include <string.h>
#include <fcntl.h>


int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        return 0;
    }

    int file = open(argv[1], O_WRONLY | O_CREAT | O_APPEND, 0644);
    char input[256];

    printf("Enter strings to write to the file. Enter -1 to stop.\n");

    while(1)
    {
        scanf("%s", input);
        if (strcmp(input, "-1") == 0)
        {
            break;
        }
        write(file, input, strlen(input));
    }
    close(file);

    return 0;
}
