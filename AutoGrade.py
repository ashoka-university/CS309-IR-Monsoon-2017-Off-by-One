import docx
from Tools import num_sentences_per_para, word_count, words_per_sentence, quotes, voice, point_of_view, tense, grammar, \
    spelling_mistakes, semantic_similarity
import numpy as np
from nltk import sent_tokenize


def get_paragraphs(filename):
    document = docx.Document(filename)
    document_paragraphs = []
    for paragraph in document.paragraphs:
        if paragraph.text:
            document_paragraphs.append(paragraph.text)
    return document_paragraphs


def get_attributes(essay_file):
    paragraphs = get_paragraphs(essay_file)
    full_text = ""
    num_of_paragraphs = len(paragraphs)
    for para in paragraphs:
        full_text += para + '\n'

    attributes = []
    # ---------------Attribute 1-----------------
    # standard deviation of number of sentences will be the value for the attribute, high is bad
    sentence_count_per_para = num_sentences_per_para.sentences_per_paragraph(paragraphs)
    sd_sent_count_per_para = np.std(np.array(sentence_count_per_para))
    attributes.append(["SD of paragraph length", sd_sent_count_per_para])

    # ---------------Attribute 2-----------------
    # |word_count/word_limit| will be the value, too high is bad
    num_of_words = word_count.word_count(full_text)
    word_limit = 200
    word_count_limit_ratio = abs(1 - (num_of_words / word_limit))
    attributes.append(["Word count limit ratio", word_count_limit_ratio])

    # ---------------Attribute 3-----------------
    # average of all sentences of length > 15
    sentences = sent_tokenize(full_text)
    sentence_length_value = words_per_sentence.long_sentences_average_length(sentences, 15)
    attributes.append(["Long sentences", sentence_length_value])

    # ---------------Attribute 4-----------------
    # voice: number of active voice sentences / total
    full_text_without_quotes = quotes.remove_quotes(full_text)
    active_voice, passive_voice = voice.check_voice(full_text_without_quotes)
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
    # Grammatical errors: num of errors / num of sentences
    grammar_error_score = grammar.check_grammar(sentences)
    grammar_error_ratio = grammar_error_score / num_of_sentences
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
        intra_paragraph_score += semantic_similarity.intra_para_semantic_similarity(quotes.remove_quotes(paragraph))
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
        first_p2 = sentences_p2[len(sentences_p2) - 1]
        last_first_sentence += semantic_similarity.inter_para_semantic_similarity(last_p1, first_p2)
        count += 1
    last_first_sentence /= count
    attributes.append(["SS last first", last_first_sentence])
    return attributes


attributes_with_values = get_attributes("Essay.docx")
