"""Code that asks and test the user for the answer"""


def test_user(question, answers):
    answer = input(f"Translate '{question}' >>> ").lower()
    if answer in answers:
        print("Correct")
    else:
        print("Incorrect")
        print(f"The correct answer was {answers[0]}")
    if len(answers) > 1:
        print(f"answers included: {', '.join(answers)}")


# main routine
q = "one"
a = ["tahi", "nopee"]


test_user(q, a)
