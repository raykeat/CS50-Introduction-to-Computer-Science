#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get number from user
    long n=get_long("Enter number: \n");

    //find length of number
    int i=1;
    while (n>=10)
    {
        n/=10;
        i++;
    }

    //find if length of number is valid
    if ((i!=13) && (i!=15) && (i!=16))
    {
        printf("INVALID\n");
    }

    //find out the sum of digits
    int sum1=0;
    int sum2=0;
    int mod1=0;
    int mod2=0;
    long y=n;
    int total=0;
    int digit1=0;
    int digit2=0;

    do
    {
        //calculate sum1
        mod1 = y%10;
        sum1+=mod1;
        y/=10;

        //calculate sum2
        mod2 = y%10;
        mod2 = mod2 *2;
        digit1= mod2 % 10;
        digit2= (mod2/10)%10;
        sum2 += digit1 + digit2;
        y/=10;
    }
    while (y>0);

    //calculate total sum
    total = sum1+sum2;

    //check if total sum divisible by 10
    if (total%10!=0)
    {
        printf("INVALID\n");
    }

    //find first 2 digits of number
    while (n>=100)
    {
        n/=10;
    }

    //find out if its mastercard
    if ((n==51 || n==52 || n==53 || n==54 || n==55) && (i==16))
    {
        printf("MASTERCARD\n");
    }

    //find out if its amex
    else if ((i==15) && (n==34||n==37))
    {
        printf("AMEX\n");
    }

    else if ((i==13||i==16) && ((n/10)%10==4))
    {
        printf("VISA\n");
    }

    else
    {
        printf("INVALID\n");
    }
}