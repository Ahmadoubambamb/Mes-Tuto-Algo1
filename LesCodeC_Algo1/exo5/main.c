#include <stdio.h>
#include <stdlib.h>

int main(){
 int fact = 1 , i , n;
  do{printf("donner un entier positif:");
      scanf("%d",&n);
   }while(n < 0);
   if(n > 0)
 for( i = 1 ; i < n ; i++)
    fact = fact * i;
     printf("factoriel de %d est %d ",n,fact);
  return 0;
}
