#include <stdio.h>

void main(){
	int n  , nbC , tmp , p; 
     long int carre ;
	do{
		printf("donner un entier :");
		scanf("%d",&n);
	}while(n <= 0);
   carre = (long int)n*n ;
   nbC = 0 ;
   tmp = n ;
   while(tmp != 0){
   	nbC++ ;
   	tmp = tmp / 10 ;
   }
   p = 1 ; 
   for(int i = 1 ; i <= nbC ; i++){
    p = p * 10 ;
   }
  if(carre % p == n)
  	printf("%d est un nombre automorphe car %d^2 = %d",n,n,carre);
  else
  	printf("%d n'est pas un nombre automorphe car %d^2 = %d",n,n,carre);

}