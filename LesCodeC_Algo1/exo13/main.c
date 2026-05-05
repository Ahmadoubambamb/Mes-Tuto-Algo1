#include <stdio.h>
int main() {
  int n , m , sm ,divis , sn ;
  for( n = 1 ; n <= 10000 ; n++ ) {
    sm = 0 ;
    sn = 0 ;
    for( divis = 1 ; divis < n ; divis++ ) {
      if( n % divis == 0 ) {
        sn += divis ;
      }
    }
    m = sn ;
   for( divis = 1 ; divis < m ; divis++ ) {
      if( m % divis == 0 ) {
        sm += divis ;
      }
    }
    if( sm == n && n <= m ) {
      printf("(%d ; %d) est un couple de nombres amicaux.\n", n, m);
    }
  }
    return 0;
}