"""Code taken from v4.
All functionality has been added.
Also added a help option so users know what collections can be selected
"""
import library_v2
import pprint


# choice interpreter that checks choice is valid, and does action accordingly
def choice_selection(master):
    collections = []
    choice = input("From what collection of words would you like to learn? "
                   "\nEnter '?' for collection options >>> ").lower()

    while True:
        if choice == "all":
            master.clear()
            collections.clear()
            for i in library_v2.collections:
                master = add_collections(i, master)
                collections.append(i)
            print(f"Collections {library_v2.collections} have been added.")

        elif choice == "?":
            print(f"The available collections to learn from are: "
                  f"{', '.join(library_v2.collections)}, or 'all'")
            print()

        elif choice == "x":
            if collections:
                # print("exit choice selection")
                # print()
                break
            else:
                print("<error>, you need to pick some words")
                print()

        # checks choice is a collection name
        elif choice in library_v2.collections:
            if choice not in collections:  # checks not already chosen

                master = add_collections(choice, master)

                # adds name of collection to list that keeps track of
                # collections added
                collections.append(choice)

                print(f"Collection {choice} added")
                print()

            else:
                print("<error>, you already have added that collection")
                print()

        else:
            print("<error>, collection does not exist")
            print()

        # checks if all collections have been added to master list
        if len(collections) == len(library_v2.collections):
            print("All collections have been selected.")
            break

        # asks the user for input
        if not collections:  # if nothing has been chosen
            choice = input(
                "From what collection of words would you like to learn >>> "
                "").lower()
        else:  # is something has been chosen
            choice = input(
                "If you would like to add another collection, do so. "
                "Otherwise type 'x' >>> ").lower()

    print("Choice selection complete.")
    print()
    print(f"You chose: {', '.join(collections)}")
    return master


# adds a collection list to a master list
def merge_list(collection1, collection2):
    result = collection1 + collection2
    return result


# code that adds correct collection to master list based on choice
def add_collections(choice, master):
    if choice == "numbers":
        master = merge_list(library_v2.numbers_collection, master)

    elif choice == "days":
        master = merge_list(library_v2.days_collection, master)

    elif choice == "months":
        master = merge_list(library_v2.months_collection, master)

    else:
        print("Something went wrong.")

    return master


# main routine


master_list = []  # will contain word-sets

master_list = choice_selection(master_list)
master_list_display = pprint.pformat(master_list)
print()
print(master_list_display)

# test code for how to access a word-set
# print(library_v2.numbers_collection[0])
