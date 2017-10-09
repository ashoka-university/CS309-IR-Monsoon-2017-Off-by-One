import Tools.pos_tagger


def check_tense(string):
    all_verbs = Tools.pos_tagger.tag(string, "verbs")
    total_verbs = len(all_verbs)
    present_verbs = len([verb for verb in all_verbs if verb[1] == "VBG" or verb[1] == "VBP" or verb[1] == "VBZ"])
    past_verbs = len([verb for verb in all_verbs if verb[1] == "VBD"])
    future_verbs = len([verb for verb in all_verbs if verb[1] == "VB"])
    return [total_verbs, present_verbs, past_verbs, future_verbs]