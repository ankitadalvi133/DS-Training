'''
program1:
name = "Dishanaik"
print(name[0])
print(name[1])
print(name[-1])
print(name[15])#Error
print(name[0:5])
print(name[1:])
print(name[:5])
print(name[:])
print(name[1:8:2])
print(name[::-3])

Program2:
s = "Python is a High level programming Language"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

program3:

print('Subjects Marks :')
phy = 50
chem = 60
math = 70
print("physics ={} chemistry={} Math={}".format(phy,chem,math))
print("physics ={0} chemistry={1} Math={2}".format(phy,chem,math))
print("physics ={x} chemistry={y} Math={z}".format(x=phy,y=chem,z=math))
total = phy+chem+math
print("total Marks",f"{total}")
print("Roll No=","7".zfill(4))


program4:

for i in range(1,11,2):
    print(i)
    

for i in range(1,11):
    print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)

print()
for i in range (1,11):

    print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)



Program5: 
name="racear"
for i in name:
    print(i)

program6:

name="racear"
nname=" "

for i in name:
    if i not in nname:
        nname +=i
print(name)    
    
print(nname)

Program7:Print 1to 1 in 2 range
for i in range(10,0,-2):
    print(i)

name="Mumbai"
nname = " "
n = len(name)
for i in range(n-1,-1,-1):
    nname +=name[i]

print(nname)'''


name = "racecar"
print(name)
print(name[::-1])

if name == name[::-1]:
    print("Palindrome String")

else:
    print("Not palindrome string")
