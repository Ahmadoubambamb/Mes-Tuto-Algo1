#include <stdio.h>

int main()
{
    float l;
    int n , ni, i, s;
    do
    {
        printf("donner nombre strictement positif: ");
        scanf("%f", &l);
    } while (l <= 0.0);

    ni = 0;
    do
    {
        s = 0;
        for (i = 1; i <= ni; i++)
          s = s + i ;
        n = ni ;
        ni++ ;
    } while (2 * s - n < l);
    printf("n = %d est la parti entier sup de racine(%.2f)",n,l);
}