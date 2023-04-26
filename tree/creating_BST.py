class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self,data,node):
        if node:
            if data>node.data:
                node.right=self.insert(data,node.right)
            elif data<node.data:
                node.left=self.insert(data,node.left)
        else:
            return Node(data)
    def preorder(self,node):
            
            print("node.data : ",node.data)
            self.preorder(node.left)
            self.preorder(node.right)

n = int(input())
tree = Tree()
tree.root = Node(int(input()))
print("tree.root : ",tree.root.data)
for i in range(n-1):
    tree.insert(int(input("enter value : ")),tree.root)
print("tree.root.data : ",tree.root.data)
print("tree.root.data : ",tree.root.left.data)
print("tree.root.data : ",tree.root.right.data)
print("#################")
tree.preorder(tree.root)
    
            
