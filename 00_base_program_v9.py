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
+ adjust text formatting for test user & review stats
+ adjust text formatting for review mistakes & word to revise & welcome screen
+ improved instructions


To add (maybe):
Only need to type first letter of collection to add in pre-game phase
Entering a '?' while translating does not mean a mistake, but a question
that you didn't know?
Add an easter-egg 'default settings' that skips all the pregame stuff and
chooses numbers collection and sets language to english
"""
import library_v2
import random
import time
import text_decorator


# COLLECT WORDS
# choice interpreter that checks choice is valid, and does action accordingly
def choice_selection(master):
    collections = []
    choice = input(f"{GI_TXT}From what collection of words would you "
                   f"like to learn? \n{GI_TXT} Enter '?' for "
                   f"collection options >>> ").lower()

    while True:
        if choice == "all":
            master.clear()
            collections.clear()
            for w in library_v2.collections:
                master = add_collections(w, master)
                collections.append(w)
            collection_added_text = f"Collections {', '.join(collections)} added"
            text_decorator.print_centre(GI, collection_added_text, 71, "+")

        elif choice == "?":

            print()

            print(f"{GI_TXT}The available collections to learn from "
                  f"are:\n{GI_TXT} {', '.join(library_v2.collections)},"
                  f" or 'all'")

        elif choice == "x":
            if collections:
                # print("exit choice selection")
                # print()
                break
            else:
                print(f"{GI_TXT}You do have to pick SOME words, silly")

        # checks choice is a collection name
        elif choice in library_v2.collections:
            if choice not in collections:  # checks not already chosen

                master = add_collections(choice, master)

                # adds name of collection to list that keeps track of
                # collections added
                collections.append(choice)

                collection_added_text = f"Collection {choice.upper()} added"
                text_decorator.print_centre(GI, collection_added_text, 40, "+")

            else:
                print(f"{GI_TXT}You have already added that collection")

        else:
            print(f"{GI_TXT}Sorry, but that collection does not exist")

        print()

        # checks if all collections have been added to master list
        if len(collections) == len(library_v2.collections):
            print(f"{GI_TXT}All collections have been added")
            break

        # asks the user for input
        if not collections:  # if nothing has been chosen
            choice = input(f"{GI_TXT}From what collection of words "
                           f"would you like to learn? >>> ").lower()

        else:  # is something has been chosen
            choice = input(f"{GI_TXT}If you would like to add another "
                           f"collection, do so.\n{GI_TXT} Otherwise "
                           "type 'x' >>> ").lower()

    print(f"{GI_TXT}<< Choice selection COMPLETE >> ")
    print()
    collections_chosen_text = f"You chose: {', '.join(collections)}"
    text_decorator.print_surrounding(GI, 6, collections_chosen_text, 75, ":")
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
        answer = input(f"{GI_TXT}{question.capitalize()} >>> ").lower()

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
                print(f"{GI_TXT}  Please answer '{a}' or '{b}'")

            # if d has not been assigned
            elif d is None:
                print(f"{GI_TXT}  Please answer '{a}', '{b}', or '{c}'")

            # if all possible answers have been assigned
            else:
                print(f"{GI_TXT}  Please answer '{a}', '{b}', '{c}', "
                      f"or '{d}'")
            print(f"{GI_TXT}  < Initial also works >")
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
        print(f"{GI_TXT}<error>, invalid language chosen")


# will return a list
def get_correct_answers(word_set, language):
    return word_set[language]


# will return a string
def get_question(word_set, language):
    if language == "english":
        return word_set["maori"][0]
    elif language == "maori":
        return word_set["english"][0]


def test_user(question, answers, question_number, language="undefined"):
    # asks the question
    question_text = f"{GI_TXT}{question_number}) Translate " \
                    f"'{question.upper()}' into {language.capitalize()} >>> "
    user_answer = input(question_text)

    # if answer is correct
    if user_answer in answers:
        text_decorator.print_correct_answer(user_answer)
        correct_answers.append(
            remember_question(question, answers, user_answer))
        is_correct = True

    # if user wishes to exit the program
    elif user_answer == "x":
        exit_warning = f"Are you sure you want to quit? You " \
                       f"will not be able to\n{GI_TXT} continue this " \
                       f"game"
        print()
        want_to_quit = abcd_checker(exit_warning, "yes", "no")
        if want_to_quit == "yes":
            return "exit"
        else:
            is_correct = "repeat"
            return is_correct

    # if answer is incorrect
    else:
        text_decorator.print_incorrect_answer(user_answer, answers[0])

        user_mistakes.append(remember_question(question, answers, user_answer))
        is_correct = False

    # if there was more than one possible answer
    if len(answers) > 1:
        text_decorator.print_possible_answers(answers)

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
        print()
        text_decorator.print_surrounding(GI, 6, "Game Over", 75, ":")
        return []
    elif is_correct == "repeat":
        print()
        text_decorator.print_surrounding(GI, 6, "Good for you", 75, ":")

    else:  # if the answer is right / wrong
        if is_correct:
            master.remove(word_set)
        elif not is_correct:
            master.append(word_set)

        # code that keeps track of how many questions left
        left_to_answer = len(master)
        text_decorator.print_questions_left(left_to_answer)

    print()
    text_decorator.print_question_divider()

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
def find_min_and_sec(seconds):
    minutes = int(seconds // 60)
    and_seconds = int(seconds % 60)

    return [minutes, and_seconds]


# WELCOME INSTRUCTIONS
def instructions():
    print()
    print(f"{GI_TXT}This quiz is a whole-word answer quiz that tests "
          f"your knowledge of the\n{GI_TXT}Maori language and helps you"
          f" to improve.\n{GI_TXT}After selecting the words you wish "
          f"to learn and the language you wish to\n{GI_TXT}answer in, "
          f"you will continue translating words until you have translated\n"
          f"{GI_TXT}all the words you selected.\n{GI_TXT}Once "
          f"you have finished translating words, you will be able to review "
          f"your\n{GI_TXT}stats and mistakes.\n\n"
          f"{GI_TXT}NOTES:\n{GI_TXT}When "
          f"choosing a language, you can choose 'both' if you wish to answer"
          f" in\n{GI_TXT}Maori and English.\n{GI_TXT}When "
          f"translating, enter 'x' if you wish to stop the quiz there.")

    text_decorator.print_divide_section()


def welcome():
    text_decorator.welcome_banner()
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

    worst_mistake = mistakes[
        mistakes_questions_repeats.index(most_mistakes_repeats)]

    text_decorator.print_word_to_revise(worst_mistake['question'],
                                        worst_mistake['answers'],
                                        most_mistakes_repeats)

    # print(f"Word to Revise! {worst_mistake['question'].upper()} which "
    #       f"translates to {', '.join(worst_mistake['answers']).upper()}")
    #
    # print(f"(You got this one wrong {most_mistakes_repeats} time"
    #       f"{pluraliser(most_mistakes_repeats, 's')})")


def review_mistakes(mistakes):
    if abcd_checker("Do you want to review your mistakes?", "yes",
                    "no") == "yes":

        print()
        for f in range(len(mistakes)):
            correct_text = "'" + mistakes[f]['question'].upper() + "'" + " " \
                                                                      "means { "\
                           + ", ".join(mistakes[f]['answers']).upper() + " }"
            user_answer_text = "  >> You answered '" + \
                               mistakes[f]['user_answer'] + "'"

            print(f"{GI_TXT}{f + 1}) {correct_text}")
            print(f"{GI_TXT}{user_answer_text}")

    text_decorator.print_divide_section()
    input("  Press enter to get your Word to Revise >>> ")  # just waits for
    print()
    # the user to hit enter

    text_decorator.print_section_title("word to revise")

    print_word_to_revise(mistakes)


def review_stats(correct, mistakes, seconds):
    total_questions = correct + mistakes
    converted_time = find_min_and_sec(seconds)  # is a list

    if total_questions != 0 and seconds != 0:
        sec_per_question = round(seconds / total_questions, 1)
    else:
        sec_per_question = 0
    text_decorator.print_stats(total_questions, correct, mistakes,
                               converted_time, sec_per_question)


# main routine


# pre-game

global GI_TXT  # global indent as string
GI_TXT = text_decorator.GI * " "
global GI  # global indent as int
GI = text_decorator.GI

# WELCOME INSTRUCTIONS
welcome()
if abcd_checker("Would you like to see the instructions?", "yes", "no") == \
        "yes":
    instructions()
print()

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
text_decorator.print_surrounding(GI, 6, print_text, 75, ":")
text_decorator.print_divide_section()

# PLAY ROUND

user_mistakes = []
correct_answers = []

# during game: game mechanics / looping
text_decorator.print_section_title("quiz time")
print()

i = 1
user_start = start_timer()
while len(master_list) > 0:
    master_list = play_round(language_choice, master_list, i)
    i += 1
user_stop = stop_timer()
print()

# post-game
# REVIEW STATS
text_decorator.print_section_title("review")
print()
correct_num = len(correct_answers)
mistakes_num = len(user_mistakes)

user_time = calc_time(user_start, user_stop)

review_stats(correct_num, mistakes_num, user_time)
print()

# REVIEW MISTAKES
if len(user_mistakes) > 0:
    review_mistakes(user_mistakes)
else:
    print(f"{GI_TXT}You didn't make any mistakes! Ka Pai!")

print()
text_decorator.print_bar(0, 79, "*")

# GOODBYE MESSAGE
print()
print("Thanks for playing, I hope you learned something!")
