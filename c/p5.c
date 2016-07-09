#include <stdio.h>
#include <stdbool.h>

bool canDivide(int num) {
  // Everything below 10 is tested from 11-20
  for(int i = 20; i > 10; i--) {
    if(num % i != 0) return false;
  }
  return true;
}

int main() {
  int smallest = 0;
  int test = 100;
  while(!smallest) {
    if(canDivide(test)) smallest = test;
    ++test;
  }
  printf("%d\n", smallest);

  return 0;
}
