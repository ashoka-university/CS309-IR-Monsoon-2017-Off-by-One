import language_check
import nltk


def check_grammar_of_str(string):
    tool = language_check.LanguageTool('en-US')
    matches = tool.check(string)
    score = 0
    for match in matches:
        if not match.ruleId == "MORFOLOGIK_RULE_EN_US":  # do not count any spell errors
            score += 1
    return score


def check_grammar(sentences):
    score = 0
    for sentence in sentences:
        score += check_grammar_of_str(sentence)
    return score
