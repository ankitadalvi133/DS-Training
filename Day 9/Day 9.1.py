
class Node:

    # create a node in a tree
    def __init__(self,value):
        self.value=value
        self.left= None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root = None# seprate memmory

        
    def insert(self,value):
        #insert root node in block if there is  no root node
        if self.root is None:
            self.root=Node(value)
        else:
            self.insertNode(self.root,value)


    def insertNode(self,rootNode,value):
        if value< rootNode.value:
            if rootNode.left is None:
                rootNode.left=Node(value)
            else:
                self.insertNode(rootNode.left,value)
        else:
            if rootNode.right is None:
                rootNode.right=Node(value)
            else: 
                self.insertNode(rootNode.left,value)

btObj=BinaryTree()
btObj.insert(50)
btObj.insert(30)
btObj.insert(70)

print(btObj)
print(BinaryTree)
