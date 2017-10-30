import enchant

start_list = ['"', '(', '"(', '("']
end_list = ['.', ',', '/', '?', '!', ';', ':', ')', '...', '".', '",', '?"', '!"', '";', ':"', ';"', '":', '")', ')"',
            '..."']
user_list = ['Ambedkar', 'Gandhi', 'Caste']
dictionary = enchant.Dict("en_UK")


def user_list_check(word):
    for item in user_list:
        if word == item:
            return True
        else:
            return False


def spell_check(alpha_words):
    spelling_errors = []
    for word in alpha_words:
        if word:
            if (not dictionary.check(word) and (not user_list_check(word))):
                spelling_errors.append(word)
    return spelling_errors, len(spelling_errors)


def remove_punctuation(non_alpha_word):
    for item in end_list:
        if non_alpha_word.endswith(item):
            non_alpha_word = non_alpha_word[:len(item)]
    for item in start_list:
        if non_alpha_word.startswith(item):
            non_alpha_word = non_alpha_word[len(item):]
    return non_alpha_word


def get_spell_check_count(text):
    words = text.split()

    final_alpha_words = []

    for word in words:
        if not word.isalpha():
            word = remove_punctuation(word)
        final_alpha_words.append(word)
    spell_errors, count = spell_check(final_alpha_words)
    return spell_errors, count, len(final_alpha_words)
