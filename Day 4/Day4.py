# print('khushipawar676'.isalnum()) 
# print('khushipawar'.isalpha())
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('KHUSHIp'.isupper())
# print('My Name Is Khushi'.istitle())
# print(''.istitle())
# print(''.isspace())
# print('Hello'.startswith("He"))
# print('Hello'.endswith("lo"))

# print("khushiankita".find("u"))
# print("khushiankita".index("i"))
# print("khushi pawar".count("a"))



#
# def exist():
#     for i in dict:
#         if i in dict.keys:
#             A.append(i)
#     print(A)

#exist()


# list = [1,2,2,3,4,3,5]
# A = {}
# count = 0

# for i in list:
#     if i not in A:
#         A.push(i)
#     else:
#         i.count +=1
# print(A)


# n1 = int(input("Enetr first no :"))
# n2 = int(input("Enetr second no :"))
# try:
#     print(n1/n2)
# except:
#     print("can't divide by zero")
# print("to be continue")


# try:
#     n1 = int(input("Enter first no :"))
#     n2 = int(input("Enter second no :"))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("enter only integer value")
# print("to be continue")


# multiple error handle in single exception
# try:
#     n1 = int(input("Enter first no :"))
#     n2 = int(input("Enter second no :"))
#     print(n1/n2)
# except(ValueError,ZeroDivisionError) as message:
#     print(message)
# print("to be continue")


#cocept of default exception block
# try:
#     n1 = int(input("Enter first no :"))
#     n2 = int(input("Enter second no :"))
#     print(n1/n2)
# except(ValueError,ZeroDivisionError) as message:
#     print('Enter correct number',message)
# except:
#     print('this is default part')
# print("to be continue")


#we can use else block if no error will be generate it is ok
# try:
#     n1 = int(input("Enter first no :"))
#     n2 = int(input("Enter second no :"))
#     print(n1/n2)
# except(ValueError,ZeroDivisionError) as message:
#     print('Enter correct number',message)
# else:
#     print('Everything is ok')



#finally block will always executed whether try block 
# generate error not
# try:
#     n1 = int(input("Enter first no :"))
#     n2 = int(input("Enter second no :"))
#     print(n1/n2)
# except(ValueError,ZeroDivisionError) as message:
#     print('Enter correct number',message)
# finally:
#     print('I will always execute')



#nested try except block
# try:
#     n1 = int(input("Enter first no :"))
#     n2 = int(input("Enter second no :"))
#     try:
#         print(n1/n2)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)



# try:
#     n1 = int(input("Enter first no :"))
#     n2 = int(input("Enter second no :"))
#     print(n1/n2)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)
# else:
#     print("there is no error in try block")
# finally :
#     print("i am finally block i always executed whether end")



# n = input("enter no")
# A = []
# count = 0
# try:
#     for i in n:
#         if i in A:
#             count +=1
#         else:
#             A.append(i) 
# except TypeError as meg :
#     print(meg)

# print(A)

# mylist = [5,7,8,3,7,8,9,2,3]
# newlist = []

# for i in range(len(mylist)):
#     count = 0
#     key = mylist[i]
    
#     j = i+1
#     while j<len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j = j+1

# print(len(newlist))


# find the second largest element
# list = [7,3,9,2,8]
# list.sort()
# print(list)
# print(list[-2])


# while loop
# i=1
# while i<=5:
#     print(i)
#     i = i+1


# username = ""
# password = ""
# while username != "admin" or password != "admin":
#     username = input("enter username:")
#     password = input("enter password:")
    
    
# name = 'Programming'
# vowels = ['a','e','i','o','u']
# con = 0
# vowel = 0
# for i in name:
#     if i in vowels:
#         vowel +=1
#     else:
#         con +=1
# print("consonent : ",con)
# print("Vowels : ",vowel)


# list = [1,2,2,3,4,2]
# A = []

# for i in list:
#     if i not in A:
#         A.append(i)
#     if i == 2:
#         A.remove(i)
    
# print(A)



# list = [2,3,4,5]

# def mul():
#     for i in list:
#         for j in list:
#             mul = i*j+1
    
#     print(mul)

# mul()   

# -----------------------------------------------------------------------
#file handaling Concept

# f = open("myfile.txt","w")
# print("name of file : ",f.name)
# print("file mode : ",f.mode)
# print("readable : ",f.readable())
# print("writable: ",f.writable())
# print("file closed : ",f.closed)
# f.close()
# print("file closed : ",f.closed)

# performing write operation and append operation
# f = open("myfile.txt","a")
# f.write("\n Nagpur is a smart city")
# f.write("\n Mumbai is a smart city")
# f.write("\n Goa is a smart city")
# f.write("\n Nashik is a smart city")
# f.close()
# print("file operation is done")

# f = open("myfile.txt","w")
# mylist = ['Ankita','khushi','Pooja']
# tuple = ('ankita','khushi','Tanvi')
# dict = {'name':'ankita','101':'khushi'}
# f.writelines(mylist)
# f.writelines(tuple)
# f.writelines(dict.values())
# f.close()
# print("file operation is done")



# f = open("myfile.txt","r")
# print(f.read())
# f.close()


# with open("myfile.txt","w") as f:
#     f.write("amit\n")
#     f.write("ankita\n")
#     f.write("khushi\n")
#     print("file closed",f.closed)
# print("file closed",f.closed)


# with open("myfile.txt","r") as f:
#     content = f.read()
#     print (content)


# f1 = open("pqr.jpg","rb")
# f2 = open("abc.jpg","wb")
# data = f1.read()
# f2.write(data)
# print("image is available with new name")

# operation with csv file
# import csv
# f = open("student.csv","a",newline="")
# a = csv.writer(f) #here it will return csvwriter object
# # a.writerow(["StudentID",'rollno','name','mobile_no'])
# StudentID = int(input("Enter the  student id:"))
# rollno = int(input("Enter the  rollno:"))
# name = input("Enter the  name:")
# mobile_no = int(input("Enter the  mobile_no:"))
# a.writerow([StudentID,rollno,name,mobile_no])
# print("student record has save") 



import csv
f = open("studentRecord1.csv","a",newline="")
a = csv.writer(f) 
# a.writerow(["rollno",'name','mobile_no','email','p1','p2','p3','total','percentage','result'])
rollno = int(input("Enter the  student rollno:"))
name = input("Enter the  student name:")
mobile_no = int(input("Enter the  student mobileno:"))
email = input("Enter the  student email:")
p1 = int(input("Enter the  p1:"))
p2 = int(input("Enter the  p2:"))
p3 = int(input("Enter the  p3:"))

total = p1+p2+p3
percentage = total/3
if p1>=40 and p2>=40 and p3>=40:
    result = "pass"
else:
    result = "fail"

a.writerow([rollno,name,mobile_no,email,p1,p2,p3,total,percentage,result])

print("student record has save")

