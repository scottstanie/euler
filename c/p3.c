#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include "prime.h"

int main() {
  long long target = 600851475143;
  long max_attempt = (long)sqrt(target);
  long max;

  for(long i=1; i<=max_attempt; i++) {
    if((0 == (target % i)) && isPrime(i)) {
      max = i;
    }
  }
  printf("Max prime factor: %ld\n", max);
  return 0;
}
