import re
def compute(s):
    list3=s.split('.')                  #split line as per the fullstop
    ctr1=0
    #print(list3)
    for element in list3:               # so in one particular sentence
        for e in list2:                 #go through the list of citations
            if e in element:            #if it is present in the sentence.
                str1=re.findall(r'\((.*?)\)',element)
                print(str1)
                ctr1=ctr1+1             #increment ctr1 with with one.
    print("the total:",ctr1)
with open('input.txt', 'r') as input:#this as input text
    my_list = []
    para = ''
    ctr=0
    for line in input:              # for each line in input
        temp=line.lower()           #switch characters to lower case.
        if temp=="works cited\n":   # find the works cited
            ctr=1                   #increment ctr to 1.
        if ctr==1:                  #if ctr is one
            if line != '\n':        #add line till the end
                para += line
            else:
                my_list.append(para)#my_list is list containing all lines.
                para = ''
    my_list.append(para)
list2=[]
for e in my_list:                   #for an elment e in my_list
    tem1=e.replace('.',',')         #replace a full stop with comma
    tem=tem1.partition(',')[0]      #partition with respect to the first comma in my_list
    print(tem)                      #print tem, after partition
    list2.append(tem)               #list2 is appended, with all the citations!
s="Although some medical ethicists claim that cloning will lead to designer children (Pena 12), others note that the advantages for medical research outweigh this consideration (Layton 46). The authors claim that surface reading looks at what is “evident, perceptible, apprehensible in texts” (Farmers Insurance Group 9)."
compute(s)

