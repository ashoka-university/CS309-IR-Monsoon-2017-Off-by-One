def number_of_paragraphs(file):
    count = 0
    f = open(file).read()
    lines = f.split('\n')

    for line in lines:
        if line != "":
            count += 1
    return count


print(number_of_paragraphs("input.txt"))
