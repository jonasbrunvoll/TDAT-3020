#include <stdio.h>
#include "fargeskrift.h"

const int max = 10;

void minefarger() {
    farge_printf(2,0, "Dette er en fargedemo");
    for(int i = 0; i < max; i++){
        printf("\n");
        for (int j = 0; j < max -4; j++){
            farge_printf(j,j+1,"NORGE HEI HEI");
        }
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
 minefarger();
}
