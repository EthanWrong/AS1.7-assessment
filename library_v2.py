"""This is a dictionary of words in their English and Maori translations
created by Ethan Wong.
All maori translations according to
https://www.maorilanguage.net/maori-words-phrases and
with secondary translations added from
https://maoridictionary.co.nz/

** Understanding**
> Each separate themed collection is called __collection (e.g
numbers_collection). These are lists.

> Each item in the lists are WORD-SETS, which are dictionaries

> Word-sets contain two items which are lists, the English translation(s) and
Maori translation(s).

> English and Maori translations may contain multiple items in each list
because there may be multiple acceptable translations for each word. The
first word in each list is the best translation and should be used to display.
"""
# list of all the collections in this library
collections = ["numbers", "days", "months"]

# collection of numbers 1-10 in English and Maori
numbers_collection = [
    {
        "english": ["one", "1"],
        "maori": ["tahi"]
    },
    {
        "english": ["two", "2"],
        "maori": ["rua"]
    },
    {
        "english": ["three", "3"],
        "maori": ["toru"]
    },
    {
        "english": ["four", "4"],
        "maori": ["whā", "wha"]
    },
    {
        "english": ["five", "5"],
        "maori": ["rima"]
    },
    {
        "english": ["six", "6"],
        "maori": ["ono"]
    },
    {
        "english": ["seven", "7"],
        "maori": ["whitu"]
    },
    {
        "english": ["eight", "8"],
        "maori": ["waru"]
    },
    {
        "english": ["nine", "9"],
        "maori": ["iwa"]
    },
    {
        "english": ["ten", "10"],
        "maori": ["tekau"]
    }
]

# collection of the days in English and Maori
days_collection = [
    {
        "english": ["monday", "mon"],
        "maori": ["rāhina", "rahina", "mane"]
    },
    {
        "english": ["tuesday", "tue"],
        "maori": ["rātū", "ratu", "turei"]
    },
    {
        "english": ["wednesday", "wed"],
        "maori": ["rāapa", "raapa", "wenerei"]
    },
    {
        "english": ["thursday", "thu"],
        "maori": ["rāpare", "rapare", "taite"]
    },
    {
        "english": ["friday", "fri"],
        "maori": ["rāmere", "ramere", "paraire"]
    },
    {
        "english": ["saturday", "sat"],
        "maori": ["rāhoroi", "rahoroi", "hatarei"]
    },
    {
        "english": ["sunday", "sun"],
        "maori": ["rātapu", "ratapu"]
    }
]

# collection of the months in English and Maori
months_collection = [
    {
        "english": ["january", "jan"],
        "maori": ["hanuere", "kohitātea", "kohitatea"]
    },
    {
        "english": ["february", "feb"],
        "maori": ["pēpuere", "pepuere", "hui-tanguru", "pēpuere"]
    },
    {
        "english": ["march", "mar"],
        "maori": ["maehe", "poutū-te-rangi", "poutu-te-rangi"]
    },
    {
        "english": ["april", "apr"],
        "maori": ["āperira", "aperira", "paenga-whāwhā", "paenga-whawha"]
    },
    {
        "english": ["may"],
        "maori": ["mei", "haratua", "maramarima"]
    },
    {
        "english": ["june", "jun"],
        "maori": ["hune", "pipiri"]
    },
    {
        "english": ["july", "jul"],
        "maori": ["hūrae", "hurae", "hōngongoi", "hongongoi"]
    },
    {
        "english": ["august", "aug"],
        "maori": ["akuhata", "ākuhata", "here-turi-kōkā", "here-turi-koka"]
    },
    {
        "english": ["september", "sep"],
        "maori": ["hepetema", "mahuru"]
    },
    {
        "english": ["october", "oct"],
        "maori": ["ōketopa", "oketopa", "whiringa-ā-nuku", "whiringa-a-nuku"]
    },
    {
        "english": ["november", "nov"],
        "maori": ["noema", "whiringa-ā-rangi", "whiringa-a-rangi"]
    },
    {
        "english": ["december", "dec"],
        "maori": ["tīhema", "tihema", "hakihea"]
    }
]

# collection of the word 'family' in English and Maori
test_collection = [
    {
        "english": ["family"],
        "maori": ["whānau", "whanau"]
    }
]

""" below is sample code for examples on how to reference and use the 
dictionary in a different file (OUT OF DATE, WORKS FOR DICTIONARIES)"""

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
