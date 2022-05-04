"""Code taken from v1. This asks user what collections of words they would
like to learn, and adds those collections to a master list. When the user is
done picking, the choices and master list are displayed and the program ends

Inefficiencies: main routine is repeated in places
Bugs: user can type 'x' on first input and there will be no words in
master_list"""

import library


# code taken from https://favtutor.com/blogs/merge-dictionaries-python,
# takes two dictionaries as arguments and combines them
def merge_two_dicts(dict_1, dict_2):
    result = dict_1 | dict_2
    return result


def choose_collection(master, choice):
    # important-- all if/else statements here must do: (result = something)

    if choice in possible_choices:  # checks that user input if valid

        if choice in choices:  # stops duplicate in master_list
            print(f"You already chose {choice}")
            result = master
        elif choice == "numbers":
            result = merge_two_dicts(master, library.numbers_dict)
        elif choice == "days":
            result = merge_two_dicts(master, library.days_dict)
        elif choice == "months":
            result = merge_two_dicts(master, library.months_dict)

        elif choice == "all":
            # resets master list, and calls itself going through all the
            # options until all collections are added to master_list
            master = {}
            choices.clear()
            for i in range(len(possible_choices) - 2):
                print(i)
                master = choose_collection(master, possible_choices[i])
            result = master
            return result

        elif choice == "x":

            if not choices:
                print("You need to pick something, silly")
            else:
                print("Collections selected")
            result = master
            return result  # this stops 'x' from being added to choices

        choices.append(choice)  # adds user choice to list to ensure no repeats

    else:
        print(f"Sorry, there is no collection called '{choice}'")
        result = master

    return result


# The following method converts an item in the master_list to a tuple. This
# means the tuple is a word-set. This tuple contains two items: a string of
# the name of the word-set, and a dictionary of translations.
# word_set1 = list(master_list.items())[0]


# main routine


master_list = {}

# the method choose_collection() will add the user's choices to this list to
# ensure no duplicates of dictionaries are added to master_list
choices = []

# this is the easiest way to check for valid/invalid input. Must end in 'x'
# and 'all'
possible_choices = ["numbers", "days", "months", "x", "all"]

collection_choice = input("From what collection of words would you like to "
                          "learn >> ").lower()
master_list = choose_collection(master_list, collection_choice)

while collection_choice != "x":
    collection_choice = input("If you would like to add another collection, "
                              "do so. Otherwise type 'x' >>> ").lower()
    master_list = choose_collection(master_list, collection_choice)

print("\n end")
print(f"You chose: {choices}")
print(master_list)
