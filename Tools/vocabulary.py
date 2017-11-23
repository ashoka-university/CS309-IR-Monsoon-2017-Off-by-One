from nltk import word_tokenize
from nltk.corpus import stopwords


def get_vocab(input_text):
    input_text = input_text.lower()

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(input_text)

    size = len(word_tokens)
    indexes = []

    for i in range(size):
        if len(word_tokens[i]) < 2:
            indexes.append(i)

    indexes.reverse()
    for index in indexes:
        del word_tokens[index]

    vocabulary = []

    for w in word_tokens:
        if w not in stop_words and w not in vocabulary:
            vocabulary.append(w)

    return vocabulary, len(vocabulary)
