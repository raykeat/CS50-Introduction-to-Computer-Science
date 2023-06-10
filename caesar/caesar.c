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
        printf("%s","Usage: ./caesar key");
        return 1;
    }

    //check whether the command line argument contains only digits
    for (int i=0 ; i<strlen(argv[1]) ; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("%s","Usage: ./caesar key");
            return 1;
        }
    }


    //convert string to integer
    int k = atoi(argv[1]);

    //get plain text input from user
    string plain_text = get_string ("Plaintext:  ");

    //print ciphertext
    printf("%s","Ciphertext: ");

    //loop through all the character of plain text
    for (int s=0 ; s<strlen(plain_text) ; s++)
    {
        if (isupper(plain_text[s]))
        {
            printf("%c", (plain_text[s]- 65 + k) % 26 +65);
        }
        else if (islower(plain_text[s]))
        {
            printf("%c", (plain_text[s]- 97 + k) % 26 +97);
        }
        else
        {
            printf("%c",plain_text[s]);
        }
    }
    printf("\n");

}