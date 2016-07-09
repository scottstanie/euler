#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isPal(int a) {
  char strnum[10];
  sprintf(strnum, "%d", a);
  int num_digits = strlen(strnum);
  //printf("%d", num_digits);
  for(int i=0; i<num_digits/2; i++) {
    if(strnum[i] != strnum[num_digits - 1 - i]) return false;
  }
  return true;
}

int main() {
  int prod;
  int max = 0;
  for(int i=1000; i>100; i--) {
    for(int j=1000; j>100; j--) {
      prod = i*j;
      if((prod >= max) && isPal(prod)) max = prod;
    }
  }
  printf("%d\n", max);
  return 0;
}
