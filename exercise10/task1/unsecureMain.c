#include <stdio.h>

/*
This function is unsecure because the 
printf function is missing format parameters.

The main function is therfore to 
format string attacks.

Input values which is dangerouse for this program:
  %s - Resualt in segmentation fault. Makes the program crash. 
  %x - Prints out local_28 address as hex. 
*/

int main(void)

{
  char local_28 [32];
  printf("Enter your name: "); 
  fgets(local_28,0x20,stdin);
  printf("Hello "); 
  printf(local_28); //Missing format parameter.
  putchar(10);
  return 0;
}
