"""Code restarted.
Instead of a dictionary of dictionaries, I used a list of dictionaries. Code
is not yet complete, but the majority of the core work is done. There is proof
that the code will work when all functionality is added.

Code is much more elegant and efficient than v1, v2, and v3
"""
import library_v2


# choice interpreter that checks choice is valid, and does action accordingly
def choice_selection(master):
    collections = []
    choice = input("Choice: ").lower()
    while True:
        if choice == "all":
            print("clear master list and add all collections to it")

        elif choice == "x":
            if collections:
                print("exit choice selection")
                break
            else:
                print("<error>, you need to pick some words")

        # checks choice is a collection name
        elif choice in library_v2.collections:
            if choice not in collections:  # checks not already chosen

                if choice == "numbers":
                    master = add_collection(library_v2.numbers_collection,
                                            master)

                    # adds name of collection to list that keeps track of
                    # collections added
                    collections.append("numbers")

                elif choice == "days":
                    master = add_collection(library_v2.days_collection,
                                            master)

                    # adds name of collection to list that keeps track of
                    # collections added
                    collections.append("days")

                elif choice == "months":
                    master = add_collection(library_v2.months_collection,
                                            master)

                    # adds name of collection to list that keeps track of
                    # collections added
                    collections.append("months")

                print(f"Collection {choice} added")

            else:
                print("<error>, you already have added that collection")

        else:
            print("<error>, collection does not exist")

        # checks if all collections have been added to master list
        if len(collections) == len(library_v2.collections):
            print("All collections have been selected.")
            break

        choice = input("Choose more? ").lower()

    print("Exited.")
    print(collections)
    return master


# adds a collection list to a master list
def add_collection(collection, master):
    result = collection + master
    return result


# main routine

master_list = []  # will contain word-sets

master_list = choice_selection(master_list)
print(master_list)

# test code for how to access a word-set
# print(library_v2.numbers_collection[0])
