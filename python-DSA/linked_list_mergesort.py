#from linked_list.py file import class LinkedList
from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    -Recursively divide the linked list into sublists containing a single node
    -Repeatedly merge the sublists to produce sorted sublists until only one remains
    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half,right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

#implementing split function
def split(linked_list):
    """
    divide the unsorted linked list at midpoint into 2 sublists
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half,right_half
    else:
        size = linked_list.size()
        midpoint = size//2
        midnode = linked_list.node_at_index(midpoint-1)

        left_half = linked_list

        #creating an empty linked list
        right_half = LinkedList()
        right_half.head = midnode.nextnode

        #severing connection between midnode and right half
        midnode.nextnode= None

        return left_half,right_half


#implementing merge function
def merge(left,right):
    """
    Merges 2 linked lists according to data in the nodes

    Retursn new merged linked list
    """

    #creating the new linked list
    merged_list = LinkedList()

    #adding a fake head that is discarded later
    merged_list.add(2)

    current = merged_list.head

    # head of left linked list
    left_head = left.head

    #head of right linked list
    right_head = right.head

    #iteration through left and right lists to merge them
    while left_head or right_head:

        if left_head is None:
            current.nextnode = right_head
            #terminating condition which sets right head to None
            if right_head is not None:
                right_head = right_head.nextnode

        if right_head is None:
            current.nextnode = left_head
            #terminating condition which sets left head to None
            if left_head is not None:
                left_head = left_head.nextnode


        #scenario where neither left nor right head are None(haven't arrived at tail for either left or right linked list)
        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data<=right_data:
                current.nextnode = left_head
                left_head = left_head.nextnode
            else:
                current.nextnode = right_head
                right_head = right_head.nextnode

        current = current.nextnode

    # discard fake head and set next node as head
    merged_list.head = merged_list.head.nextnode

    return merged_list

l = LinkedList()
l.add(32)
l.add(2)
l.add(678)
l.add(29)
l.add(2636)
m = merge_sort(l)
print(m)
