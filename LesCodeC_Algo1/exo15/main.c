#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N1, N2, tmp, min, max, nb;
      int trouve;
      int sont_frr;
    printf("donner 2 nbre");
    scanf("%d%d", &N1, &N2);
    if(N1<N2)
     { min = N1 ;
       max = N2 ;
     }
     else
     {
         min = N2;
         max = N1;
     }
     sont_frr = 1;
     while(max != 0){
        nb = max % 10;
        trouve = 0 ;
        tmp = min ;
        while(tmp != 0){
            if(nb == tmp % 10)
                trouve = 1;
            tmp = tmp / 10;
        }
        if(trouve == 0)
            sont_frr = 0;
        max = max / 10;
     }
     if(sont_frr == 1)
        printf("ils sont frere");
    printf("ils ne sont pas frere");
    return 0;
}