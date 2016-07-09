#include <stdio.h>
#include "prime.h"

int quadratic(long n, long a, long b) {
  return n*n + (a * n) + b;
}

int main() {
  long prod;
  long streak = 0;
  long max, maxa, maxb;
  int count;
  for(int i=1000; i>-1000; i--) {
    for(int j=1000; j>-1000; j--) {
      count++;
      int n = 0;
      while(1) {
        prod = quadratic(n, i, j);
        if(isPrime(prod)) {
          streak++;
          n++;
        } else {
          if(max < streak) {
            max = streak;
            maxa = i;
            maxb = j;
          }
          streak = 0;
          break;
        }
      }
    }
  }
  printf("%ld %ld %ld %d\n", maxa, maxb, max, count);
  printf("Product of coeffs: %ld \n", maxa * maxb);


  return 0;
}
