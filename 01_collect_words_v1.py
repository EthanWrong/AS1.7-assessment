import library

items = library.numbers_dict


# print(items)

# word = list(items.items())[3][1]
# this method converts an item in a dictionary to a tuple, that contains the
# name of the item of said dictionary and the inner dictionary like so:
# (1, {'english': ['one', '1'], 'maori': ['tahi']})

# print(word)

# if "wha" in word["maori"]:
#     print(True)

# code taken from https://favtutor.com/blogs/merge-dictionaries-python,
# takes two dictionaries as arguments and combines them
def merge_two_dicts(dict_1, dict_2):
    result = dict_1 | dict_2
    return result


master_list = merge_two_dicts(library.numbers_dict, library.test_dict)
print(master_list)
