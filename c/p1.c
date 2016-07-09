#include <stdio.h>

int main(int argc, char **argv) {
  int max = 1000;
  int sum = 0;
  for (int i=0; i<max; i++) {
    if ((i % 3 == 0) || (i % 5 == 0)) sum += i;
  }

  printf("%d\n", sum);
  return 0;
}
