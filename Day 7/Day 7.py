# Dict ={"C":3,"B":2,"A":1}
# A ={}
# for i,j in Dict.items():
#     print(i,j)

#     for i in sorted(Dict):
#         print(Dict[i])
        


# DataStructure:
#Queue:

#program1:

# import sys
# class Queue:
#     def __init__(self,queueSize): #parameterized constructor
#         self.queueList =[]  #stack created 
#         self.queueSize = queueSize

#     def isFull(self):
#         if len(self.queueList) ==self.queueSize:
#             return True
#         else:
#             return False 

#     def Enqueue(self, value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.queueList.append(value)

#     def displayQueue(self):
#         print("------------------")
#         print(self.queueList)
#         print("------------------")

#     def isEmpty(self):
#         if self.queueList == []:
#             return True
#         else:
#             return False

#     def Dequeue(self):
#         if self.isEmpty():
#             return "Queue is Empty"

#         else:
#             return self.queueList.pop(0)
        
#     def deleteQueue(self):  #delete the queue
#         # self.queueList = None
#         self.queueList = []
#         return "Queue is deleted"
        
        
    
#     def peek(self):   #It returns first element of Queue
#         if self.isEmpty():
#             return "Queue is Empty"
#         else:
#             return self.queueList[0]  #slicing of list
# size = int(input("Enter the size of stack :"))
# queueObj = Queue(size)         #Queue object has created

# while True:
   
#     print("1. Enqueue Element In the Queue: ")
#     print("2. Display Queue Element: ")
#     print("3. check isEmpty :")
#     print("4. Dequeue Element :")
#     print("5. Delete Queue :")
#     print("6. Peek Operation")
#     print("7. Exit")


#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#        val = int(input("Enter The value for stack :"))
#        queueObj.Enqueue(val)
#     elif choice ==2:
#         queueObj.displayQueue()
#     elif choice ==3:
#         print(queueObj.isEmpty())
#     elif choice ==4:
#         print(queueObj.Dequeue())
#     elif choice ==5:
#         print(queueObj.deleteQueue())
#     elif choice == 6:
#         print(queueObj.peek())
#     else:
#         sys.exit()




#Timecoplexity/SpaceComplexity:

#Finding a biggest number

# def findBiggestNumber(array):
#     firstValue = array[0]----------------------------->o(1)
#     for i in range(1,len(array)):----------->o(n)
#         if array[i] >firstValue:------------>o(1)
#             firstValue = array[i]----------->o(1)
#     return firstValue 
# array =[2,4,5,6,7,1,9,3,4,5,6]
# print(findBiggestNumber(array))------------->o(1)
            
# Time complexity of above :
# O(1) + o(n) +o(1) =o(n)





# str = input("Enter a string :")
# a = []
# count = 0
# for i in a:
#     if i is int:
#         pass
#     else:
#         count+=1
    
# print(count)


#WAP for count the variable or special char

# var = 'gasggG%^&*i'
# count =0
# for i in var:
#     z = ord(i)
#     print(z)
#     if z>=97 and z<=122:
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count+=1
# print(count)





# WAP for give the from the above list the numbers are check the root number.     
# import math
# list = [2,4,5,9,16,81,144]
# count =0
# for i in list:
#     root = math.sqrt(i)
#     if root == int(root):
#         count +=1
#     else:
#         pass

# print(count)
      
   
#WAP for find the index of  number:

# def linearsearch(array, target):
#     for i in range(len(array)):
#         if array[i] == target:
#             return i
#     return -1

# array =[1,2,3,4,5,6,7,8,9]
# target = 7
# result = linearsearch(array, target)
# if result == -1:
#     print("Not Fount")
# else:
#     print("Element found at index no=" ,result)




#BinarySearch :

# def binarysearch(array,target):
#     start = 0
#     end = len(array)-1
#     while start <=end:
#         mid = (start+end) //2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             start = mid+1
#         else:
#             end = mid-1
#     return -1

# array = [1,2,3,4,5,6,7,8,9]
# target = 9
# result = binarysearch(array, target)
# if result == -1:
#     print("Not Fount")
# else:
#     print("Element found at index no=" ,result)



#LInkedList:

#WAP for add a node in begging

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None


# linkedlist =LinkedList()

# linkedlist.head = Node(5) #First Node 
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)


# #linking part
# linkedlist.head.next = second
# second.next = third
# third.next  = fourth

# print(linkedlist.head.data)#when we pass the head.next it give the address of next
# print(second.data)
# print(third.data)
# print(fourth.data)

# #display LinkedList
# while linkedlist.head !=None:
#     print("|",linkedlist.head.data,"",linkedlist.head.next,end =" ")
#     linkedlist.head = linkedlist.head.next


import sys
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #add Node
    def addNode(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def displayNode(self):
        print("------------------")
        while self.head is not None:
            print(self.head.data,'|', self.head.next,'->',end =" ")
            self.head = self.head.next
        print("------------------")
    
    def addNodeBeginning(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def addNodeBetween(self,index,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self .tail = node
        elif index ==0:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            node.next = temp.next
            temp.next = node

    def deleteNode(self):
        pass





if __name__ == '__main__':
    object = LinkedList()

    while True:
        print('1. Add node in LinkedList ')
        print('2. Add node in Begining ')
        print('3. Add node in Between ')
        print('4. Add node in End ')
        print('5. Display Linked List ')
        print('6. Display Linked List ')
        print('7. Exit ')

        ch = int(input('Enter your Choice : '))

        if ch == 1:
            value = int(input('Enter Value : '))
            object.addNode(value)
            print("Node added sucessfully in single Linkedlist")

        elif ch == 2:
            value = int(input('Enter Value : '))
            object.addNodeBeginning(value)

        elif ch == 3:
            value = int(input('Enter Value : '))
            index = int(input('Enter Value of index : '))
            object.addNodeBetween(index,value)
            print('Node added sucessfully in Between')

           

        elif ch == 5:
            object.displayNode()
        elif ch == 6:
            index = int(input('Enter Value of index : '))
            object.deleteNode(index)
        elif ch == 7:
            sys.exit()
