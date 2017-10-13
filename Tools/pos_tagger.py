import nltk

# Tags
# CC | Coordinating conjunction |
# CD | Cardinal number |
# DT | Determiner |
# EX | Existential there |
# FW | Foreign word |
# IN | Preposition or subordinating conjunction |
# JJ | Adjective |
# JJR | Adjective, comparative |
# JJS | Adjective, superlative |
# LS | List item marker |
# MD | Modal |
# NN | Noun, singular or mass |
# NNS | Noun, plural |
# NNP | Proper noun, singular |
# NNPS | Proper noun, plural |
# PDT | Predeterminer |
# POS | Possessive ending |
# PRP | Personal pronoun |
# PRP$ | Possessive pronoun |
# RB | Adverb |
# RBR | Adverb, comparative |
# RBS | Adverb, superlative |
# RP | Particle |
# SYM | Symbol |
# TO | to |
# UH | Interjection |
# VB | Verb, base form |
# VBD | Verb, past tense |
# VBG | Verb, gerund or present participle |
# VBN | Verb, past participle |
# VBP | Verb, non-3rd person singular present |
# VBZ | Verb, 3rd person singular present |
# WDT | Wh-determiner |
# WP | Wh-pronoun |
# WP$ | Possessive wh-pronoun |
# WRB | Wh-adverb |

def tag(string, return_words):
    text_tokens = nltk.word_tokenize(string)
    tagged_words = nltk.pos_tag(text_tokens)

    if return_words == "all":
        return tagged_words

    if return_words == "nouns":
        return [tagged_word for tagged_word in tagged_words if 'NN' in tagged_word[1]]

    if return_words == "verbs":
        return [tagged_word for tagged_word in tagged_words if 'VB' in tagged_word[1]]

    if return_words == "conjunctions":
        return [tagged_word for tagged_word in tagged_words if 'CC' in tagged_word[1]]

    if return_words == "adverbs":
        return [tagged_word for tagged_word in tagged_words if 'RB' in tagged_word[1]]

    if return_words == "pronouns":
        return [tagged_word for tagged_word in tagged_words if 'PRP' in tagged_word[1]]

    if return_words == "adjectives":
        return [tagged_word for tagged_word in tagged_words if 'JJ' in tagged_word[1]]

    if return_words == "prepositions":
        return [tagged_word for tagged_word in tagged_words if 'IN' in tagged_word[1]]

    print("Second argument not defined. Returning all tagged words!")
    return tagged_words


