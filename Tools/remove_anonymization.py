def remove_ner(essay):
    words = essay.split()
    indexes = []
    i = 0
    for word in words:
        if word[0] == '@':
            indexes.append(i)
        i += 1
    indexes.reverse()
    for index in indexes:
        word = words[index]
        last_char = str(word[len(word) - 1])
        if not last_char.isalnum():
            words[index - 1] += last_char
        del words[index]

    processed_essay = ""
    for word in words:
        processed_essay += word + " "
    return processed_essay
