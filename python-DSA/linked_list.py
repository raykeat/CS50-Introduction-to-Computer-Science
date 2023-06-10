class Node:

    """
    An object for storing a single node of a linked list
    Has 2 attributes - data and link to the next node in the list
    """
    data = None
    nextnode = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" %self.data

class LinkedList:
    """
    Singly linked list
    """

    #constructor method to initialize the object's attributes
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    #creating size method for the object, returns number of nodes in the list
    def size(self):
        current = self.head
        count=0

        while current:
            count+=1
            current = current.nextnode

        return count

    def add(self,data):
        """
        Add a new node containing data at the head of the list
        """

        newnode = Node(data)
        newnode.nextnode = self.head
        self.head = newnode

    def search(self,key):

        """
        Search for the first node containing data that matches the key

        Time complexity O(n)
        """
        current=self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.nextnode
        return None

    def insert(self,data,index):
        """
        inserting a node at a certain "index" specified by user

        insertion takes O(1)

        list traversal to find the node at specified index takes O(n)
        """

        #basically adding/inserting node at the head of the list
        if index == 0:
            self.add(data)

        #inserting node at some other location other than the head
        else:

            #creating new node with data provided by user
            newnode = Node(data)

            position = index
            current = self.head

            while position>1:
                current=current.nextnode
                position-=1

            prev_node = current
            next_node = current.nextnode

            prev_node.nextnode = newnode
            newnode.nextnode = next_node

    def remove(self,key):
        current = self.head
        previous = None
        found = False

        while current and not found:

            #if current.data==key and current is self.head:
               #found=True
               #self.head=current.nextnode
            #elif current.data==key:
                #found = True
                #previous.nextnode = current.nextnode
            #else:
                #previous = current
                #current = current.nextnode
        #return(current)

             #if the node to be removed is the head, we can remove the node by making the second node the head
            if current.data == key and current is self.head:
                self.head = current.nextnode
                found=True

            else:
                while True:
                    previous = current
                    current = current.nextnode
                    if current.data == key:
                        found=True
                        break

        next = current.nextnode
        previous.nextnode = next
        return(next)

    #function to include in linked_list.py file
    def node_at_index(self,index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position<index:
                current = current.nextnode
                position+=1

            return current


    def __repr__(self):
        """
        returns string representation of the linked list
        """
        nodes=[]
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" %current.data)

            if current.nextnode is None:
                nodes.append("[Tail: %s]" %current.data)
            else:
                nodes.append("[%s]" %current.data)

            current = current.nextnode
        return ' ->'.join(nodes)









