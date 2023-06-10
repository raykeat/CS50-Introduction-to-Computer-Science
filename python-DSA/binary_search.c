#include <stdio.h>
#include <math.h>
#include <stdbool.h>

//function prototype
bool binary_search(int arr[], int arr_len, int number);

int main(void){

    //initializing an array in C
    int arr[] = {1,2,5,10,79,92,545};

    //choosing target number
    int number = 5;

    int arr_len = sizeof(arr)/sizeof(arr[0]);

    bool result = binary_search(arr, arr_len, number);

    printf("result is %d\n",result);

    printf("hello world");

}


//recursive function to check if number exist in list
bool binary_search(int arr[], int arr_len, int number)
{

    int midpoint = floor(arr_len/2);

    //base case to terminate recursion
    if (arr_len == 0)
    {
        return false;
    }

    else
    {

        //base case to terminate recursion
        if (arr[midpoint] == number)
        {
            return true;
        }

        //recursive case 1
        if (arr[midpoint]<number)
        {
            //In the recursive calls, you are passing in the ending address of the subarray
            //rather than the length of the subarray. In C, when passing the length of
            //an array to a function, the size should be passed in bytes.
            //So, in the recursive call, you should pass the length of the subarray in bytes,
            //which can be calculated by subtracting the starting address
            //of the subarray from the ending address of the subarray and
            //then multiplying by the size of an element in the array.
            return binary_search(arr + midpoint + 1, arr_len - midpoint - 1, number);

        }

        //recursive case 2
        if (arr[midpoint]>number)
        {
            return binary_search(arr, midpoint-1, number);

        }


    }
    return false;

}