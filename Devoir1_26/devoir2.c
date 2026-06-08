#include <stdio.h>
int main(){
 int N , est_pair, tmp ,r, repeter;
   do{ printf("donner un entier N > 0 : ");
       scanf("%d",&N);
     }while(N <= 0);
     r = N % 10 ;
     tmp = N / 10 ;
     if(r % 2 == 0)
         est_pair = 1 ;
    else
        est_pair = 0 ;
    repeter = 0 ;
    while(tmp != 0 && !repeter){
        r = tmp % 10 ;
       if(r % 2 == 0 && est_pair)
           repeter = 1 ;
       if(r % 2 == 0 && !est_pair)
           est_pair = 1 ;
        if(r % 2 != 0 && !est_pair)
            repeter = 1 ;
        if(r % 2 != 0 && est_pair)
            est_pair = 0;
        tmp = tmp / 10;
    }
     if(!repeter)
    printf("%d est alternant !",N);
    else
        printf("%d n'est pas alternant",N);

}
