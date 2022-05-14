"""Code taken from 04_v1 and 05_v3
This code only uses numbers, but can (and will be in the final program) be
expanded to use other word collections such as months"""
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


def test_user(question, answers, language="The corresponding Language"):
    user_answer = input(f"Translate '{question}' into "
                        f"{language.capitalize()} >>> ").lower()

    # if answer is correct
    if user_answer in answers:
        print("Correct")
        correct_answers.append(remember_question(question, answers, user_answer))

    # if answer is incorrect
    else:
        print("Incorrect")
        print(f"The correct answer was {answers[0]}")
        mistakes.append(remember_question(question, answers, user_answer))

    # if there was more than one possible answer
    if len(answers) > 1:
        print(f"All possible answers include: {', '.join(answers)}")
    print()


def remember_question(question, answers, user_answer):
    return {"question": question,  # what the question was
            "answers": answers,  # what the correct answers were
            "user_answer": user_answer}  # what the user answered


def play_round(language_choice, master):
    # code that chooses a word-set, defines the language, then gets the question
    # and answers from that word set
    word_set = choose_word_set(master)
    language = set_language(language_choice)

    question = get_question(word_set, language)
    answers = get_correct_answers(word_set, language)
    print(f"Question: {question} | Answers: {answers}")

    test_user(question, answers, language)

# main routine


master_list = library_v2.numbers_collection  # will be set using comp 01
language_choice = "both"  # will be set using component 03


mistakes = []
correct_answers = []

for i in range(1, 5):
    print(f"Round {i}: ")
    play_round(language_choice, master_list)


print(f"Mistakes: {mistakes}")
print(f"Correct answers: {correct_answers}")


