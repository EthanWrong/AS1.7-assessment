"""This is an easy way to spruce up code with some easy unicode decorations
created by Ethan Wong.

At the bottom is some example code for how to use this.
Code commented with 'specifically' has been made for the Maori Quiz.

This code is copied from 12_text_decoration_v2 (used to be component 12 in
the Maori Quiz, but was renamed because Python import does not work with
numbers at the start of the filename)
"""
import math


# accepts an int and str ('s' or 'es') and determines whether plural or not
def pluraliser(amount, conjugation):
    if amount != 1:
        return conjugation
    else:
        return ""


# prints a bar of characters
def print_bar(indent, width, character):
    print(f"{indent*' '}{width*character}")


# allows text to be placed within a line of characters
def print_surrounding(indent, character_indent, text, total_width, character):
    characters_right = (total_width - (indent + character_indent + len(
        text) + 2)) * character
    print(f"{indent*' '}{character_indent*character} {text} {characters_right}")


# prints text in centre of selected characters
def print_centre(indent, text, total_width, character):
    central_text = f" {text} "
    indent_text = indent * " "

    uneven_side = ((total_width - len(central_text)) / 2)
    left_side = int(math.floor(uneven_side)) * character
    right_side = int(math.ceil(uneven_side)) * character

    print(indent_text + left_side + central_text + right_side)


# indents text to be used in body
def body_indent(extra_indent=0):
    return " " * 2 + extra_indent*" "


# specifically prints section title
def print_section_title(title_text):
    title = f">> {title_text.upper()} <<"

    print_bar(0, 79, "*")
    print_surrounding(0, 8, title, 79, "*")
    print_bar(0, 79, "*")


# specifically prints section divider
def print_divide_section():
    print("----")
    print()


# specifically prints correct answer
def print_correct_answer(user_answer):
    print_bar(2, 75, "▁")

    text = f"'{user_answer.upper()}' ✓ Correct"
    print_surrounding(2, 4, text, 77, "▓")

    print_bar(2, 75, "▔")


# specifically prints incorrect answer
def print_incorrect_answer(user_answer, correct_answer):
    print_bar(2, 75, "▁")

    incorrect_text = f"'{user_answer.upper()}' ✗ Incorrect"
    print_surrounding(2, 4, incorrect_text, 77, "░")

    correct_text = f"'{correct_answer.upper()}' is the answer"
    print_surrounding(2, 4, correct_text, 77, "▓")

    print_bar(2, 75, "▔")


# specifically prints possible answers
def print_possible_answers(answers_list):
    possible_answers = ", ".join(answers_list).upper()
    print(body_indent() + "-- { " + possible_answers + " } are possible "
                                                       "answers --")


# specifically prints questions left
def print_questions_left(number):
    print(f"{body_indent(2)}[ {number} question"
          f"{pluraliser(number, 's')} left ]")


# specifically prints question divider
def print_question_divider():
    print_bar(2, 75, "-")


# specifically prints word to revise
def print_word_to_revise(word, answers, times_wrong):
    word_text = f"'{word.upper()}"
    answers_text = "which means { " + ", ".join(answers).upper() + " }"
    times_wrong_text = f"( you got this wrong {times_wrong} time" \
                       f"{pluraliser(times_wrong, 's')}"

    print_bar(2, 75, "▁")

    print_bar(2, 75, "▓")
    print_centre(2, word_text, 75, "▓")
    print_centre(2, answers_text, 75, "▒")
    print_bar(2, 75, "▒")
    print_centre(2, times_wrong_text, 75, "░")
    print_bar(2, 75, "░")

    print_bar(2, 75, "▔")


# specifically prints welcome banner
def welcome_banner():
    print_bar(0, 79, "(")
    print_centre(0, "WELCOME TO THE MĀORI QUIZ", 79, ')')
    print_centre(0, "learn Te Reo Māori", 79, '(')
    print_bar(0, 79, ")")


# specifically prints reviewable stats
def print_stats(questions, correct, mistakes, time, sec_p_q):
    print(f"{body_indent()}🖊 {questions} question"
          f"{pluraliser(questions, 's')}")
    print(f"{body_indent()}✓ {correct} correct")
    print(f"{body_indent()}✗ {mistakes} mistake{pluraliser(mistakes, 's')}")

    print()

    minutes = time[0]
    seconds = time[1]
    minutes_and_seconds = f"{minutes} minute{pluraliser(minutes, 's')} and " \
                          f"{seconds} second{pluraliser(seconds, 's')}"
    print(f"{body_indent()}🕑 {minutes_and_seconds}")
    print(f"{body_indent()}⌛ {sec_p_q} second{pluraliser(sec_p_q, 's')} per "
          f"question")


# example code below


# print_bar(0, 79, "-")
# print_surrounding(2, 4, "'TWO' is correct", 77, "*")

# print(f"{body_indent()}this is indented")
# print_divide_section()
# print_section_title("section title")
# print_correct_answer("five")
# print_incorrect_answer("two", "asdf")
# print_possible_answers(["one", "1"])
# print_questions_left(3)
# print_question_divider()

# print_word_to_revise("five", ["rima"], 3)
# welcome_banner()

print_stats(5, 2, 3, [3, 12], 5)
