#include <stdio.h>

int main(int argc, char *argv[]) {
  long long a;
  long long b;
  long long c;
  long long sum;
  a = 0;
  b = 1;
  while(b < 4000000) {
    c = b;
    b = a + b;
    a = c;
    if(b % 2 == 0) {
      printf("%lld\n", b);
      sum += b;
    }
  }
  printf("Sum: %lld\n", sum);
  return 0;
}
