#include <stdio.h>

int check_Perfect(int num)
{
    int sum = 0;

    for (int i = 1; i <= num / 2; i++)
    {
        if (num % i == 0)
        {
            sum += i;
        }
    }

    if (sum == num)
    {
        return num;
    }
    return 0;
}

int main()
{
    int start, end;

    scanf("%d", &start);
    scanf("%d", &end);

    for (int i = start; i <= end; i++)
    {
        if (check_Perfect(i) != 0)
        {
            printf("%d \n", i);
        }
    }
    return 0;
}
