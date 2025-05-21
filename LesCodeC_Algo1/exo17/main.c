#include <stdio.h>
#include <stdlib.h>

int main(){
    int n , q , p , r , est_premier;
    do{
        printf("donner un nombre : ");
        scanf("%d",&n);
    }while(n < 2 || n > 100);
    q = n ;
    printf("%d = ",n);
    for(p = 2 ; p < q ; p++)
    {  est_premier = 0;
        for(int i = 2 ; i <= p/2 ; i++){
            if(p % i == 0) est_premier++;
        }
        if(est_premier == 0){
         do{ r = q % p ;
            if(r == 0)
               { printf("%d * ",p);
                q = q / p;}
           }while(r == 0);
        }
    }
    printf("%d",p);
    return 0;
}
