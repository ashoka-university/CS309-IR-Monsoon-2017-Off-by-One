from nltk import sent_tokenize


def sentence_count(text):
    sentences = sent_tokenize(text)
    count = len(sentences)
    return (count)
