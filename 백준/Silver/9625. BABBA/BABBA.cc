#include <stdio.h>

int main()
{
    int k, a = 1, b = 0;
    scanf("%d", &k);

    while (k--)
    {
        int c, d;
        c = b;
        d = a + b;
        a = c;
        b = d;
    }
    printf("%d %d", a, b);
}