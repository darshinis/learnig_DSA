class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self,val):
        temp = self.head
        newNode = Node(val)
        while temp.next:
            temp = temp.next
        temp.next = newNode
    def printLl(self):
        temp = self.head
        while temp.next:
            print("{0}".format(temp.data),end=" -> ")
            temp = temp.next
        print("{0}".format(temp.data))
        
    def pickAlternative(self):
        temp = self.head
        while temp or temp.next.next:
            if temp and temp.next is not None:
                print("temp.data = ",temp.data)
                if temp.next.next is not None:
                    place = temp.next.next
                    temp.next = place
                    temp = place
                else :
                    temp.next = None
            elif temp.next is None:
                return
            else:
                return
            
            
        
if __name__ == "__main__":
    n = int(input("what size of linked list is need : "))
    ll = Linkedlist()
    ll.head = Node(int(input()))
    for i in range(n-1):
        l = int(input())
        ll.insert(l)
    ll.printLl()
    ll.pickAlternative()
    ll.printLl()
