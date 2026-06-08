#include <stdio.h>

int main(){
    int i , N , cpt , tmp , s, invers;
    printf("les nombres tout terrain entre 100 et 1000 sont :\n");
    for(N = 100 ; N < 1000 ; N++){
     cpt = 0 ; // on compte le nombre de diviseurs
     for(i = 1 ; i <= N ; i++)
      {  if(N % i == 0)
             cpt++ ;
      }
     if(cpt == 2){ //un nombre premier n'a que deux diviseurs
      tmp = N ;
      s = 0 ;
      while(tmp != 0){
        s = s + tmp % 10 ;
        tmp = tmp / 10 ;
      }
      cpt = 0 ;
      for(i = 1 ; i <= s ; i++)
      {  if(s % i == 0)
             cpt++ ;
      }
      if(cpt == 2){
          invers = 0 ;
          tmp = N ;
          while(tmp != 0){
              invers = invers * 10 + tmp%10 ;
              tmp = tmp / 10 ;
        }
        cpt = 0 ;
        for(i = 1 ; i <= invers; i++){
            if(invers % i == 0)
             cpt++ ;
           }
           if(cpt == 2)
               printf("%d \n",N);
       }
     }
    }
    return 0;
}
