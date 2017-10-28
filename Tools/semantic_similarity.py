from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
import nltk.data


# returns the first letter of the pos_tag of a word
def penn_to_wn(tag):
    if tag.startswith('N'):
        return 'n'
    if tag.startswith('V'):
        return 'v'
    if tag.startswith('J'):
        return 'a'
    if tag.startswith('R'):
        return 'r'
    return None


# returns the synsets of word
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None


# returns best possible similarity score between two sentences
def sentence_similarity(sentence1, sentence2):
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))

    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]  # get the synsets
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]

    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]

    score, count = 0.0, 0

    # calculates best score for every pair of synsets based on path similarity
    for synset in synsets1:
        scores = [synset.path_similarity(ss) for ss in synsets2]
        scores = [s for s in scores if s]
        if len(scores) == 0:
            scores.append(0.0)
        best_score = max(scores)

        score += best_score
        count += 1

    score /= count
    return score


def inter_para_semantic_similarity(str1, str2):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences_from_str1 = tokenizer.tokenize(str1)
    sentences_from_str2 = tokenizer.tokenize(str2)

    score, count = 0.0, 0

    for sentence1 in sentences_from_str1:
        for sentence2 in sentences_from_str2:
            score += sentence_similarity(sentence1, sentence2)
            count += 1

    score /= count
    return score


def intra_para_semantic_similarity(str1):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences_from_str1 = tokenizer.tokenize(str1)

    num_of_sentences = len(sentences_from_str1)
    score, count = 0.0, 0

    for i in range(num_of_sentences - 1):
        for j in range(i + 1, num_of_sentences):
            score += sentence_similarity(sentences_from_str1[i], sentences_from_str1[j])
            count += 1
            print(sentences_from_str1[i], sentences_from_str1[j], score)

    score /= count
    return score
