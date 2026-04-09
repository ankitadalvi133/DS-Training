#Regular Expression:
# import re
# count =0
# pattern = re.compiler("Function")
# matcher = pattern.finditer("A function or operation that can be applied multiple times without changing the result beyond the initial application. A function obtained by composing another function with itself several times.")
# for i in matcher:
#     count+=1
#     print(i.start(),".....",i.end(),".....",i.group())
# print("The number of occurrences:",count)



# import re
# count=0
# matcher=re.finditer("Hi","HiHiHiHiHiHi")
# for i in matcher:
#     count+=1
#     print(i.start(),"....",i.end(),"....",i.group())
# print("The number of occurancees:",count)



# import re
# obj = input ("Enter any character : ")
# objmatch=re.finditer(obj,"a7b @k9z")
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())



#match() Function operation:It always match beginning of string or starting of paragraph

# import re
# a = input("Enter string to perform match operation :")
# mtch = re.match(a,"python is very important language")
# print(mtch)
# if mtch!=None:
#     print("match found at beginning level")
#     print(mtch.start(), " ",mtch.end())
# else:
#     print("There is no matching at beginning level")



#fullmatch() :As a name suggest when we have to match full string with the given pattern we have to use fullmatch() if match does not then it will give none

# import re
# a = input("Enter string to perform match operation :")
# mtch = re.fullmatch(a,"pythonisvery")
# print(mtch)
# if mtch!=None:
#     print("match found ")
#     print(mtch.start(), " ",mtch.end())
# else:
#     print("There is no matching at beginning level")



#search()Function:If the match found anywhere in the string then it will return the object else it return the none

# import re
# a = input("Enter string to perform match operation :")
# mtch = re.search(a,"python sss dynamic lannn")
# print(mtch)
# if mtch!=None:

#     print(mtch.start(), " ",mtch.end()," ",mtch.group())
# else:
#     print("There is no matching anywhere")



# WAP to found a character from the text file:
# import re
# a = input("Enter string to perform match operation :")
# f = open('Day8python.txt','r')
# c = f.read()
# mtch = re.search(a,c)
# print(mtch)
# if mtch!=None:
#     print("match found ")
#     print(mtch.start(), " ",mtch.end())
# else:
#     print("There is no matching at beginning level")



# findall()function :this function return a list which containing all matches
# import re
# mtch= re.findall('[^a-zA-Z0-9]',"abch40fguhABCY$@")
# print(mtch)


#substitution():perform substitusion or replacement re.sub(expression,replacement,string) here every match pattern will be replaced by provided replacement.
# import re
# obj = re.sub('[a-zA-Z]','X','2345 ABCD Fabc deff')
# print(obj)

#op:2345 XXXX XXXX XXXX



#subn()Function:It is similar to sub() only one thing is diffrent that is also return number of replacement .This return in tuple where first element is tring and second one is number of relacement

# import re
# obj = re.subn('[0-7]','@','abcd3df5nj7')
# print(obj)
# print("The string is=",obj[0])
# print("The number of replacement is=",obj[1])

# op:The string is= abcd@df@nj@
#The number of replacement is= 3





#split()function:This function is used to split the given string as per some pattern


#WAP to check the valid mobile number

# import re
# mo = input ("Enter a mobile number :") 
# obj = re.fullmatch("[0-9]\d{9}",mo)
# if obj!=None:
#     print ("valid mobile number")
# else:
#     print("Invalid Mobile Number")


#valid gmail id or not:

# import re
# s = input("Enter Mail id: ")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m!=None:
#     print("Valid E-Mail Id")
# else:
#     print("Invalid E-mail id")




#Q.write a program to check whether the given file exits or not

# import os,sys
# fname=input("Enter File Name: ")
# if os.path.isfile(fname):
#     print("File exits:",fname)
#     f=open(fname,"r")
# else:
#     print("File does not exist:",fname)
#     sys.exit(0)
# print("This content of file is:")
# data=f.read()
# print(data)
