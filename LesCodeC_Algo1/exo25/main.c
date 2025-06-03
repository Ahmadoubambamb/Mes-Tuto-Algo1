#include <stdio.h>
#include <stdlib.h>

int main(){
 int n , chif ,p , carre , somme;
  //controle de saisi
   do{printf("donner un nombre : ");
       scanf("%d",&n);
   }while(n <= 0);
   if(n <10)
   carre = n*n;
    // ici si le nombre est superieur a 10 donc cela dit que le nombre a plus de 2 chiffre
   while(carre >=10){
       somme  = 0;
       printf("%d \n\n",carre);
      while(carre != 0){
        chif = carre % 10;
        p = chif * chif;
        somme  = somme + p;
        carre = carre/10;
       }

    carre = somme;
  }
  printf("%d\n\n",carre);
  if(carre == 1)
   printf("Le nombre %d est heureux \n",n);
   else
       printf("le nombre %d n'est pas heureux \n",n);

  return 0;
}
