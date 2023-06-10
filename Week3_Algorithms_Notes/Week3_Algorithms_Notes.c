//Selection Sort
Pseudo code
For i from 0 to n-1
    Find smallest number between numbers[i] and numbers[n-1]
    Swap smallest number with number[i]

Big O notation for selection sort
O (worst case running time)
Ω (best case running time)
O(n^2/2 + n/2)
O(n^2) Worst Case Scenario - unsorted array
Ω(n^2) Best Case Scenario - sorted array

//Bubble Sort
Repeat (n-1) times
    For i from 0 to n-2
        if number(i) > number (i+1)
            then swap them
    if no swaps
        quit
O(n^2 - 2*n +1)
O(n^2) Worst Case Scenario - unsorted array
Ω(n) Best Case Scenario - sorted array

//Linear Search for correct number in lockers
For i from 0 to n-1
    if number behind door[i]
        Return True
Return False
Time complexity O(n)

//Binary Search for correct number in lockers (can only be done if the numbers are sorted)
If no doors
    Return False
Else if number behind middle door
    Return True
Else if number <  middle door
    Search Left half
Else if number > middle door
    Search right half
Time Complexity O(logn)

//string comparison in C
can't use == to compare if 2 strings are equal in C language
use strcmp function to compare 2 strings

//creating own data type in C
typedef struct
{
    string name;
    string number;
}
person;

typedef = defining a new keyword
struct = data structure
person = name of data type we're inventing
person (new data type) consists of name(a string) and number (another string)

//recursion
a programming technique whereby a function calls itself

//merge sort algorithm
if only one number
    quit
else
    sort left half of numbers
    sort right half of numbers
    merge 2 sorted halves
O(nlogn) Worst Case Scenario - unsorted array
Ω(nlogn) Best Case Scenario - sorted array


sort 1 reversed 10,000
real time = 0.302s

sort 2 reversed 10,000
real time = 0.088s

sort 3 reversed 10,000
real time = 0.194s


