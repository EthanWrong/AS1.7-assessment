"""Code taken from v2.

Inefficiencies: main routine is repeated in places
Bugs: user can type 'x' on first input and there will be no words in
master_list

This code became too difficult to work with, and the methods were not
efficient and the end result did not function properly."""
import library


# code taken from https://favtutor.com/blogs/merge-dictionaries-python,
# takes two dictionaries as arguments and combines them
def merge_two_dicts(dict_1, dict_2):
    result = dict_1 | dict_2
    return result


# code that adds the chosen collection from a library to the master_list.
# This code assumes that the choice is valid, so does not check for valid
# choice
def choose_collection(master, choice):
    # important-- all if/else statements here must do: (result = something)
    # otherwise master will be set to NoneType

    # stops duplicate in master_list
    if choice in choices:
        print(f"You already chose {choice}")
        result = master

    # will add the correct collection to master_list
    elif choice == "numbers":
        result = merge_two_dicts(master, library.numbers_dict)
    elif choice == "days":
        result = merge_two_dicts(master, library.days_dict)
    elif choice == "months":
        result = merge_two_dicts(master, library.months_dict)

    # resets master list, and calls itself going through all the options
    # until all collections are added to master_list
    elif choice == "all":

        master = {}
        choices.clear()
        for i in range(len(collections)):
            print(i)
            master = choose_collection(master, collections[i])
        result = master
        return result

    # will exit the choice selection
    elif choice == "x":

        # if choices is empty, it will return a blank dict
        if not choices:
            print("You need to pick something, silly")
            return {}
        else:
            print("Collections selected")
        result = master
        return result  # this stops 'x' from being added to choices

    else:
        print(f"Something HAS GONE WRONG")
        result = master

    choices.append(choice)  # adds user choice to list to ensure no repeats

    print(f"Collection {choice} added to learning list")
    return result


# The following method converts an item in the master_list to a tuple. This
# means the tuple is a word-set. This tuple contains two items: a string of
# the name of the word-set, and a dictionary of translations.
# word_set1 = list(master_list.items())[0]

def get_player_choice(master):
    while True:  # code will loop until a valid option is given
        choice = input("Choose another collection: ").lower()

        if choice in collections:  # checks user input is one of the
            # collections
            master = choose_collection(master, choice)
            return master

        elif choice in other_options:  # checks user input is an option
            if choice == "all":
                master = choose_collection(master, choice)
                return master
            else:
                return "end"
        else:
            print(f"Sorry, there is no collection called '{choice}'")


# main routine


master_list = {}

# the method choose_collection() will add the user's choices to this list to
# ensure no duplicates of dictionaries are added to master_list
choices = []

# this is the easiest way to check for valid/invalid input.
collections = ["numbers", "days", "months"]
other_options = ["all", "x"]

""" ---------------game mechanics------------ """


# collection_choice = input("choose collections: ").lower()
# master_list = choose_collection(master_list, collection_choice)

# loop until all choices chosen
# collection_choice = ""
# while collection_choice not in ("x", "all"):
#     collection_choice = input("choose more collections: ").lower()
#     master_list = choose_collection(master_list, collection_choice)


# choice = input("Choose first one: ").lower()
# master_list = choose_collection(master_list, choice)


while master_list != "end":
    master_list = get_player_choice(master_list)

print("\n end")
print(f"You chose: {choices}")
print(master_list)
