"""Code taken from v2.
Will now work if only first letter of answer is typed."""


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


print(abcd_checker("How are you?", "good", "bad", "ok"))
print(abcd_checker("Yes or no?", "yes", "no"))
print(abcd_checker("Favourite colour?", "red", "orange", "green", "blue"))
