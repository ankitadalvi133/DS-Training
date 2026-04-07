#Print Reverse Number:
# list = [1,2,3,4,5]

# list.reverse()
# print(list)

#Palindrom:
# list = [1,2,3,2,1]

# print(list)

# print(list[::-1])

# if list == list[::-1]:
#     print("list are palindrom")
# else:
#     print("list are not  palindrom")


#return the common value in list

# list = [1,2,2,3,2,3,6,6,6,6,7,2,9,2]

# a = []
# b = []
# for i in list:
#     if i not in a:
#         a.append(i)
#     elif i not in b:
#         b.append(i)
#     else:
#         pass
# print(a)
# print(b)


#class concept:

# class Student:
#     roll_no=101 # data member
#     def studentData(self): #method/member function
#         print("Student information")

# obj = Student()
# print(obj.roll_no)
# obj.studentData()


#constructor: create a memory and initialize Datastructure
# class Demo:
#     def __init__(self):
#         print("I am constructor:")

#     def msg(self):
#         print("Hello Class !")

# obj1 = Demo()
# #print(obj1)
# obj2 = Demo()
# obj1.msg()


#Default Constructor:
# class Hod :
#     def __init__(self):
#         self.name = 'Ankita Dalvi'
#         self.age = 22
#         self.empid = 1001
    
#     def info(self):
#         print("My name is : ",self.name)
#         print("My age is : ",self.age)
#         print("My empid is : ",self.empid)

# obj = Hod()
# obj.info()


# Parameterized constructor
# class Hod :
#     def __init__(self,name,age,rollno):
#         self.name = name
#         self.age = age
#         self.rollno = rollno
    
#     def show(self):
#         print("My name is : ",self.name)
#         print("My age is : ",self.age)
#         print("My rollno: ",self.rollno)

# obj = Hod('Disha',20,101)
# obj.show()


#Variable:

# variable are assign a single object  if change the value of instance variable then only change a single object value
#
# class New:
#     def __init__(self):
#         self.a =10

# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a = 20
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


#Declaration of instance variable outside a class by using object

# class Student:
#     def __init__(self):         #constructor
#         self.s_name ="Disha"
#         self.s_rollno = 101     # declaring a instance var inside a constructor
    
#     def getdata(self):
#         self.s_mb = 987654321  # declaring a instance var inside a method

# obj = Student()
# obj.getdata()
# del obj.s_mb                   #delete the instance varibale using object 
# obj.s_branch ="CS"             #adding instance variable by using object
# print(obj.__dict__)


#Static variable # 1staticword=1 memory

# class New :
#     a = 10        #static Variable
#     def __init__(self):
#         self.name="Disha"     # instance variable
# obj1 = New()
# obj2 = New()
# obj3 = New()

# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a = 50 # New value assign
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)



#Task : CRUD 

# import sys
# class CRUD :
#     def __init__(self):
#         print("Student Management System ")
#         self.studentID = []
#         self.studentName = []
#         self.studentRollno = []
#         self.studentCity = []

#     def addStudent(self):
#         self.studentID.append(input("Enter student ID :"))
#         self.studentRollno.append(input("Enter student Roll No :"))
#         self.studentName.append(input("Enter student Name :"))
#         self.studentCity.append(input("Enter student city :"))
    
#     def show(self):
#         for i in range(len(self.studentID)):
#              print("StudentId",self.studentID)
#              print("Student RollNo ",self.studentRollno)
#              print("Student Name",self.studentName)
#              print("Student City",self.studentCity)
    

    
#     def update(self):
#         self.studentID.append(input("Enter student ID :"))
#         self.studentRollno.append(input("Enter student Roll No :"))
#         self.studentName.append(input("Enter student Name :"))
#         self.studentCity.append(input("Enter student city :"))

#     def delete(self):
#         self.studentID.append(input("Enter student ID :"))
#         self.studentRollno.append(input("Enter student Roll No :"))
#         self.studentName.append(input("Enter student Name :"))
#         self.studentCity.append(input("Enter student city :"))
    
#     def exit():
#         sys.exit()
            
# obj = CRUD()

# while True:
#         print("1.Add Student")
#         print("2.show Student")
#         print("3.Update Student")
#         print("4.delete Student")
#         print("5.Exit")

#         choice = int(input("Enter Your Choice:"))

#         if choice == 1:
#              obj.addStudent()
#         elif choice == 2:
#              obj.show()
#         elif choice == 3:
#              obj.update()
#         elif choice == 4:
#              obj.delete()
#         else:
#              obj.exit()



#Instance method

# class Student:
#     def __init__(self,name,rollno,mob):
#         self.name = name
#         self.rollno = rollno
#         self.mob = mob

#     def display(self):
#         print(self.name," ",self.rollno," ",self.mob)

# stud = Student("Disha",1,987435789)
# stud.display()



#Static method


# class Student:  
#     # by using class name we can access static method  
#     @staticmethod # decorator  
#     def get_personal_detail(firstname,lastname):  
#         print("your personal detail=",firstname,lastname)  
  
#     @staticmethod  
#     def contact_detail(mobil_no, rollno):  
#         print("your contact detail=", mobil_no,rollno)  
  
# Student.get_personal_detail("Disha", "Naik")  
# Student.contact_detail(987654321, 1001)  


# Inheritance (reusability of data)

#single inheritance 

# class College:
#     def college_name(self):
#         print("College Name : YBIT")

# class Student(College):
#     def student_info(self):
#         print("Name: Disha Naik")
#         print("Branch: CSE")

# obj = Student()
# obj.college_name()
# obj.student_info()


# Multilevel Inheritance

# class College:
#     def college_name(self):
#         print("College Name : YBIT")

# class Student(College):
#     def student_info(self):
#         print("Name: Disha Naik")
#         print("Branch: CSE")

# class Exam(Student):
#     def subject(self):
#         print("Subject1: CSS")
#         print("Subject2: MC")
#         print("Subject3: SPCC")

# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()



# Multiple Inheritance:- A subclass inherits from more than one parent class.

# class Submarks:
#     print("Enter Subject Marks ")
#     SPCC = int(input("Enter SPCC Marks : "))
#     CSS = int(input("Enter CSS Marks : "))
#     MC = int(input("Enter MC Marks : "))
#     CC = int(input("Enter CC Marks : "))

# class PractMarks:
#     print("Enter Practical Marks ")
#     cpracti = int(input("Enter CC Marks : "))

# class Result(Submarks,PractMarks):
#     def total(self):
#         if self.SPCC>=40 and self.CSS>=40 and self.MC>=40 and self.CC>=40 and self.cpracti>=20:
#             print("Pass")
#         else:
#             print("Fail")


# obj = Result()
# obj.total()



#Polymorphisum:

# class Principle:
#     def role(self):
#         print("I am managing all activity of college")

# class Dean:
#     def role(self):
#         print('Dean= I am a decision taking person')

# class Hod:
#     def role(self):
#         print('Hod= I have a responsiblelity of teacher and student')

# class Faculty:
#     def role(self):
#         print('Faculty= I have to complete sullabus sucessfully')

# def func(obj):   #called func obj =1:Dean
#     obj.role()   #calling func
# campus=[Principle(),Dean(),Hod(),Faculty()]
# for obj in campus:   #obj =[0:Principle(),1:Dean(),2:Hod()]
#     func(obj)        #calling func


# python does not support Method overloading

# class Arithmetic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)

# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)



# to handle overload method  in python 
# if method with variable no of arguments require then

# class Arithmetic:
#     def add(self,a = None, b = None, c = None):
#         if a!=None and b!= None:
#             print(a + b)
#         elif a!=None and b!= None and c!= None:
#             print(a + b + c)
#         else:
#             print("Enter at least two arguments ")

# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,4,3)



# define multiple constricyor
# constructor overloading is not possible 
# if we define multiple constructor then the last constructor will be execute

# class Arithmetic:
#     def __init__(self):
#         print("There is no arguments")
#     def __init__(self):
#         print("passing one arguments")

#     def __init__(self):
#         print("passing two arguments")

# obj = Arithmetic()
# obj = Arithmetic(10)
# obj = Arithmetic(10,10)


# python support both overriding
#1.method Overriding
#2.constructor overriding
# method overriding(parent and child relationship must be their)


# class Rbi:
#     def home_loan(self):
#         print("Home Loan : 7.5")
#     def car_loan(self):
#         print("car loan 8%")

# class Sbi(Rbi):
#     def home_loan(self):
#         print("SBI Home Loan : 6.5")
#         super().home_loan()  # using super method you can acesss the mothod of parent class in child class 

# obj = Sbi()
# obj.home_loan()


#  Constructor overriding:
# class Father:
#     def __init__(self):
#         print("FAther:= i am alrady at breakfast table")

# class Child:
#     def __init__(self):
#         print("FAther:= i will be late for breakfast")
#         # super().__init__() # it call child class constructor here

# obj = Child()