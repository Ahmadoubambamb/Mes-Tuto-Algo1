#include <stdio.h>
#include <stdlib.h>

int main(){
    int n ,cpt0 , cpt1 , tmp;
    do{
        printf("donner un entier naturel:");
        scanf("%d",&n);
    }while(n < 0);
    cpt0 = 0; cpt1 = 0;
    tmp = n;
    while(tmp!=0){
        if(tmp%2 == 0) cpt0++;
        else cpt1++;
        tmp = tmp / 2;
    }
    if(cpt0 == cpt1)
        printf("%d est un nombre ROND \n",n);
    else
        printf("%d n'est pas un nombre ROND \n",n);
}
