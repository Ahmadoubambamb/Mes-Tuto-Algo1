#include <stdio.h>
#include <stdlib.h>
int main(){
    int n ,pE = 1 , i = 0 , j = 1 , pd = 1;
    double d , pD = 0.0 , som;
    do{
        printf("donner un chiffre :");
        scanf("%d",&n);
        if(n < 0 ||n >9)
          printf("ce n'est pas un chiffre ou n'est pas positif :");
          else{
            if(n % 2 == 0){
              if(i == 0){
                    pE = n;
                    i = 1;
                }
                else
                pE = pE * 10 + n;
            }
            else{
                pd = 1;
                for(int k = 0 ; k < j ; k++)
                  pd = pd * 10 ;
                 pD = pD + (double)n /pd;
                 j++;
            }
          }
    }while(n != -1);
    som = pD + pE ;
    printf("on a %lf  ",som,pD);
    return 0;
}
