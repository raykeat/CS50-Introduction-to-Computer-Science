def mergesort(list):
    """
    Sorts a list in ascending order

    Divide: find the midpoint of the list and divide into sublists

    Conquer: Recursively sort the sublists created

    Combine:Merge the sorted sublists
    """

    if len(list)<=1:
        return list

    left,right = split(list)
    left = mergesort(left)
    right = mergesort(right)

    return merge(left,right)

def split(list):
    """
    divides the unsorted list into 2 halves and returns the left and right sublists
    """
    midpoint = len(list)//2
    lefthalf = list[:midpoint]
    righthalf = list[midpoint:]
    return(lefthalf, righthalf)

def merge(left,right):
    """
    function that merges 2 lists, sorting them in the process
    """
    i=0
    j=0
    l=list()


    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i<len(left):
        l.append(left[i])
        i+=1

    while j<len(right):
        l.append(right[j])
        j+=1

    return l

def verify_sorted(list):
    n = len(list)
    if n==0 or n==1:
        return True
    else:
        return list[0]<=list[1] and verify_sorted(list[1:])

l = [3,6,8,2,4,1,46464738,69,342,45363,4545,735,4]
l1 = mergesort(l)
print(mergesort(l1))
print(verify_sorted(l1))




def check(num1,num2):
    return num1<num2





