#write function to perform binary search of number from a list

def binary_search(new_list,number):

    #base case to terminate recursion
    if len(new_list) == 0:
        return False

    else:
        midpoint = (len(new_list))//2

        #base case to terminate recursion
        if new_list[midpoint] == number:
            return True

        #recursive case 1
        elif new_list[midpoint]<number:
            first = midpoint + 1
            last = len(new_list)-1
            return binary_search(new_list[first:last],number)

        #recursive case 2
        else:
            first = 0
            last = midpoint-1
            return binary_search(new_list[first:last],number)

list = [2,3,4,5,6,4,6,66,3,5,55,8907,123,457,4231,69,96]
new_list = sorted(list)
number = 96

result = binary_search(new_list,number)
print(result)





