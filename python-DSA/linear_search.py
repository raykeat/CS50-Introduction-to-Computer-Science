#write functions to perform linear search of a number from a list

def linear_search(list,number):
    for i in range(len(list)):
        if list[i]==number:
            return i

#function to verify the result of linear_search function

def verify(index):
    if index is not None:
        return("Index position ",index)
    else:
        return("Number not found!")

list=[1,2,3,3,45,6,2,33,4,6,7,3]
number=6

result = linear_search(list,number)
print(verify(result))
