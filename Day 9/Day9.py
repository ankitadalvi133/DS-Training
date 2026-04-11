# space effeincint :  recursion : no
                    # iteration: yes  : no stack memory  requires in case of iertartion
# time effiencnt: recursion:no
#                 iteration:yes : in case of recursion syste needs more time for pop and push elements to stack memory which makes recursion less time effiencint

# easy to code :recursion:
#             iteration: we use recurion espiciallu in the case we know that problem can be divieded into simliaar sub problems

# def powerOfTwo(n):
#     if n==0:
#         return 1
#     else: 
#         power =powerOfTwo(n-1)
#         return power * 2
    


# def powerOfTwo(n):
#     i=0
#     power=1
#     while i < n:
#         power =power * 2
#         i=i+1
#     return power


#Factorial solution
# def factorial(num):
#     if num <=1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(4))


# def isPalindrome(string):
#     if len(string)==0:
#         return True
#     if string[0]==string[len(string):-1]:
#         return False
#     return isPalindrome(string[1:-1])

# print(isPalindrome("tacocat"))
# print(isPalindrome("awsome"))
# print(isPalindrome("ankita"))

# def power(base,exponent):
#     if exponent ==0:
#         return 1
#     return base * power(base,exponent-1)

# print(power(2,0))#1
# print(power(2,2))#4
# print(power(2,4))#16
#2*power(2,1)
#2*power(2,0)
#2*2*1

# def capitalizeFirst(arr):

#     result = []
#     if len(arr) == 0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car','taco','banana']))


# def productOfArray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])

# print(productOfArray([1,2,3]))#6
# print(productOfArray([1,2,3,10]))#60


#fib solution

# def fib(num):
#     if(num<2):
#         return num
#     return fib(num-1)+fib(num-2)

# print(fib(4))#3
# #print(fib(10))#55
# #print(fib(28)#317811
# #print(fib(35))#9227465

#Tree data struture
# class Tree:
#     def __init__(self,data):
#         self.data=data # instance var(create separte memory  for each obj)
#         self.children=[]

#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret="  "*level+str(self.data)+"\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret

        

# rootNode=Tree("Drinks")
# hot =Tree("Hot")
# cold =Tree("Cold")
# tea =Tree("tea")
# coffie=Tree("Coffie")
# nonAlchoholic =Tree("nonAlchoholic")
# alchoholic= Tree("alchoholic")

# rootNode.addChild(hot)
# rootNode.addChild(cold)
# hot.addChild(tea)
# hot.addChild(coffie)
# cold.addChild(nonAlchoholic)
# cold.addChild(alchoholic)

# print(rootNode)


# class Tree:
#     def __init__(self,data):
#         self.data=data # instance var(create separte memory  for each obj)
#         self.children=[]

#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret="  "*level+str(self.data)+"\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret

        

# rootNode=Tree("Drinks")
# hot =Tree("Hot")
# cold =Tree("Cold")
# tea =Tree("tea")
# coffie=Tree("Coffie")
# nonAlchoholic =Tree("nonAlchoholic")
# alchoholic= Tree("alchoholic")

# rootNode.addChild(hot)
# rootNode.addChild(cold)
# hot.addChild(tea)
# hot.addChild(coffie)
# cold.addChild(nonAlchoholic)
# cold.addChild(alchoholic)

# print(rootNode)


#binary tree 
#

#full binary tree
# each node has either 0 or 2 children
# no node has a single child


#complete binary tree
#all levels except posssibly the last are completely filled
#nodes in the last level are filled from left to right

# perfecct binary 
#all internal nodes have exactly two nodes
#all leaf are at the same level


# class Tree:
#     def __init__(self,data):
#         self.data=data # instance var(create separte memory  for each obj)
#         self.children=[]

#     def addChild(self,child):
#         self.children.append(child)

#     def __str__(self,level=0):
#         ret="  "*level+str(self.data)+"\n"
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret
    
#     def insertNode(self):
#         pass


       
# #creation of nodes
# rootNode=Tree("n1")
# n2 =Tree("n2")
# n3 =Tree("n3")
# n4 =Tree("n4")
# n5=Tree("n5")
# n9 =Tree("n9")
# n10= Tree("n10")
# n6=Tree("n6")
# n7=Tree("n7")



# rootNode.addChild(n2)
# rootNode.addChild(n3)
# n2.addChild(n4)
# n2.addChild(n5)
# n4.addChild(n9)
# n4.addChild(n10)
# n3.addChild(n6)
# n3.addChild(n7)


# print(rootNode)



# #depth first search 
# #preorder traversal : root node => left subtree => right subtree
# #inorder  : left subtree => root node => right subtree
# #post order : left subtree => right subtree => root node


# # class BSTNode:
# #     def __init__(self,data):
# #         self.data=data
# #         self.leftChild= None
# #         self.rightChild=None

# #     def insertNode(rootNode,nodeValue):
# #         if rootNode.data==None:
# #             rootNode.data=nodeValue
# #         elif nodeValue <= rootNode.data:
# #             if rootNode.leftChild is None:
# #                 rootNode.leftChild = BSTNode(nodeValue)
# #             else:




# # newBst = BSTNode(None)


# class Node:

#     # create a node in a tree
#     def __init__(self,value):
#         self.value=value
#         self.left= None
#         self.right=None

# class BinaryTree:
#     def __init__(self):
#         self.root = None# seprate memmory

        
#     def insert(self,value):
#         #insert root node in block if there is  no root node
#         if self.root is None:
#             self.root=Node(value)
#         else:
#             self.insertNode(self.root,value)


#     def insertNode(self,rootNode,value):
#         if value< rootNode.value:
#             if rootNode.left is None:
#                 rootNode.left=Node(value)
#             else:
#                 self.insertNode(rootNode.left,value)
#         else:
#             if rootNode.right is None:
#                 rootNode.right=Node(value)
#             else: 
#                 self.insertNode(rootNode.left,value)

# btObj=BinaryTree()
# btObj.insert(50)
# btObj.insert(30)
# btObj.insert(70)

# print(btObj)
