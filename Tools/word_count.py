from textstat.textstat import textstat


def word_count(text):
    count = textstat.lexicon_count(text)
    return (count)



