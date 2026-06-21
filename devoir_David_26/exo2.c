#include <stdio.h>

int main(){
    int n , result , rest, emputer;
    do{
       printf("donner un entier :");
       scanf("%d",&n);
    }while(n <= 0);
    result = n ;
    while(result > 19){
        rest = result % 10 ;
        emputer = result / 10 ;
        result = emputer + 2 * rest ;
    }
    if(result == 19)
     printf("%d est divisible par 19",n);
     else
     printf("%d n'est divisible par 19",n);
}