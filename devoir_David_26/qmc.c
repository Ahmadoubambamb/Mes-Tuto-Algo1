#include <stdio.h>
#include <math.h>
void qcm1()
{
    int i = 0, j, nb = 0;
    printf("QCM 1 ----> ");
    for (j = -4; j <= 4; j++)
    {
        if (j >= 0 && (i++))
            nb = nb + j;
    }
    nb = nb + i;
    printf("%d \n\n", nb);
}

void qcm2()
{
    unsigned long int n, i, j = 0, som = 0;
    n = pow(2, 30);
    printf("QCM 2 ----> ");
    for (i = n; i > 1; i = i / 2)
        j++;
    for (; j > 1; j = j / 2)
        som++;
    printf("%d \n\n", som);
}

void qcm3()
{
    printf("QCM 3 ----> ");
    while (1)
    {
        int i = 0;
        while (i-- < 12)
        {
            ++i;
            for (;;)
            {
                if (i++ < 5)
                    continue;
                break;
            }
        }
        printf("%d ", i);
        break;
    }
    printf("\n\n");
}

void qcm4()
{
    printf("QCM 4 ----> ");
    int n = 92625, d, t, x, y;
    x = y = 0;
    t = 1;
    while (n >= t)
        t *= 10;
    t /= 10;
    while (t > 0)
    {
        d = n / t;
        n = n % t;
        t /= 10;
        if (y)
            x = 10 * x + d;
        y = (y + 1) % 2;
    }
    printf("%d \n\n", x);
}

void qcm5()
{
    printf("QCM 5 ----> ");
    int i, j, k = 0;
    j = 2 * 3 / 4 + 2.0 / 5 + 8 / 5;
    k -= --j;
    // for (i = 0; i < 6; i++)
    // {
    //     switch (i + k)
    //     {
    //     case 1:
    //     case 2:
    //         printf("\n %d", i + k);
    //     case 3:
    //         printf("\n %d ", i + k);
    //     default:
    //     }
    // }
    printf("erreur de compilation");
}

int main()
{
   qcm1();
   qcm2();
   qcm3();
   qcm4();
   qcm5();

}