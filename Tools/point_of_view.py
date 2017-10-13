import Tools.pos_tagger


def check_point_of_view(string):
    first_person_pronoun_list = ["I", "me", "we", "us", "my", "our", "mine", "ours"]
    second_person_pronoun_list = ["your", "yours", "you"]
    third_person_pronoun_list = ["his", "hers", "their", "theirs", "its", "she", "he", "her", "him", "it", "they",
                                 "them"]
    number_first_person = 0
    number_second_person = 0
    number_third_person = 0
    all_pronouns = Tools.pos_tagger.tag(string, "pronouns")

    for pronoun in all_pronouns:
        if pronoun[0] in first_person_pronoun_list:
            number_first_person += 1
        elif pronoun[0] in second_person_pronoun_list:
            number_second_person += 1
        elif pronoun[0] in third_person_pronoun_list:
            number_third_person += 1

    return [number_first_person, number_second_person, number_third_person]
