#include<stdio.h>
#include<stdlib.h>

void merge(int *left, int *right, int *list, int nL, int nR) {
    int i = 0, j = 0, k = 0;
    while (i < nL && j < nR) {
        if (left[i] <= right[j]) {
            list[k++] = left[i++];
        } else {
            list[k++] = right[j++];
        }
    }
    while (i < nL) {
        list[k++] = left[i++];
    }
    while (j < nR) {
        list[k++] = right[j++];
    }
}

void mergeSort(int *list, int n) {
    if (n <= 1) {
        return;
    }
    int mid = n / 2;
    int *left = malloc(sizeof(int) * mid);
    int *right = malloc(sizeof(int) * (n - mid));
    for (int i = 0; i < mid; i++) {
        left[i] = list[i];
    }
    for (int i = 0; i < n - mid; i++) {
        right[i] = list[i + mid];
    }
    mergeSort(left, mid);
    mergeSort(right, n - mid);
    merge(left, right, list, mid, n - mid);
    free(left);
    free(right);
}

int main() {
    int list[] = {38, 27, 43, 3, 9, 82, 10};
    int n = sizeof(list) / sizeof(list[0]);
    mergeSort(list, n);
    for (int i = 0; i < n; i++) {
        printf("%d ", list[i]);
    }
    printf("\n");
    return 0;
}
