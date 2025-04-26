#include <stdio.h>
#include <stdlib.h>

int main(){
     int i , n , tmp , s =0 , rest;
     printf("donner un nombre : ");
     scanf("%d",&n);
     tmp = n;
     while(tmp != 0){
         rest = tmp%10;
         s +=rest;
         tmp /=10;
    }
    printf(" la somme des chiffre de %d est %d\n",n,s);
    return 0;
}
