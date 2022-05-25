"""Code that determines if a word is pluralised or not, to simplify code in
base program"""


# accepts an int and str ('s' or 'es') and determines whether plural or not
def pluraliser(amount, conjugation):
    if amount != 1:
        return conjugation
    else:
        return ""


# main routine

print(f"You got this wrong {1} time{pluraliser(1, 's')}")
print()
print(f"You got this wrong {4} time{pluraliser(4, 's')}")

print(f"I saw {3} bus{pluraliser(3, 'es')} ")
