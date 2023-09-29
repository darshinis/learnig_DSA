class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insertAtStart(self,val):
        temp = self.head
        newNode = Node(val)
        newNode.next =temp
        self.head = newNode
        
    def insertAtEnd(self,val):
        temp = self.head
        newNode = Node(val)
        while temp.next:
            temp = temp.next
        temp.next = newNode
     
    def insertAftertheNode(self,node,val):
        newNode = Node(val)
        newNode.next = node.next
        node.next = newNode
        
    def printLl(self):
        temp = self.head
        while temp.next:
            print("{0}".format(temp.data),end=" -> ")
            temp = temp.next
        print("{0}".format(temp.data))
        
      
if __name__ == "__main__":
    
    ######## inserion at the Start of ll ########
    n = int(input("what size of linked list is need : "))
    ll = Linkedlist()
    ll.head = Node(int(input()))
    for i in range(n-1):
        l = int(input())
        ll.insertAtStart(l)
    ll.printLl()
    
    """
    ######## inserion at the end of ll ########
    n = int(input("what size of linked list is need : "))
    ll = Linkedlist()
    ll.head = Node(int(input()))
    for i in range(n-1):
        l = int(input())
        ll.insertAtEnd(l)
    ll.printLl()
    
    """
    
