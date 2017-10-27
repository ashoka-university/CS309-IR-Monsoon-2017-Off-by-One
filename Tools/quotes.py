import re


def quotes(str1):
    finallist=[]
    quotes1=re.findall(r'\"(.+?)\"',str1)#Regex Pattern match for all double quotes
    #print(str1)
    for i in quotes1:
        i=i[:-1]#Remove the quotation marks from each string
        i=i[1:]
        finallist.append(i)
    print(finallist)#output
    print(len(finallist))
    return str1;


def remove_quotes(input_string):
    string = str(input_string)
    double_quotes = re.findall(r'"[^"]*"', string, re.U)
    for quote in double_quotes:
        string.replace(quote, '')
    return string
