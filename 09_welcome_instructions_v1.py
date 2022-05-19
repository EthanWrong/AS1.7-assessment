"""Copied abcd_checker() function from 02v2"""


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


# main routine
welcome()
if abcd_checker("Would you like to see the instructions?", "yes", "no") == \
        "yes":
    instructions()
print("<program continues>")
