import re


def quotes(str1):
    finallist = []
    quotes1 = re.findall(r'"[^"]*"', str1, re.U)  # Regex Pattern match for all double quotes
    for i in quotes1:
        i = i[:-1]  # Remove the quotation marks from each string
        i = i[1:]
        finallist.append(i)
    return len(finallist)


def remove_quotes(input_string):
    string = str(input_string)
    double_quotes = re.findall(r'"[^"]*"', string, re.U)
    for quote in double_quotes:
        string.replace(quote, '')
    return string
