#include <stdio.h>
#include <stdlib.h>
/* exo3: un entier est dit distinct s'il est composer de chiffre tous differents*/
int main(){
    int i , est_distinct , tmp1 , tmp2 , rest, j = 0;
    for(i = 1000 ; i < 2000 ; i++){
       tmp1 = i ;
        while(tmp1 != 0){
             tmp2 = i;
             est_distinct = 0;
            rest = tmp1%10;
            while(tmp2 !=0){
                if(rest == tmp2%10)
                est_distinct++ ;
                   if(est_distinct >= 2)
                       break;
                tmp2 /= 10;
            }
            if(est_distinct >= 2)
                break;
            tmp1 /=10;
        }
        if(est_distinct == 1)
            printf("%d  ",i);
        if(j++%20 == 0) printf("\n");
    }
    return 0;
}
