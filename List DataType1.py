'''mylist = ["Disha","Ankita",44,"Khushi","Tanvi","Pooja",55]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[3:5])
print(mylist[:4])
print(mylist[1:])
print(mylist[1:8:3])
print(mylist[:])
print(mylist[::-1])

mylist[2]="Akshay"
print(mylist)

if "Disha" in mylist:
    print("Yes Disha is available ")

else:
    print(" Disha is not available ")

mylist.append("ABC")
print(mylist)

mylist.insert(4,"riddhi")
print(mylist)

mylist.remove(44)
print(mylist)


mylist.copy()
print(mylist)

mylist = [['Disha','Naik'],['85.56'],[440022,"yyy"]]
print("Example of Multidimensional list: ")
print(mylist)
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])


list=["Disha","Naik"]
print(list*2)

list2=[50,25.50]
print(list+list2)

del list2
print(list2)

name = "Disha"
print(name)
mylist=list(name)
print(mylist)

mylist = [40,30,20,10]
mylist.reverse()

print(mylist)

mylist = [44,22,33,0,6,4]
mylist.sort(reverse=True)
print(mylist)


mylist = [44,22,33,0,6,4]
newlist = mylist
print(id(mylist))

print(id(newlist))
mylist[0]="Disha"
print(mylist)
print(newlist)


Pop operation:
    
arr =[[1,2,3,4],
      [4,5,6,7],
      [7,8,9,10],
      [10,11,12,13]]
for i in range (0, 4):
    print(arr[i].pop())

arr = [1,2,3,4,5,6]
for i in range (1, 6):
    arr[i-1] = arr[i]# i-1 so the position is 1=2
for i in range (0, 6):
    print(arr[i], end = " ")

#collection Datastructure
a = [1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50,60
print(a)

a=[1,2,3,4,5]
print(a[3:0:-1])


#Tuple operation

mytuple = ("Disha","Ankita",44,"Khushi","Tanvi","Pooja",55)
print(mytuple)
print(type(mytuple))

mytuple[2]="sunil"
print(mytuple)


init_tuple = ()
print(init_tuple.__len__())
print(type(init_tuple))

#op:0


init_tuple_a = 'a','b'
init_tuple_b = ('a','b')
print(id(init_tuple_a))
print(id(init_tuple_b))
print(init_tuple_a == init_tuple_b)



init_tuple_a = '1','2'
init_tuple_b = ('3','4')
print(init_tuple_a+init_tuple_b)


init_tuple =('Python',)*3
print(type(init_tuple))
#op the output is 'str' and after giving the (,) the output will be tuple



init_tuple =(1,)*3
init_tuple[0] = 2
print(init_tuple)


init_tuple = ((1,2),)*7
print(len(init_tuple[3:8]))


names =[4,2,5,6,8,2]
for i in names:
    print(i)



#Task
A=[4,0,2,5,0,1]
for i in A:
    if i ==0:
        A.remove(i)
        A.append(i)
print(A)

#op:[4, 2, 5, 1, 0, 0]

A = [1,2,2,3,4,4,5]
B = []
for i in A:
    if i not in B:
        B.append(i)
print(B)

# find common value
A = [1,2,3]
B = [2,3,4]
C = [3,4,5]

for i in A:
    for j in B:
        for k in C:
            if i == j and j==k:
                print(i)


# OR

A = [1,2,3]
B = [2,3,4]
C = [3,4,5]

for i in A:
    if i in B and i in C:
        print(i)
op:3
 

#sum of distancebetween value

n = int(input("Enter size of array "))
arr = []
for i in range(n):
    val = int(input("Enter value"))
    arr.append(val)
sum = 0
print(arr)


for i in range(n):
    if i+1 in range(n):
        sum += abs(arr[i]-arr[i+1])#abs function is used to change nigative number to positive
  

print(sum)

#break and Continue

for i in range(1,5): 
    if i == 3:
        break
    print(i)

for i in range(1,5): 
    if i == 3:
        continue
    print(i)


#zip()
Reverse the number

for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i, "  ",j)


#task 
input = "prashant*is*a*good*programer"
newname=""
val=''

for i in input:
    if i!="*":
        newname+=i
    else:
        val+=i
print(newname)
print(str(val+newname))

op:
    prashantisagoodprogramer
****prashantisagoodprogramer

#bodmost 
a=50
b=30
c=20
d=10
print((a+b)*c/d)
print((a-b)*c/d)
print(a+(b*c)/d)   

#op
160.0
40.0
110.0

x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]
print(id(x))
print(id(y))
print(id(z))
print(x==y)
print(x==z)
print(x != z)

op:
    2148946806976
2148932500480
2148948059520
True
False
True

#Anagram pr

A= "listen"
B = "silent"


if sorted(A) == sorted(B):
    print("anagram")
else:
    print("not")
        
 '''

#count word in string
name = "Welcome to YBIT"

count=1

for i in name:
    if i==" ":
        count +=1
print (count)


