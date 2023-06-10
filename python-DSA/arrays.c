#include <stdio.h>
#include <stdlib.h>

void insert_number(int arr[], int number, int position, int len) {

    for (int i = len; i >= position; i--) {
        arr[i] = arr[i - 1];

        if (i == position) {
            arr[i] = number;
        }
    }
}

int main(void) {
    int arr[] = {1, 2, 3, 6, 7, 10, 3};
    int number = 3764;
    int position = 3;
    int len = sizeof(arr) / sizeof(arr[0]);
    //call function
    insert_number(arr, number, position, len);
    //print out numbers in the array
    for (int i = 0; i < len + 1; i++) {
        printf("%i ", arr[i]);
    }
    printf("\n");
    return 0;
}
