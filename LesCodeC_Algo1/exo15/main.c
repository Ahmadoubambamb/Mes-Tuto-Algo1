#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N1, N2, tmp, nb, trouve, sont_frr , actuel;
      do{
    printf("donner un nombre N1 > 0 :");
    scanf("%d", &N1);
    printf("donner un nombre N2 > 0 :");
    scanf("%d", &N2);
    }while(N1 < 0 || N2 < 0 );
     sont_frr = 1;
     actuel = N1;
     while(actuel != 0){
        nb = actuel % 10;
        trouve = 0 ;
        tmp = N2; ;
        while(tmp != 0){
            if(nb == tmp % 10)
                trouve = 1;
            tmp = tmp / 10;
        }
        if(trouve == 0)
            sont_frr = 0;
        actuel = actuel / 10;
     }
     if(sont_frr == 1)
      { 
         actuel = N2;
            while(actuel != 0){
                nb = actuel % 10;
                trouve = 0 ;
                tmp = N1; ;
                while(tmp != 0){
                    if(nb == tmp % 10)
                        trouve = 1;
                    tmp = tmp / 10;
                }
                if(trouve == 0)
                    sont_frr = 0;
                actuel = actuel / 10;
            }
    }
     if(sont_frr == 1)
        printf("ils sont frere");
     else
        printf("ils ne sont pas frere");
    return 0;
}