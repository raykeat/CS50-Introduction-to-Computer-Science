#creating a ListNode class
class ListNode:
  def __init__(self,val,next=None):
    self.val = val
    self.next = next

#creating a Linked List class
class LinkedList:
  def __init__(self,val):
    self.head = ListNode(val)


  def __repr__(self):
        """
        returns string representation of the linked list
        """
        nodes=[]
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" %current.val)

            elif current.next is None:
                nodes.append("[Tail: %s]" %current.val)
            else:
                nodes.append("[%s]" %current.val)

            current = current.next
        return ' ->'.join(nodes)



  def add(self, val):
      newnode = ListNode(val)
      if self.head is None:
          self.head = newnode
      else:
          current = self.head
          while current.next is not None:
              current = current.next
          current.next = newnode



#function to merge the 2 lists
def mergelists(list1: ListNode, list2: ListNode)->ListNode:
  #creating a dummy Node
  dummy = LinkedList(0)
  dummy.next = None

  current = dummy
  while list1 and list2:
    if list1.val<=list2.val:
      current.next = list1
      list1 = list1.next
      current = current.next
    else:
      current.next = list2
      list2 = list2.next
      current = current.next
  if list1:
    current.next = list1
  else:
    current.next = list2

  head = dummy.next
  return head

list1 = LinkedList(2)
list1.add(3)
list1.add(4)
list1.add(5)

list2 = LinkedList(2)
list2.add(4)
list2.add(5)
list2.add(8)

mergedlist_head = mergelists(list1.head,list2.head)
mergedlist = LinkedList(mergedlist_head.val)
current = mergedlist_head.next
while current:
   mergedlist.add(current.val)
   current = current.next
print(mergedlist)

