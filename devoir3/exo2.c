#include <stdio.h>
#include <stdlib.h>

int main(){
    int t[20],i ,j , permute = 0 , n = 8 , tmp;
     for(int i = 0 ;i < n ; i++){
         printf("donner le %d ieme element :",i+1);
         scanf("%d",&t[i]);
    }
  for(i = 0 ; i < n ; i++){
     if(t[i] == 0){
         j = i + 1;
         permute = 0;
         while(permute == 0 && j < n){
             if(t[j] != 0){
                 tmp = t[i] ;
                 t[i] = t[j] ;
                 t[j] = tmp ;
                 permute = 1;
            }
            else
                j++;
        }
    }
 }
 printf("apres l'operation on  a : \n");
 for(int i = 0; i < n ; i++)
     printf("%d  ",t[i]);
}
