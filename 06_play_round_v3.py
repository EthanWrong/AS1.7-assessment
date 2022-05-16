"""Code taken from 04_v1 and 05_v3
This code only uses numbers, but can (and will be in the final program) be
expanded to use other word collections such as months"""
import library_v2
import random
import pprint


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


def test_user(question, answers, language="The corresponding Language"):
    user_answer = input(f"Translate '{question}' into "
                        f"{language.capitalize()} >>> ").lower()

    # if answer is correct
    if user_answer in answers:
        print("Correct")
        correct_answers.append(
            remember_question(question, answers, user_answer))
        is_correct = True

    # if answer is incorrect
    else:
        print("Incorrect")
        print(f"The correct answer was {answers[0]}")
        mistakes.append(remember_question(question, answers, user_answer))
        is_correct = False

    # if there was more than one possible answer
    if len(answers) > 1:
        print(f"All possible answers include: {', '.join(answers)}")
    print()

    return is_correct


def remember_question(question, answers, user_answer):
    return {"question": question,  # what the question was
            "answers": answers,  # what the correct answers were
            "user_answer": user_answer}  # what the user answered


def play_round(chosen_language, master):
    # code that chooses a word-set, defines the language, then gets the question
    # and answers from that word set
    word_set = choose_word_set(master)
    language = set_language(chosen_language)

    question = get_question(word_set, language)
    answers = get_correct_answers(word_set, language)

    is_correct = test_user(question, answers, language)
    if is_correct:
        master.remove(word_set)
    elif not is_correct:
        master.append(word_set)

    # this code is only to display testing
    master_display = pprint.pformat(master)
    print(f"Master-list of word-sets to choose from: \n{master_display}")

    return master


# main routine

# pre-game
master_list = library_v2.numbers_collection[:5]  # will be set using comp 01
language_choice = "english"  # will be set using component 03

mistakes = []
correct_answers = []

# game mechanics / looping
i = 1
while len(master_list) > 0:
    print(f"Question {i}: ")
    master_list = play_round(language_choice, master_list)
    i += 1

# post-game
print(f"Mistakes: {mistakes}")
print(f"Correct answers: {correct_answers}")
