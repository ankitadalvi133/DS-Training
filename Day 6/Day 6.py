# str = "aaabbbcccc"
# A = []
# count = 1
# for i in str :
#     if i not in A:
#         A.append(i)
#     elif i in A:
#         count +=1
#     else:
#         pass
# print(A,count)



# A= "Hello World"
# print(A[::-1])


# Abtraction Concept 

# from abc import ABC, abstractmethod
# class Help4code(ABC):
#     @abstractmethod
#     def training(self):
#         pass

#     @abstractmethod
#     def placement(Self):
#         pass

# class Ankita(Help4code):
#     def training(self):
#         print("C, C++, Python")
    
#     def placement(Self):
#         print("python Placement")

# class Disha(Help4code):
#     def training(self):
#         print("C, Java, Python")
    
#     def placement(Self):
#         print("Java Placement")

# class Tanvi(Help4code):
#     def training(self):
#         print("C#, Python")
    
#     def placement(Self):
#         print("C# Placement")


# obj1 = Ankita()
# obj1.training()
# obj1.placement()


# obj2 = Disha()
# obj2.training()
# obj2.placement()

# obj3 = Tanvi()
# obj3.training()
# obj3.placement()





# from abc import ABC, abstractmethod
# class IRCTC(ABC):
#     @abstractmethod
#     def bookticket(self):
#         pass

# class Yatra(IRCTC):
#     def bookticket(self):
#         print("Welcome to Yatra")
#         source = input("Enter source station name :")
#         Destination =input("Enter Destination of Station :")
#         Date = input("Enter Date :")
#         print("==================================")

# class Makemytrip(IRCTC):
#     def bookticket(self):
#         print("Welcome to Makemytrip")
#         source = input("Enter source station name :")
#         Destination =input("Enter Destination of Station :")
#         Date = input("Enter Date :")

# class Goibibo(IRCTC):
#     def bookticket(self):
#         print("Welcome to Goibibo")
#         source = input("Enter source station name :")
#         Destination =input("Enter Destination of Station :")
#         Date = input("Enter Date :")


# obj1 = Yatra()
# obj1.bookticket()

# obj1 = Makemytrip()
# obj1.bookticket()

# obj1 = Goibibo()
# obj1.bookticket()


#  Encapsulation:
# class Base: #parent class
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "BKC"  # public data member
#         self.__c = "YBIT" #private member
    
# #Creating a derived class/child class
# class Derived(Base):
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         # print("calling private member of base class: ")
#         # print(self.a)
#         # print(self.__c)

# # obj1 = Derived()
# # print(obj1.a)
# # print(obj1.__c )

# obj2 = Base()
# print(obj2.a) #Accessible
# print(obj2.__c ) # not Accessible


# class Rbi:
#     # declaring Public Method
#     def publicPolicy(self):
#         print("Check the public policy of RBI")

#     # declaring Public Method
#     def __privatePolicy(self):
#         print("There is some private policy there is not acccessible for public")


# class Sbi(Rbi):
#     def __init__(self):     # self class const called
#         Rbi.__init__(self)      # second paraent class constr called

#     def callingPublicMethod(self):      # child class public method
#         print("\nInside Child class")   
#         self.publicPolicy()             # calling Parent class public method

#     def callingPrivateMethod(self):    # child class public method
#         self.__privatePolicy()         # calling Parent class private method

# obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()

# obj1.publicPolicy()
# obj1.__privatePolicy()

# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()

# obj2 = Rbi()
# obj2.publicPolicy()
# obj2._Rbi__privatePolicy()
        



 

# n = int(input("Enter array size: "))
# arr = []

# for i in range(n):
#     val = int(input("Enter element: "))
#     arr.append(val)

# even_list = []
# odd_list = []

# for i in arr:
#     if i % 2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)

# print("Result:", even_list + odd_list)





#DataStructure and algorithm:

#Stack Implimentation:

import sys
class Stack:
    def __init__(self):
        self.stackList =[]  #stack created 

    def push(self, value):
        self.stackList.append(value)

    def displayStack(self):
        print("------------------")
        print(self.stackList)
        print("------------------")

    def isEmpty(self):
        if self.stackList == []:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"

        else:
            return self.stackList.pop()
        
    def deleteStack(self):
        self.stackList = None
        return "Stack is deleted"
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.stackList[-1]

stackObj = Stack()

while True:
   
    print("1. Push Element In the Stack: ")
    print("2. Display Stack Element: ")
    print("3. check isEmpty")
    print("4. Pop Element :")
    print("5. Delete Stack")
    print("6. Show Top Element From Stack")
    print("7. Exit")


    choice = int(input("Enter your choice :"))
    if choice == 1:
       val = int(input("Enter The value for stack :"))
       stackObj.push(val)
    elif choice ==2:
        stackObj.displayStack()
    elif choice ==3:
        print(stackObj.isEmpty())
    elif choice ==4:
        print(stackObj.pop())
    elif choice ==5:
        print(stackObj.deleteStack())

    elif choice == 6:
        print(stackObj.peek())

    else:
        sys.exit()



