from Tools import word_count
from Tools import sentence_count

def words_per_sentence(text):
    words = word_count.word_count(text)
    sentences = sentence_count.sentence_count(text)
    return (words/sentences)
