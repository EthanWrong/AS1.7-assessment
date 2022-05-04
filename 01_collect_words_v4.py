"""Code taken from v1.
"""
import library


# code taken from https://favtutor.com/blogs/merge-dictionaries-python,
# takes two dictionaries as arguments and combines them
def merge_two_dicts(dict_1, dict_2):
    result = dict_1 | dict_2
    return result


# choice checker that checks choice is valid.
def choice_checker(choice):
    if choice in (dictionaries):
        # add di















master_list = merge_two_dicts(library.numbers_dict, library.test_dict)
print(f"master_list: {master_list}")

# The following method converts an item in the master_list to a tuple. This
# means the tuple is a word-set. This tuple contains two items: a string of
# the name of the word-set, and a dictionary of translations.
word_set1 = list(master_list.items())[0]
print(f"word-set: {word_set1}")
