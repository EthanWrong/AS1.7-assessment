"""Base component version of the Maori Quiz program
+ 01_collect_words_v5
+ 03_choose_language_v1
+ 06_play_round_v4
+ 07_timer_v3
+ 09_welcome_instructions_v1
+ 10_review_mistakes_v5
+ 11_pluraliser_v1
- 11_pluraliser_v1 (moved to 12_text_decoration)
+ import text_decoration
+ adjust text formatting for collection selection & language selection


To add (maybe):
Only need to type first letter of collection to add in pre-game phase
Entering a '?' while translating does not mean a mistake, but a question
that you didn't know?
Add an easter-egg 'default settings' that skips all the pregame stuff and
chooses numbers collection and sets language to english

To do:
Global indent in instructions + concisify
Text-decorate from Quiz Time onwards
"""
import library_v2
import pprint
import random
import time
import text_decorator


# COLLECT WORDS
# choice interpreter that checks choice is valid, and does action accordingly
def choice_selection(master):
    collections = []
    choice = input(f"{GLOBAL_INDENT}From what collection of words would you "
                   f"like to learn? \n{GLOBAL_INDENT} Enter '?' for "
                   f"collection options >>> ").lower()

    while True:
        if choice == "all":
            master.clear()
            collections.clear()
            for i in library_v2.collections:
                master = add_collections(i, master)
                collections.append(i)
            print_text = f"Collections {', '.join(collections)} added"
            text_decorator.print_centre(2, print_text, 71, "+")

        elif choice == "?":

            print()

            print(f"{GLOBAL_INDENT}The available collections to learn from "
                  f"are:\n{GLOBAL_INDENT} {', '.join(library_v2.collections)},"
                  f" or 'all'")

        elif choice == "x":
            if collections:
                # print("exit choice selection")
                # print()
                break
            else:
                print(f"{GLOBAL_INDENT}You do have to pick SOME words, silly")

        # checks choice is a collection name
        elif choice in library_v2.collections:
            if choice not in collections:  # checks not already chosen

                master = add_collections(choice, master)

                # adds name of collection to list that keeps track of
                # collections added
                collections.append(choice)

                print_text = f"Collection {choice.upper()} added"
                text_decorator.print_centre(2, print_text, 40, "+")

            else:
                print(f"{GLOBAL_INDENT}You have already added that collection")

        else:
            print(f"{GLOBAL_INDENT}Sorry, but that collection does not exist")

        print()

        # checks if all collections have been added to master list
        if len(collections) == len(library_v2.collections):
            print(f"{GLOBAL_INDENT}All collections have been added")
            break

        # asks the user for input
        if not collections:  # if nothing has been chosen
            choice = input(f"{GLOBAL_INDENT}From what collection of words "
                           f"would you like to learn? >>> ").lower()

        else:  # is something has been chosen
            choice = input(f"{GLOBAL_INDENT}If you would like to add another "
                           f"collection, do so.\n{GLOBAL_INDENT} Otherwise "
                           "type 'x' >>> ").lower()

    print(f"{GLOBAL_INDENT}<< Choice selection COMPLETE >> ")
    print()
    print_text = f"You chose: {', '.join(collections)}"
    text_decorator.print_surrounding(2, 6, print_text, 75, ":")
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
        answer = input(f"{GLOBAL_INDENT}{question.capitalize()} >>> ").lower()

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
                print(f"{GLOBAL_INDENT}  Please answer '{a}' or '{b}'")

            # if d has not been assigned
            elif d is None:
                print(f"{GLOBAL_INDENT}  Please answer '{a}', '{b}', or '{c}'")

            # if all possible answers have been assigned
            else:
                print(f"{GLOBAL_INDENT}  Please answer '{a}', '{b}', '{c}', "
                      f"or '{d}'")
            print(f"{GLOBAL_INDENT}  < Initial also works >")
            print()


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
        print(f"{GLOBAL_INDENT}<error>, invalid language chosen")


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
        print(f"The correct answer was {answers[0].upper()}")
        user_mistakes.append(remember_question(question, answers, user_answer))
        is_correct = False

    # if there was more than one possible answer
    if len(answers) > 1:
        print(f"All possible answers include: {', '.join(answers).upper()}")

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
        print("Game over.")
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

    # if str(minutes) != "1":
    #     min_s = "s"
    # else:
    #     min_s = ""
    #
    # if str(and_seconds) != "1":
    #     sec_s = "s"
    # else:
    #     sec_s = ""

    return f"{minutes} minute{pluraliser(minutes, 's')} and {and_seconds} " \
           f"second{pluraliser(and_seconds, 's')}"


# WELCOME INSTRUCTIONS
def instructions():
    print("PRE-GAME")
    print("You will be able to select different collections of words to \n"
          "learn from. Simply choose all the collections you would like to \n"
          "learn, then exit collection selection.\n"
          "You will then choose which language you would like to answer "
          "in:\n You can choose Maori, English, or Both. \n"
          "Simply enter a language and the quiz will begin.")
    print("\nTHE QUIZ")
    print("You will be asked to translate a word from either Maori or "
          "English.\nSimply enter the word.\nIf you are unsure of the word, "
          "enter '?' so that it doesn't count as incorrect.\nHowever, "
          "two more instances of the word will be added for "
          "practice.\nLikewise if you make a mistake, two more instances of "
          "the word will be added for practice.\nIf you wish to stop "
          "playing, simply enter 'x' and you will exit the game. "
          "\nOtherwise, try to answer all the questions!")
    print("\nPOST-GAME")
    print("First, you will be shown all your stats, such as time, questions \n"
          "answered, and mistakes. If you wish to review your mistakes in "
          "\nMore detail, feel free to do so, and you will get information \n"
          "about which questions you struggled the most with.")
    print("\nThat is all the information you need to know, enjoy the game!")
    print()


def welcome():
    print("WELCOME TO the *MAORI QUIZ*")
    print("Learn Te Reo Maori fast.")
    print()


# REVIEW MISTAKES
# makes a list from the values of a given key in a dict
def create_list_from_dict_keys(dict, key):
    parallel_questions = []
    for p in range(len(dict)):
        parallel_questions.append(dict[p][key])

    return parallel_questions


# find repeats, and makes a list where the index of the list of
# item_repeats is the same as the index of that item in the main list/dict
def test_for_repeats(list):
    item_repeats = []
    for item in list:
        repeats = 0
        for x in list:
            if item == x:
                repeats += 1
        item_repeats.append(repeats)

    return item_repeats


# finds the index of the first largest number in list of integers
def find_highest_num(list):
    # find the largest number in list of integers
    max = list[0]
    for t in list:
        if t > max:
            max = t

    # returns the index of the first largest number
    return max


# find the word to revise from list of mistakes, and prints relevant info
def print_word_to_revise(mistakes):
    mistakes_questions = create_list_from_dict_keys(mistakes, "question")
    mistakes_questions_repeats = test_for_repeats(mistakes_questions)
    most_mistakes_repeats = find_highest_num(mistakes_questions_repeats)

    worst_mistake = mistakes[mistakes_questions_repeats.index(most_mistakes_repeats)]

    print(f"Word to Revise! {worst_mistake['question'].upper()} which "
          f"translates to {', '.join(worst_mistake['answers']).upper()}")

    print(f"(You got this one wrong {most_mistakes_repeats} time"
          f"{pluraliser(most_mistakes_repeats, 's')})")


def review_mistakes(mistakes):
    if abcd_checker("Do you want to review your mistakes?", "yes", "no") == "yes":
        print()
        for x in mistakes:
            print(f"{x['question'].upper()} which translates to "
                  f"{', '.join(x['answers']).upper()}  "
                  f"//  You answered:"
                  f" {x['user_answer']}")
        print()
    else:
        print("Okay, but don't forget: ")

    print_word_to_revise(mistakes)


# PLURALISER
# accepts an int and str ('s' or 'es') and determines whether plural or not
def pluraliser(amount, conjugation):
    if amount != 1:
        return conjugation
    else:
        return ""

# main routine


# pre-game

global GLOBAL_INDENT
GLOBAL_INDENT = " " * 2

# # WELCOME INSTRUCTIONS
# welcome()
# if abcd_checker("Would you like to see the instructions?", "yes", "no") == \
#         "yes":
#     instructions()
# print()

# COLLECT WORDS
master_list = []  # will contain word-sets

text_decorator.print_section_title("collection selection")
print()

master_list = choice_selection(master_list)
text_decorator.print_divide_section()

# CHOOSE LANGUAGE
text_decorator.print_section_title("language selection")
print()

language_choice = abcd_checker("What language would you like to answer in",
                               "maori", "english", "both")
print()
print_text = f"You chose to answer in: {language_choice.upper()}"
text_decorator.print_surrounding(2, 6, print_text, 75, ":")
text_decorator.print_divide_section()

# PLAY ROUND

user_mistakes = []
correct_answers = []

# game mechanics / looping
i = 1
user_start = start_timer()
while len(master_list) > 0:
    master_list = play_round(language_choice, master_list, i)
    i += 1
user_stop = stop_timer()
print()

# post-game
mistakes_num = len(user_mistakes)
correct_num = len(correct_answers)
total_questions_answered = mistakes_num + correct_num

user_time = calc_time(user_start, user_stop)
print(f"It took you {write_min_and_sec(user_time)} to answer "
      f"{total_questions_answered} questions")
print(f"You got {correct_num} correct, and made {mistakes_num} mistake"
      f"{pluraliser(mistakes_num, 's')}")
print()

# REVIEW MISTAKES
if len(user_mistakes) > 0:
    review_mistakes(user_mistakes)
else:
    print("You didn't make any mistakes! Ka Pai!")


