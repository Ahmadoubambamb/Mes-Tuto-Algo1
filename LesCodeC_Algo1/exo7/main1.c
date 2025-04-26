#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int n, nb1 , nb2 , nb3 ,temp,i;
    int c1, c2 , c3 ,c4 ,c5,c6;
    do{
    printf("donner un nombre de trois chiffre non null:");
    scanf("%d",&n);
    temp = n;
    nb3 = temp%10;
    temp /= 10;
    nb2 = temp%10;
    nb1 = temp/10;
    }while(nb1 == 0 || nb2 == 0 || nb3 == 0 || n >999);

    c1 = nb1 * 100 + nb2 * 10 + nb3;
    c2 = nb1 * 100 + nb3 * 10 + nb2;
    c3 = nb2 * 100 + nb1 * 10 + nb3;
    c4 = nb2 * 100 + nb3 * 10 + nb1;
    c5 = nb3 * 100 + nb1 * 10 + nb2;
    c6 = nb3 * 100 + nb2 * 10 + nb1;

    printf("%d  %d  %d  %d  %d  %d\n",c1,c2,c3,c4,c5,c6);
    return 0;
}

/*
   nb1 1
  nb2  8

 */
