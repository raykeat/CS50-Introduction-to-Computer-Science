#include <cs50.h>
#include <stdio.h>

int main(void)
{
  int n;
  do
  {
    n = get_int("Enter height: ");
  }
  while (n>8||n<1);

  for (int row=0; row<n; row++)
  {
    for(int x=1;x<n-row;x++)
    {
      printf(" ");
    }
    for(int column=0;column<=row;column++)
    {
      printf("#");
    }
    printf("\n");
  }

}
