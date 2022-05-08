"""Function that can take in two or more possible answers, a question,
and then ask the player for an answer until the user inputs a valid answer,
and returns that answer."""


# function that can take a question and 4 possible answers
def abcd_checker(question, answer_a, answer_b, answer_c=None, answer_d=None):
    while True:

        # Ask the user the input question
        answer = input(f"{question.capitalize()} >>> ").lower()

        if answer == answer_a:
            answer = answer_a
            return answer

        elif answer == answer_b:
            answer = answer_b
            return answer

        elif answer == answer_c:
            if answer_c is not None:
                answer = answer_c
                return answer
        elif answer == answer_d:
            if answer_d is not None:
                answer = answer_d
                return answer

        # otherwise, show error
        else:
            # if c and d have not been assigned
            if answer_c is None and answer_d is None:
                print(f"Please answer '{answer_a}' or '{answer_b}'")

            # if d has not been assigned
            elif answer_d is None:
                print(f"Please answer '{answer_a}', '{answer_b}', or '{answer_c}'")

            # if all possible answers have been assigned
            else:
                print(f"Please answer '{answer_a}', '{answer_b}', '{answer_c}', "
                      f"or '{answer_d}'")


print(abcd_checker("How are you?", "good", "bad", "ok"))

print(abcd_checker("Favourite colour?", "red", "orange", "green", "blue"))
