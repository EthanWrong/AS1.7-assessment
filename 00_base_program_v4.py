"""Base component version of the Maori Quiz program
+ 01_collect_words_v5
+ 03_choose_language_v1
+ 06_play_round_v4

Added ability to quit while playing a round
Added tracker for how many questions left to answer
"""
import library_v2
import pprint
import random
import time


# COLLECT WORDS
# choice interpreter that checks choice is valid, and does action accordingly
def choice_selection(master):
    collections = []
    choice = input("From what collection of words would you like to learn? "
                   "\nEnter '?' for collection options >>> ").lower()

    while True:
        if choice == "all":
            master.clear()
            collections.clear()
            for i in library_v2.collections:
                master = add_collections(i, master)
                collections.append(i)
            print(f"Collections {library_v2.collections} have been added.")

        elif choice == "?":
            print(f"The available collections to learn from are: "
                  f"{', '.join(library_v2.collections)}, or 'all'")
            print()

        elif choice == "x":
            if collections:
                # print("exit choice selection")
                # print()
                break
            else:
                print("<error>, you need to pick some words")
                print()

        # checks choice is a collection name
        elif choice in library_v2.collections:
            if choice not in collections:  # checks not already chosen

                master = add_collections(choice, master)

                # adds name of collection to list that keeps track of
                # collections added
                collections.append(choice)

                print(f"Collection {choice} added")
                print()

            else:
                print("<error>, you already have added that collection")
                print()

        else:
            print("<error>, collection does not exist")
            print()

        # checks if all collections have been added to master list
        if len(collections) == len(library_v2.collections):
            print("All collections have been selected.")
            break

        # asks the user for input
        if not collections:  # if nothing has been chosen
            choice = input(
                "From what collection of words would you like to learn >>> "
                "").lower()
        else:  # is something has been chosen
            choice = input(
                "If you would like to add another collection, do so. "
                "Otherwise type 'x' >>> ").lower()

    print("Choice selection complete.")
    print()
    print(f"You chose: {', '.join(collections)}")
    return master


# adds a collection list to a master list
def merge_list(collection1, collection2):
    result = collection1 + collection2
    return result


# code that adds correct collection to master list based on choice
def add_collections(choice, master):
    if choice == "numbers":
        master = merge_list(library_v2.numbers_collection, master)

    elif choice == "days":
        master = merge_list(library_v2.days_collection, master)

    elif choice == "months":
        master = merge_list(library_v2.months_collection, master)

    else:
        print("Something went wrong.")

    return master


# CHOOSE LANGUAGE
# function that can take a question and 4 possible answers. ANSWERS CANNOT
# BEGIN WITH SAME LETTER
def abcd_checker(question, a, b, c=None, d=None):
    while True:

        # Ask the user the input question
        answer = input(f"{question.capitalize()} >>> ").lower()

        # True if answer is the answer, or first letter of answer
        if answer in (a, a[0]):
            answer = a
            return answer

        elif answer in (b, b[0]):
            answer = b
            return answer

        # answer_c and answer_d may not be set as anything
        elif c is not None and answer in (c, c[0]):
            answer = c
            return answer

        elif d is not None and answer in (d, d[0]):
            answer = d
            return answer

        # otherwise, show error
        else:
            # if c and d have not been assigned
            if c is None and d is None:
                print(f"Please answer '{a}' or '{b}'")

            # if d has not been assigned
            elif d is None:
                print(f"Please answer '{a}', '{b}', or '{c}'")

            # if all possible answers have been assigned
            else:
                print(f"Please answer '{a}', '{b}', '{c}', or '{d}'")
            print("(Just the first letter works too)")


# PLAY ROUND
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


def test_user(question, answers, question_number, language="The "
                                                           "corresponding "
                                                           "Language"):
    user_answer = input(f"{question_number}) Translate '{question}' into "
                        f"{language.capitalize()} >>> ").lower()

    # if answer is correct
    if user_answer in answers:
        print("Correct")
        correct_answers.append(
            remember_question(question, answers, user_answer))
        is_correct = True

    elif user_answer == "x":
        exit_warning = "Are you sure you want to quit? You will have to " \
                       "start " \
                       "from the top if you want to try again."
        print()
        want_to_quit = abcd_checker(exit_warning, "yes", "no")
        if want_to_quit == "yes":
            return "exit"
        else:
            is_correct = "repeat"
            return is_correct

    # if answer is incorrect
    else:
        print("Incorrect")
        print(f"The correct answer was {answers[0]}")
        mistakes.append(remember_question(question, answers, user_answer))
        is_correct = False

    # if there was more than one possible answer
    if len(answers) > 1:
        print(f"All possible answers include: {', '.join(answers)}")

    return is_correct


def remember_question(question, answers, user_answer):
    return {"question": question,  # what the question was
            "answers": answers,  # what the correct answers were
            "user_answer": user_answer}  # what the user answered


def play_round(chosen_language, master, question_number):
    # code that chooses a word-set, defines the language, then gets the question
    # and answers from that word set
    word_set = choose_word_set(master)
    language = set_language(chosen_language)

    question = get_question(word_set, language)
    answers = get_correct_answers(word_set, language)

    is_correct = test_user(question, answers, question_number, language)
    if is_correct == "exit":
        print("You ")
        return []
    elif is_correct == "repeat":
        print("Good for you.\n")
    elif is_correct:
        master.remove(word_set)
    elif not is_correct:
        master.append(word_set)

    # code that keeps track of how many questions left
    left_to_answer = len(master)
    # code that figures out if pluralised or not
    if left_to_answer == 1:
        lta_s = ""
    else:
        lta_s = "s"
    print(f"There are {left_to_answer} more question{lta_s} left to answer")
    print()

    # this code is only to display testing
    # master_display = pprint.pformat(master)
    # print(f"Master-list of word-sets to choose from: \n{master_display}")
    # print()

    return master


# TIMER
def start_timer():
    start = time.time()
    return start


def stop_timer():
    stop = time.time()
    return stop


def calc_time(start, stop):
    result = int(stop - start)
    return result


# function that returns a formatted string with the minutes and seconds
def write_min_and_sec(seconds):
    minutes = int(seconds // 60)
    and_seconds = int(seconds % 60)

    if str(minutes) != "1":
        min_s = "s"
    else:
        min_s = ""

    if str(and_seconds) != "1":
        sec_s = "s"
    else:
        sec_s = ""

    return f"{minutes} minute{min_s} and {and_seconds} second{sec_s}"


# main routine


# pre-game
# COLLECT WORDS
master_list = []  # will contain word-sets

master_list = choice_selection(master_list)
master_list_display = pprint.pformat(master_list)
print()

# CHOOSE LANGUAGE
language_choice = abcd_checker("What language would you like to answer in",
                               "maori", "english", "both")
print(f"You chose to answer in: {language_choice}")
print()


mistakes = []
correct_answers = []

# PLAY ROUND
# game mechanics / looping
i = 1
user_start = start_timer()
while len(master_list) > 0:
    master_list = play_round(language_choice, master_list, i)
    i += 1
user_stop = stop_timer()
print()

# post-game
mistakes_num = len(mistakes)
correct_num = len(correct_answers)
total_questions_answered = mistakes_num + correct_num

user_time = calc_time(user_start, user_stop)
print(f"It took you {write_min_and_sec(user_time)} to answer "
      f"{total_questions_answered} questions")
print(f"You got {correct_num} correct, and made {mistakes_num} mistakes")

