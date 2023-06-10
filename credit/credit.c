#include <cs50.h>
#include <stdio.h>

int main(void)
{
   long n;
   do
   {
    n = get_long("Enter number: ");
   }
   while (n<0);


   int n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,total;

   //every alternate digit multiplied by 2 to get product
   n2=((n%100)/10)*2;
   n4=((n%10000)/1000)*2;
   n6=((n%1000000)/100000)*2;
   n8=((n%100000000)/10000000)*2;
   n10=((n%10000000000)/1000000000)*2;
   n12=((n%1000000000000)/100000000000)*2;
   n14=((n%100000000000000)/10000000000000)*2;
   n16=((n%10000000000000000)/1000000000000000)*2;

   //sum of digits in each product
   n2=(n2%10)+((n2%100)/10);
   n4=(n4%10)+((n4%100)/10);
   n6=(n6%10)+((n6%100)/10);
   n8=(n8%10)+((n8%100)/10);
   n10=(n10%10)+((n10%100)/10);
   n12=(n12%10)+((n12%100)/10);
   n14=(n14%10)+((n14%100)/10);
   n16=(n16%10)+((n16%100)/10);

   //finding digits that are NOT multiplied by 2
   n1=(n%10);
   n3=(n%1000)/100;
   n5=(n%100000)/10000;
   n7=(n%10000000)/1000000;
   n9=(n%1000000000)/100000000;
   n11=(n%100000000000)/10000000000;
   n13=(n%10000000000000)/1000000000000;
   n15=(n%1000000000000000)/100000000000000;

   //find total sum of all digits
   total=n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16;

    //find out if number is invalid
    if ((total%10)!=0)
    {
        printf("%s\n","INVALID");
    }

    int length;
    length=1;
    long vn,an,mn;
    vn=n;
    an=n;
    mn=n;

    //find length of number
    while (n>=10)
    {
        n=n/10;
        length++;
    }

    //find out if card is visa
    if ((length==13||length==16) && n==4)
    {
        printf("%s\n","VISA");
    }

    //find out if card is master
    mn=mn/100000000000000;
    if ((mn==51||mn==52||mn==53||mn==54||mn==55) && length==16)
    {
        printf("%s\n","MASTERCARD");
    }

    //find out if card is amex
    an=an/10000000000000;
    if ((an==34||an==37) && length==15)
    {
        printf("%s\n","AMEX");
    }
}
