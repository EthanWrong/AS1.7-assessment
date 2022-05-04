"""This is a dictionary of words in their English and Maori translations
created by Ethan Wong.

** Understanding**
> Each separate themed dictionary is a variable named __dict (ie theme_dict).

> Inside these dictionaries are WORD-SETS, which are identified by the
English translation of each word

> Word-sets contain two items which are lists, the English translation(s) and
Maori translation(s).

> English and Maori translations may contain multiple items in each list
because there may be multiple acceptable translations for each word. The
first word in each list is the best translation and should be used to display.
"""
# list of all the dictionaries in this library
dictionaries = ["numbers", "days", "months", "test"]

# dictionary of numbers 1-10 in English and Maori
numbers_dict = {
    "one": {
        "english": ["one", "1"],
        "maori": ["tahi"]
    },
    "two": {
        "english": ["two", "2"],
        "maori": ["rua"]
    },
    "three": {
        "english": ["three", "3"],
        "maori": ["toru"]
    },
    "four": {
        "english": ["four", "4"],
        "maori": ["whā", "wha"]
    },
    "five": {
        "english": ["five", "5"],
        "maori": ["rima"]
    },
    "six": {
        "english": ["six", "6"],
        "maori": ["ono"]
    },
    "seven": {
        "english": ["seven", "7"],
        "maori": ["whitu"]
    },
    "eight": {
        "english": ["eight", "8"],
        "maori": ["waru"]
    },
    "nine": {
        "english": ["nine", "9"],
        "maori": ["iwa"]
    },
    "ten": {
        "english": ["ten", "10"],
        "maori": ["tekau"]
    },

}

# unfinished dictionary of the days in English and Maori
days_dict = {
    "monday": {
        "english": ["monday", "mon"],
        "maori": ["rāhina", "rahina", "mane"]
    }
}

# unfinished dictionary of the months in English and Maori
months_dict = {
    "january": {
        "english": ["january", "jan"],
        "maori": ["hānuere ", "hanuere"]
    }
}

# dictionary of the word 'family' in English and Maori
test_dict = {
    "family": {
        "english": ["family"],
        "maori": ["whānau", "whanau"]
    }
}

""" below is sample code for examples on how to reference and use the 
dictionary in a different file """

# import dictionary


# print(dictionary.numbers_dict)
#
# language = "english"
#
# word1 = dictionary.numbers_dict[1][language]
# word2 = dictionary.numbers_dict[4][language]
#
# print(word1[0], word2[0])
#
# if "4" in word2:
#     print(True)
