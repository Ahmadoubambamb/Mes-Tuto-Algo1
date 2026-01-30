#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N1, N2, tmp, min, max, nb;
      int trouve;
      int sont_frr;
      do{
    printf("donner un nombre N1 > 0 :");
    scanf("%d", &N1);
    printf("donner un nombre N2 > 0 :");
    scanf("%d", &N2);
    }while(N1 < 0 || N2 < 0 );
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
     else
        printf("ils ne sont pas frere");
    return 0;
}