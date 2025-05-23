#include <stdio.h>
#include <stdlib.h>

int main(){
    int l , pl , i , j , s;
    do{ printf("donner un entier positif:");
     scanf("%d",&l);
    }while(l <= 0);
     pl = 1 ;
     for(i = 1; i <= l; i++){
        s = 0;
       for(j = 1 ; j <= i ; j++)
          s += pl ;
         pl = s;
         printf("%d ",i);
         if(i != l)
         printf("* ");
}
printf("= %d",pl);
return 0;
}