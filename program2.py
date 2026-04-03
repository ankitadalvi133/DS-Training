'''math = 50 
name = "disha"
pi = 3.14
result = True'''

'''
#ID() function
print(id(math))
print(id(name))
print(id(pi))
print(id(result))
'''


'''math = 50
chem = 50
hindi = 40
print(type(math))
print(type(name))
print(type(pi))
print(type(result))
print(id(math))
print(id(chem))
print(id(hindi))'''


'''list=[[1,2,3],
      [4,5,6],
      [7,8,9]]

list[row][col]
list[0][0] = 1
list[1][1] = 3
list[2][2] = 9
if i == j:
    sum += i'''

'''print(2+2)
print("2"+"2")
val1 = int(input("Enter value of val1 :"))
val2 = int(input("Enter value of val2 :"))
print(val1 +val2)'''

'''print(int(3.14))
print(int(True))
print(int(False))
print(int("4.22"))
print(int("4"))

we cannot convert complex value to int
we acnnot convert floating point value string to int
cant convert string name to int'''

'''print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))

we can not convert complex value to float

cant convert string name to float'''
'''Complex Number:

print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))
print(complex(5,-3))
print(complex(True,False))'''

'''Bool :
print(bool(0))
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(1+2j))
print(bool(0+0j))
print(bool(-1))
print(bool(False))
print(bool(True))
print(bool("name"))
print(bool())'''

'''
val1=int(input("Enter the value for val1:"))
val2=int(input("Enter the value for val2:"))
print("Before swapping val1=",val1," val2 =",val2)
temp=val1
val1=val2
val2=temp

print("After swapping val1=",val1," val2 =",val2)'''

'''
a=int(input("Enter the value for a:"))
b=int(input("Enter the value for b:"))
c=int(input("Enter the value for c:"))
total=a+b+c
percentage=total/3.0
print("total=",total)
print("percentage=",percentage)'''

'''
p_amount = int(input("Enter principal amount :"))
roi = int(input("Enter rate of interest :"))
time = int(input("Enter duration of loan amount :"))
si = p_amount*roi*time/100
print("Simple interest=",si)'''

'''
h=float(input("Enter the height in feet h: "))

inch = h*12
cm= inch*2.54
print(inch)
print(cm)'''

'''Reverse Number Logic
num = 123
a = num % 10
num = num // 10
b= num % 10
c = num //10
rev = a*100+b*10+c*1
print(rev)'''

'''num = 123456
a = num % 10 
num = num //10
b = num % 10

num = num //10
c= num % 10
num= num //10
d = num % 10
num= num //10
e= num % 10
f= num //10
rev = a*100000+b*10000+c*1000+d*100+e*10+f*1
print(rev)'''


'''
Identity operator
a= 10
b= 15
print(a is b)
print(a is not b)'''

'''Membership operator
name ="help4code"
print("z" in name)
print("p" in name)'''

'''
no = int(input("Enter the value for val1:"))

if no>0:
    print("Positive")

if no<0:
    print("negative")

if no==0:
    print("no is 0")'''



'''
no1 = int(input("Enter the value for val1:"))
no2 = int(input("Enter the value for val1:"))
no3= int(input("Enter the value for val1:"))
no4 = int(input("Enter the value for val1:"))
no5 = int(input("Enter the value for val1:"))

if no1>no2 and no1>no3 and no1>no4 and no1>no5:
    print("no1 number is max")

if no2>no3 and no2>no4 and no2>no5:
    print("no2 number is max")

if no3>no4 and no3>no5:
    print("no3 number is max")

if no4>no5:
    print("no4 number is max")

if no5:
    print("no5 is max")
'''
'''
username = input("enter username:")
password = input("enter passwaord :")

if username == password :
    print("login successful")
else:
    print("Invalid Credential")


phy = int(input("Enter Phy Marks : "))
math = int(input("Enter math Marks : "))
chem = int(input("Enter chem Marks : "))

gender = input("enetr gender : ")

total = phy + math + chem
p = total/3.0

print(total)
print(p)

if p>=60 and gender == "m":
    print("eligible for placement")

else:
    print("eligible for data entry job")
          

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a>b:
    if a>c:
        print("a is max")
    else:
        print("c is max")
else:
    if b>c:
        print("b is max")
    else:
        print("c is max")


Day = input("Enter Day :")

if Day == "mon" or Day == "tue" or Day == "wed" or Day == "thu" or Day == "fri":
    print("working Days")
else:
    print("weekend Days")


char =ord(input("eneter char :"))

if char>=65 and char<=90:
    print("your enter a upper case")

elif char>=97 and char<=122:
    print("your enter a lower case")

elif char>=48 and char<=57:
    print("your enter a number")

else:
    print("Your enter in special symbol")'''

amount =int(input("Please Enter Amount for withdraw :"))
print("100 notes=",amount//100)
print("50 notes=",(amount%100)//100)
print("20 notes=",((amount%100)%50)//20)
print("10 notes=",(((amount%100)%50)% 20)//10)
print("5 notes=",((((amount%100)%50)% 20)%10)//5)

          
