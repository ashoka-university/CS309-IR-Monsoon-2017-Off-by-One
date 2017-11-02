from Tools import word_count
from Tools import sentence_count


def words_per_sentence(text):
    words = word_count.word_count(text)
    sentences = sentence_count.sentence_count(text)
    return (words / sentences)


def long_sentences_score(sentences, average_sentence_length):
    sentence_length = []
    for sentence in sentences:
        sentence_length.append(word_count.word_count(sentence))
    long_sentences_proportion = 0
    for length in sentence_length:
        if length > average_sentence_length:
            long_sentences_proportion += 1
    long_sentences_proportion /= len(sentences)
    return long_sentences_proportion
