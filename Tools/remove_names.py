import re
def remove_names(essay):
    a=essay.split()
    l=""
    for i in a:
        if(i[0]!='@'):
            l=l+i+" "
    return(l)
    #words_noun=re.findall(r'@\w+\s+',essay_string,re.U)
    #for element in essay_string:
    #    essay_string.replace(element,'')
    #print(essay_string)

s=remove_names("@Redelmeier, Donald A., @and Robert J. Tibshirani. @Association @betweend Journal of @Medicine 336 (1997): 453-58.") 
print(s)
        
