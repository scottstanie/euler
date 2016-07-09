#include <stdbool.h>
#include <math.h>
#include "prime.h"

bool isPrime(long n) {
  if(n < 2) return false;
  if(n == 2 || n == 3) return true;
  if(n % 2 == 0) return false;

  for(long i=3; i<=sqrt(n); i+=2) {
    if(n % i == 0) {
      return false;
    }
  }
  return true;
}


