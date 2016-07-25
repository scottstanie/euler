#include <stdio.h>
#include <math.h>

// double fact(double x) {
//   return tgamma(x+1.);
// }

long fact(int x) {
  if(x <= 1) return 0;
  return x * fact(x-1);
}

long s(long n) {
  int m = 2;
  while((fact(m) % n) != 0) {
    ++m;
  }
  return m;
}

int main(int argc, char *argv[]) {
  int a = atoi(argv[1]);
  printf("%ld\n", fact(a));
  return 0;
}
