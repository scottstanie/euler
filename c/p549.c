#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// double fact(double x) {
//   return tgamma(x+1.);
// }

long fact(int x) {
  if(x <= 1) return 1;
  return x * fact(x-1);
}

int s(long n) {
  int m = 1;
  for(m=1; fact(m) % n != 0; m++);
  return m;
}

long S(int n) {
  int i, sum;
  for(i=2; i<=n; i++) {
    printf("%d: %d\n", i, s(i));
    sum += s(i);
  }
  return sum;
}

int main(int argc, char *argv[]) {
  int a = atoi(argv[1]);
  // printf("fact(n): %ld\n", fact(a));
  printf("s(n): %ld\n", s(a));
  printf("S(n): %ld\n", S(a));
  return 0;
}
