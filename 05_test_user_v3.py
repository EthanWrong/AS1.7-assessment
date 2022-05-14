"""Code built on v2
Now specifies which language user should type answer in"""


def test_user(question, answers, language="The corresponding Language"):
    user_answer = input(f"Translate '{question}' into "
                        f"{language.capitalize()} >>> ").lower()

    # if answer is correct
    if user_answer in answers:
        print("Correct")
        correct_answers.append(remember_question(question, answers, user_answer))

    # if answer is incorrect
    else:
        print("Incorrect")
        print(f"The correct answer was {answers[0]}")
        wrong_answers.append(remember_question(question, answers, user_answer))

    # if there was more than one possible answer
    if len(answers) > 1:
        print(f"Other possible answers included: {', '.join(answers)}")
    print()


def remember_question(question, answers, user_answer):
    return {"question": question,  # what the question was
            "answers": answers,  # what the correct answers were
            "user_answer": user_answer}  # what the user answered


# main routine

# these variables will be set with the generate_question method
q = "one"
a = ["tahi", "nopee"]
q2 = "tekau"
a2 = ["ten", "10"]

wrong_answers = []
correct_answers = []

test_user(q, a, "maori")
test_user(q2, a2, "english")
print(wrong_answers)
print(correct_answers)
