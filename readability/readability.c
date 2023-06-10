#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//prototype of function that counts letters in text
int count_letters(string text);

//prototype of function that counts words in text
int count_words(string text);

//prototype of function that counts sentences in text
int count_sentences(string text);

//how to input string and int
//printf("%i%s\n", letters, " letters");
//printf("%i%s\n", words, " words");
//printf("%i%s\n", sentences, " sentences");

int main(void)
{
    string sentence = get_string("Text: ");
    float letters = count_letters (sentence);
    float words = count_words (sentence);
    float sentences = count_sentences (sentence);
    float L = letters/words*100;
    float S = sentences/words*100;
    float index = 0.0588 * L - 0.296*S - 15.8;
    int index_round = round (index);
    if (index_round<1)
    {
        printf("%s\n","Before Grade 1\n");
    }
    if (index_round<16 && index_round>=1)
    {
        printf("%s%i\n","Grade ",index_round);
    }
    if (index_round>=16)
    {
        printf("%s\n","Grade 16+\n");
    }
}

//function that counts letters in text
int count_letters(string text)
{
    int count=0;
    for (int i=0 ; i<strlen(text) ; i++)
    {
        if (isalpha(text[i]))
        {
            count+=1;
        }
    }
    return count;
}

//function that counts words in text
int count_words(string text)
{
    int count=1;
    for (int i=0 ; i<strlen(text) ; i++)
    {
        if (isspace(text[i]))
        {
            count+=1;
        }
    }
    return count;
}

//function that counts sentences in text
int count_sentences(string text)
{
    int count=0;
    for (int i=0 ; i<strlen(text) ; i++)
    {
        if (text[i]=='?' || text[i]=='.' || text[i]=='!')
        {
            count+=1;
        }
    }
    return count;
}