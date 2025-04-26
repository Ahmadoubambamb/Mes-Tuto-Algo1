#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int ab , nb1 , nb2 , temp , inv;
    do{
        printf("donner un nombre de deux chiffre different:");
        scanf("%d",&ab);
        nb1 = ab/10;
        nb2 = ab%10;

    }while(ab >100 || ab<=0 ||nb1 == nb2);
   temp = ab;
  printf("la liste vers est : %d\t",ab);
   while(temp != 9){
    nb1 = temp/10;
    nb2 = temp%10;
     inv = nb2 * 10 + nb1;
     temp = abs(temp - inv);
     printf("%d\t",temp);
  }
  return 0;
}

/*
   nb1 1
  nb2  8

 */
