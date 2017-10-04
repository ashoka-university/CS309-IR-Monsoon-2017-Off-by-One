import re
import sys, os


def term_frequency(input_text):
    frequency = {}  # dictionary to maintain freq

    text = input_text.lower()
    match_pattern = re.findall(r'\b[a-z]{1,30}\b', text)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    return frequency

