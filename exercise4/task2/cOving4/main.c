#include <stdio.h>
#include <stdlib.h>
#include <string.h>


const char* transform(const char* pointer, size_t input){
    char* and = "&amp";
    char* lt = "&lt";
    char* gt = "&gt";
    static char transform[256];
    int j =0;

    for (int i = 0; i < input; ++i) {
        if (pointer[i] == '&'){
            strcpy(&transform[j], and);
            j += 4;
        } else if (pointer[i] == '<'){
            strcpy(&transform[j], lt);
            j+=3;
        } else if (pointer[i] == '>'){
            strcpy(&transform[j], gt);
            j+=3;
        } else if(&pointer[i] == '/0') {
            break;
        } else {
            transform[j] = pointer[i];
            j += 1;
        }
    }
    return transform;

}

const char* setUp(char* pointer, int memorySize){
    printf("Allocating memory space...\n");
    pointer = (char* )malloc(memorySize);
    if( pointer == NULL)
    {
        perror("Unable to allocate memory");
        exit(1);
    } else {
        printf("Memory allocated! Now, write a sentence:\n");
    }
    return pointer;
}


int main()
{
    char* buffer;
    int memorySize = 32;
    size_t input;

    //Pointer pointing to allocated memorySize
    char* pointer = setUp(buffer, memorySize);

    //Reads input from terminal
    input = getline(&pointer, &memorySize, stdin);

    //Prints out transformation
    printf("You typed: %s",transform(pointer, input));
    return(0);
}
