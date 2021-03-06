from Tools import word_count, words_per_sentence, voice, tense, grammar, spelling_mistakes, semantic_similarity, \
    vocabulary
from nltk import sent_tokenize
import csv
from openpyxl import load_workbook
import math
import os


def get_attributes(topic_essay, full_essay, word_limit):
    attributes = []

    # ---------------Attribute 1-----------------
    # |word_count/word_limit| will be the value, too high is bad
    num_of_words = word_count.word_count(full_essay)
    word_count_limit_ratio = abs(1 - (num_of_words / word_limit))
    attributes.append(["Word count", num_of_words])
    attributes.append(["Word count limit ratio", word_count_limit_ratio])

    # ---------------Attribute 2-----------------
    # proportion of all sentences of length > 15
    sentences = sent_tokenize(full_essay)
    attributes.append(["Sentence count", len(sentences)])
    sentence_length_value = words_per_sentence.long_sentences_score(sentences, 15)
    attributes.append(["Long sentences", sentence_length_value])

    # ---------------Attribute 3-----------------
    # voice: number of active voice sentences / total
    [active_voice, passive_voice] = voice.check_voice(full_essay)
    voice_ratio = 0
    if active_voice + passive_voice != 0:
        voice_ratio = active_voice / (active_voice + passive_voice)
    attributes.append(["Voice", voice_ratio])

    # ---------------Attribute 4-----------------
    # tense: dominant tense verbs / total verbs
    total_verbs, present, past, future = tense.check_tense(full_essay)
    dominant_tense_verbs = max(present, past, future)
    tense_ratio = 0
    if total_verbs != 0:
        tense_ratio = dominant_tense_verbs / total_verbs
    attributes.append(["Tense", tense_ratio])

    # ---------------Attribute 5-----------------
    # spell errors: num of errors / num of words
    spell_errors, count = spelling_mistakes.get_spell_errors_count(full_essay)
    spell_errors_ratio = count / num_of_words
    attributes.append(["Spell errors", spell_errors_ratio])

    # ---------------Attribute 6-----------------
    # Grammatical errors: num of errors / num of words
    grammar_error_score = grammar.check_grammar(sentences)
    grammar_error_ratio = grammar_error_score / num_of_words
    attributes.append(["Grammatical Errors", grammar_error_ratio])

    # ---------------Attribute 7-----------------
    # semantic similarity of the whole essay
    essay_semantic_similarity = semantic_similarity.intra_para_semantic_similarity(full_essay)
    num_of_sentences = len(sentences)
    essay_semantic_similarity = essay_semantic_similarity * (math.log(num_of_sentences, 2))
    attributes.append(["SS Essay", essay_semantic_similarity])

    # ---------------Attribute 8-----------------
    # semantic similarity of the topic and essay
    topic_essay_semantic_similarity = semantic_similarity.inter_para_semantic_similarity(topic_essay, full_essay)
    topic_essay_semantic_similarity = topic_essay_semantic_similarity * (math.log(num_of_sentences, 2))
    attributes.append(["SS Topic Essay", topic_essay_semantic_similarity])
    #
    # ---------------Attribute 9-----------------
    # vocabulary
    vocabulary_words, vocabulary_size = vocabulary.get_vocab(full_essay)
    attributes.append(["Vocabulary", vocabulary_size / word_limit])

    return attributes


def write_to_csv(attr_with_values, csv_file_path):
    attrs = [attr[0] for attr in attr_with_values]
    empty = True
    with open(csv_file_path) as csvfile:
        reader = csv.reader(csvfile)
        if (len(list(reader))) > 1:
            empty = False

    with open(csv_file_path, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=attrs)
        if empty:
            writer.writeheader()
        data = {}
        for attr in attr_with_values:
            data[attr[0]] = attr[1]
        writer.writerow(data)


def train_data():
    file_path = "Data/valid_set_set8.xlsx"
    wb = load_workbook(filename=file_path, read_only=True)
    ws = wb['valid_set']

    for row in ws.rows:
        essay_id = row[0].value
        essay_set = row[1].value
        essay = row[2].value
        score = row[3].value
        topic = ""
        if essay_set == 8:
            topic = "If you want a place in the sun, you will have to expect some blisters."
            print("------------------------------------------------------")
            print(essay_id)
        if topic != "":
            word_limit = 800
            attributes_with_values = get_attributes(topic, essay, word_limit)
            attributes_with_values.append(["Score", score])
            attributes_with_values.append(["Essay ID", essay_id])
            attributes_with_values.append(["Essay Set", essay_set])
            write_to_file = "data_test_set8.csv"
            write_to_csv(attributes_with_values, write_to_file)


# train_data()