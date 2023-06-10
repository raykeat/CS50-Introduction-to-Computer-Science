// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

int count=0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int a = hash(word);
    node *p  = table[a];

    while (p!=NULL)
    {
        if (strcasecmp(p->word,word) ==0)
        {
            return true;
        }
        else if (strcasecmp(p->word,word) !=0)
        {
            p = p->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int d= (toupper(word[0]) - 65);
    d=d%26;
    return d;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //open the dictionary
    FILE *file = fopen(dictionary,"r");
    if (file==NULL)
    {
        return false;
    }

    char word[LENGTH + 1];

    //read words from file
    while (fscanf(file, "%s", word)!=EOF)
    {

        //creating a new node for each word

        node *p = malloc(sizeof(node));
        if (p==NULL)
        {
            return false;
        }
        else
        {
            strcpy(p->word,word);

            //call hash function to determine the corresponding number for each word
            int y = hash(p->word);

            p->next = table[y];
            table[y] = p;
            count++;
        }
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (count>0)
    {
        return count;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int b=0 ; b<N ; b++)
    {
        node *p = malloc(sizeof(node));

        p = table[b];
        while (p!=NULL)
        {
            node *tmp = p;
            p = p->next;
            free(tmp);
        }
        if (p==NULL)
        {
            return true;
        }
    }
    return false;

}
