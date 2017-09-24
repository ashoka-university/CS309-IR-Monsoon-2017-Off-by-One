filename = input("Enter the full path of the file to be used: ")#enter the file name
input1 =open(filename,'r')
import re
str1=input1.read()#the entire file is stored in str1 variable
#print(str1)
quotes=re.findall(r'"[^"]*"',str1,re.U)#adds all quotations with ''
quotes1=re.findall(r"'[^']*'",str1,re.U)#adds all quotations with ""
finallist=[]
for i in quotes:
    i=i[:-1]
    i=i[1:]
    finallist.append(i)
for j in quotes1:
    j=j[:-1]
    j=j[1:]
    finallist.append(j)
print(finallist)#final list is entered.
