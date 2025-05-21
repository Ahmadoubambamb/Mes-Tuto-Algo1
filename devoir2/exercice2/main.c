#include <stdio.h>
#include <stdlib.h>

int main(){
    int M , N = 0 , m , puiss2 , est_premier = 1 ;
    do{printf("donner un entier : ");
       scanf("%d",&M);
      }while(M <= 2);

     do{
          puiss2 = 1 ;
          for(int i = 1 ; i <=N ; i++)
              puiss2 *= 2;
         m = puiss2 - 1 ;
         N++;
      }while(m != M && N < M/2);
      if(N == M/2){
          printf("%d ne peut pas s'ecrire sous forme 2^n - 1 \n",M);
    }
     else{
      N-- ;

     for(int i = 2 ; i <=N/2 ;i++){
         if(N % i == 0)
             est_premier = 0 ;
    }
    (est_premier ? printf("%d est mersenne car M = 2^%d - 1 , n = %d premier\n",M,N,N) : printf("%d n'est pas mersenne  M = 2^%d - 1 n = %d non_premier",M,N,N));
    }
    return 0;
}
