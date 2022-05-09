"""Code that picks a random question"""
import library_v2
import random


def choose_word_set(word_set_collection):
    result = random.choice(word_set_collection)
    return result


def set_language(language):
    if language == "english":
        return "english"
    elif language == "maori":
        return "maori"
    elif language == "both":
        return random.choice(("maori", "english"))
    else:
        print("<error>, invalid language chosen")


# will return a list
def get_correct_answers(word_set, language):
    return word_set[language]


# will return a string
def get_question(word_set, language):
    if language == "english":
        return word_set["maori"][0]
    elif language == "maori":
        return word_set["english"][0]

# main routine


# these variables will be set using user input in the final program
master_list = library_v2.numbers_collection
language_choice = "both"

test_word_set = choose_word_set(master_list)
test_language = set_language(language_choice)

print(get_correct_answers(test_word_set, test_language))
print(get_question(test_word_set, test_language))

