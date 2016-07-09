#include <stdio.h>
#include "prime.h"

int quadratic(long n, long a, long b) {
  return n*n + (a * n) + b;
}

int countPrimes(long a, long b) {
  int n = 0;
  long prod;
  while(1) {
    prod = quadratic(n, a, b);
    if(isPrime(prod)) {
      n++;
    } else {
      return n;
    }
  }
}


int main() {
  long streak = 0;
  long max, maxa, maxb;
  for(int i=1000; i>-1000; i--) {
    for(int j=1000; j>-1000; j--) {
      streak = countPrimes(i, j);
      if(max < streak) {
        max = streak;
        maxa = i;
        maxb = j;
      }
    }
  }
  printf("%ld %ld %ld\n", maxa, maxb, max);
  printf("Product of coeffs: %ld \n", maxa * maxb);


  return 0;
}
