import docx
from Tools import num_sentences_per_para, word_count, words_per_sentence, quotes, voice, point_of_view, tense, grammar, \
    spelling_mistakes, semantic_similarity, sentence_count
import numpy as np
from nltk import sent_tokenize
import csv
import os


def get_paragraphs(filename):
    document = docx.Document(filename)
    document_paragraphs = []
    for paragraph in document.paragraphs:
        if paragraph.text:
            document_paragraphs.append(paragraph.text)
    return document_paragraphs


def remove_unnecessary_paragraphs(paragraphs):
    sentence_count_per_para = num_sentences_per_para.sentences_per_paragraph(paragraphs)
    indexes = []
    for i in range(len(sentence_count_per_para)):
        if sentence_count_per_para[i] < 2:
            indexes.append(i)
    for index in reversed(indexes):
        del paragraphs[index]
    return paragraphs


def get_title_citations(paragraphs):
    final_paragraphs = []
    references = []
    essay_title = ""
    para1_sent_count = sentence_count.sentence_count(paragraphs[0])
    if para1_sent_count == 1:
        essay_title = paragraphs[0]
        del (paragraphs[0])
    count = 0
    for paragraph in paragraphs:
        count += 1
        if str(paragraph).lower() in ["bibliography", "works cited", "references"]:
            break
        final_paragraphs.append(paragraph)
    for i in range(count, len(paragraphs)):
        references.append(paragraphs[i])
    return final_paragraphs, essay_title, references


def get_attributes(essay_file):
    all_paragraphs = get_paragraphs(essay_file)
    paragraphs, title, citations = get_title_citations(all_paragraphs)
    paragraphs = remove_unnecessary_paragraphs(paragraphs)
    file_name = os.path.basename(file_path)
    grade = (os.path.splitext(file_name)[0]).split()[1]

    full_text = ''
    num_of_paragraphs = len(paragraphs)
    for para in paragraphs:
        full_text += para + '\n'

    attributes = []

    # ---------------Attribute 1-----------------
    # standard deviation of number of sentences will be the value for the attribute, high is bad
    sentence_count_per_para = num_sentences_per_para.sentences_per_paragraph(paragraphs)
    # print(sentence_count_per_para)
    sd_sent_count_per_para = np.std(np.array(sentence_count_per_para))
    attributes.append(["SD of paragraph length", sd_sent_count_per_para])

    # ---------------Attribute 2-----------------
    # |word_count/word_limit| will be the value, too high is bad
    num_of_words = word_count.word_count(full_text)
    word_limit = 2000
    word_count_limit_ratio = abs(1 - (num_of_words / word_limit))
    attributes.append(["Word count limit ratio", word_count_limit_ratio])

    # ---------------Attribute 3-----------------
    # proportion of all sentences of length > 15
    sentences = sent_tokenize(full_text)
    sentence_length_value = words_per_sentence.long_sentences_score(sentences, 15)
    attributes.append(["Long sentences", sentence_length_value])

    # ---------------Attribute 4-----------------
    # voice: number of active voice sentences / total
    full_text_without_quotes = quotes.remove_quotes(full_text)
    [active_voice, passive_voice] = voice.check_voice(full_text_without_quotes)
    voice_ratio = active_voice / (active_voice + passive_voice)
    attributes.append(["Voice", voice_ratio])

    # ---------------Attribute 5-----------------
    # point of view: [1st, 2nd, 3rd]
    first, second, third = point_of_view.check_point_of_view(full_text_without_quotes)
    point_of_view_string = str(first) + "," + str(second) + "," + str(third)
    attributes.append(["Point of View", point_of_view_string])

    # ---------------Attribute 6-----------------
    # number of quotations / number of sentences
    quotes_count = quotes.quotes(full_text)
    num_of_sentences = len(sentences)
    quotes_ratio = quotes_count / num_of_sentences
    attributes.append(["Quotes ratio", quotes_ratio])

    # ---------------Attribute 7-----------------
    # tense: dominant tense verbs / total verbs
    total_verbs, present, past, future = tense.check_tense(full_text_without_quotes)
    dominant_tense_verbs = max(present, past, future)
    tense_ratio = dominant_tense_verbs / total_verbs
    attributes.append(["Tense", tense_ratio])

    # ---------------Attribute 8-----------------
    # spell errors: num of errors / num of words
    spell_errors, count, total_words = spelling_mistakes.get_spell_check_count(full_text)
    spell_errors_ratio = count / total_words
    attributes.append(["Spell errors", spell_errors_ratio])

    # ---------------Attribute 9-----------------
    # Grammatical errors: num of errors / num of words
    grammar_error_score = grammar.check_grammar(sentences)
    grammar_error_ratio = grammar_error_score / num_of_words
    attributes.append(["Grammatical Errors", grammar_error_ratio])

    # ---------------Attribute 10-----------------
    # semantic similarity: intro and conclusion
    intro_para = paragraphs[0]
    conclusion_para = paragraphs[num_of_paragraphs - 1]
    intro_conclusion = semantic_similarity.inter_para_semantic_similarity(intro_para, conclusion_para)
    attributes.append(["SS Intro Conclusion", intro_conclusion])

    # ---------------Attribute 11-----------------
    # semantic similarity of intra paragraphs
    intra_paragraph_score = 0
    for paragraph in paragraphs:
        intra_paragraph_score += semantic_similarity.intra_para_semantic_similarity(paragraph)
    intra_paragraph_score /= num_of_paragraphs
    attributes.append(["SS Intra-paragraph", intra_paragraph_score])

    # ---------------Attribute 12-----------------
    # semantic similarity of intro to all paras except conclusion
    intro_to_other_paras = 0
    for i in range(1, num_of_paragraphs - 1):
        intro_to_other_paras += semantic_similarity.inter_para_semantic_similarity(paragraphs[0], paragraphs[i])
    intro_to_other_paras /= num_of_paragraphs - 2
    attributes.append(["SS Intro to all", intro_to_other_paras])

    # ---------------Attribute 13-----------------
    # semantic similarity of conclusion to all paras except intro
    conclusion_to_other_paras = 0
    for i in range(1, num_of_paragraphs - 1):
        conclusion_to_other_paras += semantic_similarity.inter_para_semantic_similarity(
            paragraphs[num_of_paragraphs - 1],
            paragraphs[i])
    conclusion_to_other_paras /= num_of_paragraphs - 2
    attributes.append(["SS Conclusion to all", conclusion_to_other_paras])

    # ---------------Attribute 14-----------------
    # semantic similarity of last sentence of p1 and first sentence of p2
    last_first_sentence = 0
    count = 0
    for i in range(1, num_of_paragraphs - 2):
        p1 = paragraphs[i]
        p2 = paragraphs[i + 1]
        sentences_p1 = sent_tokenize(p1)
        last_p1 = sentences_p1[len(sentences_p1) - 1]
        sentences_p2 = sent_tokenize(p2)
        first_p2 = sentences_p2[0]
        last_first_sentence += semantic_similarity.sentence_similarity(last_p1, first_p2)
        count += 1
    last_first_sentence /= count
    attributes.append(["SS last first", last_first_sentence])

    attributes.append(["Grade", grade])

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


folder_path = "essays/"
docs = os.listdir(folder_path)
docs = [d for d in docs if d.endswith(".docx") and "~$" not in d]
print(docs)
for doc in docs:
    file_path = folder_path + doc
    attributes_with_values = get_attributes(file_path)
    print("------------- " + file_path + " ------------- ")
    for attr_value in attributes_with_values:
        print(attr_value)
        write_to_csv(attributes_with_values, "data.csv")
