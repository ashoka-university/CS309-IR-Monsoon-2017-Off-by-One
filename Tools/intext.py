import re    
with open('input.txt', 'r') as input:
    my_list = []
    para = ''
    ctr=0
    for line in input:
        temp=line.lower()
        #print(temp)
        if temp=="works cited\n":
            ctr=1
        if ctr==1:
            if line != '\n':
                para += line
            else:
                my_list.append(para)
                para = ''
    my_list.append(para)
list2=[]
for e in my_list:
    tem1=e.replace('.',',')
    tem=tem1.partition(',')[0]
    print(tem)
    list2.append(tem)
s="Although some medical ethicists claim that cloning will lead to designer children (Pena 12), others note that the advantages for medical research outweigh this consideration (Layton 46). The authors claim that surface reading looks at what is “evident, perceptible, apprehensible in texts” (Farmers Insurance Group 9)."
list3=s.split('.')
ctr1=0
print(list3)
for element in list3:# so in one particular sentence
    for e in list2:#go through the list of citations
        if e in element:#if it is present
            str1=re.findall(r'\((.*?)\)',element)
            print(str1)
            ctr1=ctr1+1
print("the total:",ctr1)
