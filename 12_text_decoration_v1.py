"""Code that can decorate text
Pluraliser was added to this component"""


# accepts an int and str ('s' or 'es') and determines whether plural or not
def pluraliser(amount, conjugation):
    if amount != 1:
        return conjugation
    else:
        return ""


# makes a bar
def print_bar(indent, width, character):
    print(f"{indent*' '}{width*character}")


# allows text to be placed within a line of characters
def print_surrounding(indent, character_indent, text, total_width, character):
    characters_right = (total_width - (indent + character_indent + len(
        text) + 2)) * character
    print(f"{indent*' '}{character_indent*character} {text} {characters_right}")


# indents text to be used in body
def body_indent(extra_indent=0):
    return " " + extra_indent*" "


def print_section_title(title_text):
    title = f">> {title_text.upper()} <<"

    print_bar(0, 79, "*")
    print_surrounding(0, 8, title, 79, "*")
    print_bar(0, 79, "*")


def print_divide_section():
    print("----")
    print()


def print_correct_answer(user_answer):
    print_bar(2, 75, "▁")

    text = f"'{user_answer.upper()}' ✓ Correct"
    print_surrounding(2, 4, text, 77, "▓")

    print_bar(2, 75, "▔")


def print_incorrect_answer(user_answer, correct_answer):
    print_bar(2, 75, "▁")

    incorrect_text = f"'{user_answer.upper()}' ✗ Incorrect"
    print_surrounding(2, 4, incorrect_text, 77, "░")

    correct_text = f"'{correct_answer}' is the answer"
    print_surrounding(2, 4, correct_text, 77, "▓")

    print_bar(2, 75, "▔")


def print_possible_answers(answers_list):
    possible_answers = ", ".join(answers_list).upper()
    indent = " " * 2
    print(indent + "-- { " + possible_answers + " } are possible answers --")


def print_questions_left(number):
    indent = " " * 4
    print(f"{indent}[ {number} question{pluraliser(number, 's')} left ]")


# main routine

print_bar(0, 79, "-")
print_surrounding(2, 4, "'TWO' is correct", 77, "*")

print(f"{body_indent()}this is indented")
print_divide_section()
print_section_title("section title")
print_correct_answer("five")
print_incorrect_answer("two", "asdf")
print_possible_answers(["one", "1"])
print_questions_left(3)
