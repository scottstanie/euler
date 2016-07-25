#include <math.h>
#include <stdlib.h>
#include <stdio.h>

long mac(int m, int k, int s, int n) {
  // More like fail recursion :(
  if(n > m) {
    return n - s;
  } else {
    return mac(m, k, s, mac(m, k, s, n + k));
  }
}

long recMac(int m, int k, int s, int n) {
  // Dis is better
  int c;
  for(c = 1; c != 0; ) {
    if (n > m) {
      n -= s;
      --c;
    } else {
      n += k;
      ++c;
    }
  }
  return n;
}


long highest_fp(m, k, s) {
  return m - (2 * s) + k;
}


long sfmac(int m, int k, int s) {
  // Return sum of an array containing the fixed points
  //
  int num_points = k - s;
  if(s % num_points != 0) return 0;

  long highest = highest_fp(m, k, s);
  long lowest = highest - num_points + 1;
  long sum = 0;
  for(int i = lowest; i <= highest; i++) sum += i;
  return sum;
  
  // int fpoints[k-s];
  // int idx = 0;
  // for(int i=1; i < m + k; i++) {
  //   if(i == recMac(m, k, s, i)) {
  //     fpoints[idx] = i;
  //     ++idx;
  //   }
  // }

  // long sum = 0;
  // for(int i=0; i<idx; i++) sum += fpoints[i];
  // return sum;
}

long s(int p, int m) {
  long sum = 0;
  for(int s=1; s < p; s++) {

    for(int k=s+1; k < p + 1; k++) {
      sum += sfmac(m, k, s);
    }
  }
  return sum;
}


int main(int argc, char *argv[]) {
  int p = atoi(argv[1]);
  int m = atoi(argv[2]);
  printf("Args: %d %d\n", p, m);
  // printf("%ld\n", mac(100, 11, 10, 91));
  // printf("%ld\n", sfmac(100, 11, 10));
  printf("%ld\n", s(p, m));

  return 0;
}
