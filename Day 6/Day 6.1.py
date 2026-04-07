# #Stack without stack sizelimit Implimentation:

# import sys
# class Stack:
#     def __init__(self):
#         self.stackList =[]  #stack created 

#     def push(self, value):
#         self.stackList.append(value)

#     def displayStack(self):
#         print("------------------")
#         print(self.stackList)
#         print("------------------")

#     def isEmpty(self):
#         if self.stackList == []:
#             return True
#         else:
#             return False

#     def pop(self):
#         if self.isEmpty():
#             return "Stack is Empty"

#         else:
#             return self.stackList.pop()
        
#     def deleteStack(self):
#         self.stackList = None
#         return "Stack is deleted"
    
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is Empty"
#         else:
#             return self.stackList[-1]

# stackObj = Stack()

# while True:
   
#     print("1. Push Element In the Stack: ")
#     print("2. Display Stack Element: ")
#     print("3. check isEmpty")
#     print("4. Pop Element :")
#     print("5. Delete Stack")
#     print("6. Show Top Element From Stack")
#     print("7. Exit")


#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#        val = int(input("Enter The value for stack :"))
#        stackObj.push(val)
#     elif choice ==2:
#         stackObj.displayStack()
#     elif choice ==3:
#         print(stackObj.isEmpty())
#     elif choice ==4:
#         print(stackObj.pop())
#     elif choice ==5:
#         print(stackObj.deleteStack())

#     elif choice == 6:
#         print(stackObj.peek())

#     else:
#         sys.exit()



#Stack with stack sizelimit Implimentation:

# import sys
# class Stack:
#     def __init__(self,stackSize): #parameterized constructor
#         self.stackList =[]  #stack created 
#         self.stackSize = stackSize

#     def isFull(self):
#         if len(self.stackList) ==self.stackSize:
#             return True
#         else:
#             return False 

#     def push(self, value):
#         if self.isFull():
#             print("Stack is Full")
#         else:
#             self.stackList.append(value)

#     def displayStack(self):
#         print("------------------")
#         print(self.stackList)
#         print("------------------")

#     def isEmpty(self):
#         if self.stackList == []:
#             return True
#         else:
#             return False

#     def pop(self):
#         if self.isEmpty():
#             return "Stack is Empty"

#         else:
#             return self.stackList.pop()
        
#     def deleteStack(self):
#         self.stackList = None
#         return "Stack is deleted"
    
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is Empty"
#         else:
#             return self.stackList[-1]
# size = int(input("Enter the size of stack :"))
# stackObj = Stack(size)#stack object has created

# while True:
   
#     print("1. Push Element In the Stack: ")
#     print("2. Display Stack Element: ")
#     print("3. check isEmpty")
#     print("4. Pop Element :")
#     print("5. Delete Stack")
#     print("6. Show Top Element From Stack")
#     print("7. Exit")


#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#        val = int(input("Enter The value for stack :"))
#        stackObj.push(val)
#     elif choice ==2:
#         stackObj.displayStack()
#     elif choice ==3:
#         print(stackObj.isEmpty())
#     elif choice ==4:
#         print(stackObj.pop())
#     elif choice ==5:
#         print(stackObj.deleteStack())

#     elif choice == 6:
#         print(stackObj.peek())

#     else:
#         sys.exit()



#Tower of Hanoi:
import time
class Tower:
    
    def __init__(self):
        print("WELCOME TO TOWER OF HONOI GAME")
        print()
        print("Problem : A[1,2,3]       B[]       C[]")
        print()
        print("Goal :    A[]            B[]       C[1,2,3]")
        self.A = []
        self.B = []
        self.C = []

    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A = ",self.A)
        print("Items in Tower A\n")

    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
        print("Pass 1 Complete =====================================")

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
        print("Pass 2 Complete =====================================")
    
    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
        print("Pass 3 Complete =====================================")
    
    
    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
        print("Pass 4 Complete =====================================")

    def pass5(self):
        self.temp = self.B.pop(0)
        self.A.append(self.temp)
        time.sleep(3)
        print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
        print("Pass 5 Complete =====================================")
    
    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
        print("Pass 6 Complete =====================================")
    
    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A = ",self.A     ,"     ",    "B = ",self.B      ,"     ", "C = ",self.C)
        print("Pass 7 Complete =====================================")

    

obj1 = Tower()
obj1.tower(3)
obj1.tower(2)
obj1.tower(1)
obj1.pass1()
obj1.pass2()
obj1.pass3()
obj1.pass4()
obj1.pass5()
obj1.pass6()
obj1.pass7()




