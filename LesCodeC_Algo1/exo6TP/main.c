#include <stdio.h>
#include <stdlib.h>

int main(){
  int i , j , n;
  printf("pour n = ");
  scanf("%d",&n);
   for(i = 1 ; i <= n ; i++){
       for(j = 1 ; j <=i ; j++)
           printf("%-7d",i*j);
           printf("\n");
      }
}
