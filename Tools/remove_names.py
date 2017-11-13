def remove_names(s):
    a=s.split()
    l=[]
    for i in a:
        if(i[0]!='@'):
            l.append(i)
    print(l)

remove_names("Shreyash krishna @Eating House") 

        
