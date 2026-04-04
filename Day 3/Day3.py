'''num=[-1,-2,3,4]
pos=[]
neg = []

for i in num:
    if i < 0:
        neg .append(i)
    else:
        pos .append(i)

print(pos)
print(neg)
print(neg+pos)

#count the similar value
A = [1,2,2,2,3,4,2,5,2]
count = 1
B=[]
for i in A:
    if i in B:
        count +=1
    else:
        B.append(i)
print(count)'''



#Disctionary Datatype:

mydict={
    101:"Disha",
    102:"Ankita",
    "103":"Tanvi",
    "104":"Khushi",
    101:"Pooja",
    104:"Disha"
}
#print(mydict)
#with the help of key we have to print value
'''a = mydict[102]
print(a)

#replace old avlue to new:

mydict[104]="Riddhi"
print(mydict)

#only print key
for x in mydict:
    print(x)

#only print values by using the values()
for x in mydict.values():
    print(x)

#printing key and value both
for x,y in mydict.items():
    print(x,y)

#If I have add a new key value pair
mydict[105]="ABC"
print(mydict)
mydict["mobile_no"]=4235677853
print(mydict)


a = {(1,2):1,(2,3):2,(4,5):3}
print(a[4,5])


a = {'a':1,'b':2,'c':3}
print(a['a','b'])

arr ={}
arr[1]=1
arr['1']=2
arr[1] += 1
sum = 0
for k in arr:
    sum +=arr[k]
print(sum)


dict = {}
dict[1]=1
dict['1']=2
dict[1.0]=4
print(dict)
sum = 0
for k in dict:
    sum +=dict[k]
print(sum)


my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
print(my_dict)
sum = 0
for k in my_dict:
    sum +=my_dict[k]
print(sum)


box = {}
jar = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jar['jam'] = 4
crates['box'] = box
crates['jars'] = jar
print(len(crates[box]))



dict ={'c' : 97,'a' : 96,'b' : 98}
for _ in sorted(dict):
    print(dict[_])



rec ={"Name" : "Python", "Age":"20"}

print(id(rec))
r = rec.copy()
print(id(r) == id (rec))
print(id(r))

rec = {"Name": "Python", "age":"20", "addr":"NJ", "country":"USA"}
id1 = id(rec)

print(id(id1)
del rec
rec = {"Name": "Python", "age":"20", "addr":"NJ", "country":"USA"}
id2 = id(rec)
print(id(id2))
print(id1==id2)



my_dict = {'a': 10, 'b': 5, 'c': 8}

min_key = min(my_dict, key=my_dict.get)
print(min_key, my_dict[min_key])



mydict ={
    101: "Disha",
    "Professinal": "developer",
    "empid": 1001
}
mydict.pop(101)
print(mydict)


#Nested Forloop

for i in range(1,4):#outer loop for rows
    for j in range(1,4):#inner loop for column
        print(i, end = " ")
    print()#newline



n = int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range (1,1+i):
        print(j,end=" ")
    print()



n = int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range (1,1+i):
        print(chr(64+i),end=" ")#chr is the function that used for assci character
    print()



n = int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range (1,n+2-i):
        print("*",end=" ")
    print()

#op
Enter the number of rows: 5
* * * * * 
* * * * 
* * * 
* * 
* 


n = int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range (1,n+2-i):
        print(chr(64+j),end=" ")
    print()

#op
Enter the number of rows: 5
A B C D E 
A B C D 
A B C 
A B 
A 


import time
n = int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range (1,n+2-i):
        time.sleep(2) # sleep() is used for sleep for 2 sec and then print op
        print(n+1-i,end=" ")
    print()

#op
Enter the number of rows: 5
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1



import time
n = int(input("Enter the number of rows: "))
for i in range (1,n+1):
    print(" "*(n-i),end=" ")#the " "* before * it will specify the space before op
    for j in range (1,i+1):
        time.sleep(2) # sleep() is used for sleep for 2 sec and then print op
        print(n+1-i,end=" ")
    print()

#op
Enter the number of rows: 5
     5 
    4 4 
   3 3 3 
  2 2 2 2 
 1 1 1 1 1 
'''

'''

#function in python

def msg():  #called function
    print("Hello World")

msg() #calling function
msg()


def arithmatic():
    a= int(input("Enter a value of A:"))
    b= int(input("Enter a value of B:"))
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add,sub,mul,div
result = arithmatic() #calling Function
print ("arithmetic = ",result)

#op
Enter a value of A:4
Enter a value of B:2
arithmetic =  (6, 2, 8, 2.0)

#How many types of arrgument we passed in function

#1.Positional argument

def login(username,password):
    if username == password:
        print("Login sucessfully")

    else:
        print("Invalid Credantial")

username=input("Enter user name :")
password=input("Enter user password :")
login(username,password)

#op:
Enter user name :Disha
Enter user password :Disha
Login sucessfully



#2.keyword argument:

def login(username,password):
    if username == password:
        print("Login sucessfully")

    else:
        print("Invalid Credantial")

login(username="admin",password="admin")

#op
Login sucessfully



#3.default argument:

def cityName(city="Goa"):
    print(city)

cityName("Delhi")
cityName("Mumbai")
cityName()

#op:
Delhi
Mumbai
Goa



#4.variable Length Argument:

def nameOfCitys(*city):
    print("City Name's=",city)
nameOfCitys("Goa","Nagpur","Nashik","Mumbai","Pune")

#op
City Name's= ('Goa', 'Nagpur', 'Nashik', 'Mumbai', 'Pune')

#WAP for menu driven code:


import sys
def add():
    val1 =int(input("Enter a value of val1:"))
    val2 =int(input("Enter a value of val2:"))
    print("Add=",val1+val2)

def sub():
    val1 =int(input("Enter a value of val1:"))
    val2 =int(input("Enter a value of val2:"))
    print("Sub=",val1-val2)

def mul():
    val1 =int(input("Enter a value of val1:"))
    val2 =int(input("Enter a value of val2:"))
    print("Mul=",val1*val2)

def div():
    val1 =int(input("Enter a value of val1:"))
    val2 =int(input("Enter a value of val2:"))
    print("Div=",val1/val2)

while True:
    print("1.Addition")
    print("2.Substaction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice = int(input("Enter Your Choice:"))
    if choice ==1:
        add()
    elif choice ==2:
        sub()
    elif choice ==3:
        mul()
    elif choice ==4:
        div()
    elif choice ==5:
        sys.exit()


#op:
1.Addition
2.Substaction
3.Multiplication
4.Division
5.Exit
Enter Your Choice:1
Enter a value of val1:4
Enter a value of val2:7
Add= 11
1.Addition
2.Substaction
3.Multiplication
4.Division
5.Exit
Enter Your Choice:2
Enter a value of val1:5
Enter a value of val2:7
Sub= -2
1.Addition
2.Substaction
3.Multiplication
4.Division
5.Exit
Enter Your Choice:3
Enter a value of val1:1
Enter a value of val2:7
Mul= 7
1.Addition
2.Substaction
3.Multiplication
4.Division
5.Exit
Enter Your Choice:4
Enter a value of val1:6
Enter a value of val2:9
Div= 0.6666666666666666
1.Addition
2.Substaction
3.Multiplication
4.Division
5.Exit
Enter Your Choice:5


#1. rstrip()==>to remove space at right hand side
#2. lstrip()==>to remove space at left hand side
#3. strip()==>to remove space both side

programming = input ("Enter your programming name:")
p_name = programming.rstrip()
if p_name =='Python':
    print(p_name)
elif p_name == 'java':
    print(p_name)
elif p_name == 'cpp':
    print(p_name)
else:
    print("wrong Programming name")'''


#Compare the triplates

a = [5,6,7]
b = [3,6,10]

for i in a:
    for j in b:
        if i==j:
            print("both are not receive point")
        elif i>j:
            print("alice receive 1 point")
        else:
            print("bob receive 1 point")

        

