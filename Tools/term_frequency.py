import re
import sys, os


def term_frequency(file_path):
    frequency = {}  # dictionary to maintain freq
    file_content = open(file_path, 'r')
    text = (file_content.read()).lower()
    match_pattern = re.findall(r'\b[a-z]{1,30}\b', text)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    return frequency


directory_path = sys.argv[1]
files = os.listdir(directory_path)

for file in files:
    if file.endswith(".txt"):
        print("------ File: " + file + " ------ ")
        print(term_frequency(directory_path + os.sep + file))
