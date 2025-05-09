#include <stdio.h>
#include <stdlib.h>

int main(){
    int n , cube , som = 0, debut ,k = 0 , membre;
    do{
        printf("donner un entier:");
        scanf("%d",&n);
    }while(n <= 0);
    cube = n*n*n ;
    while(cube != som){
        debut = 2*k+1;
        som = 0;
        membre = debut;
      for(int i = 1 ; i <=n ; i++){
         som += membre;
          membre +=2;
      }
      if(som == cube){
          membre = debut;
           printf("%d^3 =",n);
          for(int i = 1; i <n; i++){
             printf(" %d + ",membre);
             membre += 2;
        }
        printf("%d\n",membre);
    }
     k++;
    }
}


