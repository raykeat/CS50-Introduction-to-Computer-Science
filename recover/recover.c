#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    //check if there's one Command line argument
    if (argc!=2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }
    //open file for reading
    FILE *input = fopen(argv[1], "r");

    //check that file is valid
    if (file==NULL)
    {
        printf("Error: cannot open file");
        return 1;
    }

    //store 512 byte blocks into arrays

    unsigned char array[512];

    int count=0;

    //file pointer for recovered images

    FILE *output = NULL;

    while (fread(array,sizeof(char),512,input))
    {
        if (array[0]==0xff && array[1]==0xd8 && array[2]==0xff && (array[3] & 0xf0)== 0xe0)
    }





}