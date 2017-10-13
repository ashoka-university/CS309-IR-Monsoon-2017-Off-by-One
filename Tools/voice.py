import spacy


def check_voice(string):
    nlp = spacy.load('en')
    doc = nlp(string)
    active_voice = len([tok for tok in doc if (tok.dep_ == "nsubj")])
    passive_voice = len([tok for tok in doc if (tok.dep_ == "nsubjpass")])
    return [active_voice, passive_voice]


