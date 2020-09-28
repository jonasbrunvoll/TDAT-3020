#include <stdio.h>

int main(void) 
{
    char local_28 [32];   
    printf("Enter your name: ");
    fgets(local_28,0x20,stdin);
    printf("Hello ");
    printf("%s",local_28); //Added parameter to prevent segmentation fault. 
    putchar(10);
    return 0;
}
       
