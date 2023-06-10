#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //check whether there's one command line argument
    if (argc!=2)
    {
        printf("%s","Usage: ./substitution key\n");
        return 1;
    }

    //check whether command line argument contains 26 characters
    if (strlen(argv[1])!=26)
    {
        printf("%s","Key must contain 26 characters.\n");
        return 1;
    }

    //check if characters are all digits
    for (int i=0 ; i<strlen(argv[1]) ; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("%s","Error.\n");
            return 1;
        }
    }

    //get input from user
    string plain_text = get_string ("Plaintext:  ");

    //print ciphertext
    printf("%s","ciphertext: ");

    //loop through all the character of plain text
    for (int s=0 ; s<strlen(plain_text) ; s++)
    {
        if (isupper(plain_text[s]))
        {
            char upper_c = toupper(argv[1][(plain_text[s]- 65)]);
            printf("%c",upper_c);
        }
        else if (islower(plain_text[s]))
        {
            char lower_c = tolower(argv[1][(plain_text[s]- 97)]);
            printf("%c",lower_c);
        }
        else
        {
            printf("%c",plain_text[s]);
        }
    }
    printf("\n");

}