"""
Node is user data type created for Tree Node
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
"""
entire tree functionality and operations are performed in Tree class
Tree nodes are type Node()
"""
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self,data,node):
        if node:
            if data>node.data:
                node.right=self.insert(data,node.right)
            elif data<node.data:
                node.left=self.insert(data,node.left)
            return node   
        else:
            return Node(data)
    def preorder(self,node):
            if node:
                print("node.data : ",node.data)
                self.preorder(node.left)
                self.preorder(node.right)
            else:
                return
    def postorder(self,node):
            if node:
                self.preorder(node.left)
                self.preorder(node.right)
                print("node.data : ",node.data)
            else:
                return
    def inorder(self,node):
            if node:
                self.preorder(node.left)
                print("node.data : ",node.data)
                self.preorder(node.right)
            else:
                return

if __name__=='__main__':
    n = int(input())
    tree = Tree()
    tree.root = Node(int(input()))
    for i in range(n-1):
        tree.insert(int(input("enter value : ")),tree.root)
    print("#################")
    tree.preorder(tree.root)
    
    
###########################################################
###            second way to write insert               ###
###########################################################
def insert(self,data,node):
            newNode = Node(data)
            if data<node.data:
                if node.left:
                    self.insert(data,node.left)
                else:
                    node.left = newNode
                    return
            
            elif data>node.data:
                if node.right:
                    self.insert(data,node.right)
                else:
                    node.right = newNode
                    return
                
###########################################################
###                  print tree nodes                   ###
###########################################################
def printTree(self,node):
        if node:
            self.printTree(node.left)
            
            self.printTree(node.right)
            print(node.data)
        else:
            return
            
