"""Code built on v1 that picks the 'word to revise'"""


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


def create_list_from_dict_keys(dict, key):
    parallel_questions = []
    for i in range(len(dict)):
        parallel_questions.append(dict[i][key])

    return parallel_questions


# find repeats, and makes a list where the index of the list of
# item_repeats is the same as the index of that item in the main list/dict
def test_for_repeats(list):
    item_repeats = []
    for i in list:
        repeats = 0
        for x in list:
            if i == x:
                repeats += 1
        item_repeats.append(repeats)

    return item_repeats


# finds the index of the first largest number in list of integers
def find_index_highest_num(repeats):
    # find the largest number in list of integers
    max = repeats[0]
    for i in repeats:
        if i > max:
            max = i

    # returns the index of the first largest number
    return repeats.index(max)


# main routine

# mistakes variable will be set in the base program
mistakes = [{'question': 'tekau', 'answers': ['ten', '10'], 'user_answer':
    '0'}, {'question': 'tekau', 'answers': ['ten', '10'], 'user_answer':
    '0'},{'question': 'whitu', 'answers': ['seven', '7'], 'user_answer':
    '5'}, {'question': 'whitu', 'answers': ['seven', '7'], 'user_answer':
    '6'}, {'question': 'tekau', 'answers': ['ten', '10'], 'user_answer':
    '5'}, {'question': 'five', 'answers': ['rima'], 'user_answer': '1'}]

mistakes_questions = create_list_from_dict_keys(mistakes, "question")
mistakes_questions_repeats = test_for_repeats(mistakes_questions)

print(mistakes_questions_repeats)
worst_mistake = mistakes[find_index_highest_num(mistakes_questions_repeats)]
print(worst_mistake)
print(f"Word to Revise: {worst_mistake['question'].upper()} which means "
      f"{', '.join(worst_mistake['answers'])}")
