
list_of_lists = {}

def display_list_of_lists():
    """
    1 - show list print dictionary
    """
    print list_of_lists 


def display_specific_list(list_nickname):
    """
    2 - print specified list 
    """
    print list_of_lists[list_nickname]

def add_item(item):
    """
    3 - append item to selected list
    """
    list_of_lists[list_nickname].append(item)
    
def main():
    """
    0 - This is the main menu, you can choose what you want to do with your lists.
    """

print """Welcome to your shopping list, what would you like to do?
        1 - Show all lists.
        2 - Show a specific list
        3 - Add a new shopping list.
        4 - Add an item to a shopping list.
        5 - Remove an item from a shopping list.
        6 - Remove a list by nickname.
        7 - Exit when you are done."""

user_choice = raw_input(">  ")

if user_choice == 1:
    display_list_of_lists

if user_choice == 2:
    list_nickname = raw_input("Which list would you like to see?")
    display_specific_list(list_nickname)

if user_choice == 3: 
    list_nickname = raw_input("What would you like to call this list?")
    list_of_lists[list_nickname] = ()
    list_item = raw_input("What item would you like to add?")
    if list_item in list_of_lists[list_nickname]:
        list_item = raw_input("This item is already on the list. Please add another")
    else:
        add_new_list(list_item)


if __name__ == '__main__':
    main()



# 4 - select a list and add an item 
#     scan through dictionary for key that they want and append 

# 5 - which list do you want to edit?
#     show list
#     what do you want to remove?
#     remove item
#     show updated list

# 6 - find out which list they want to remove
#     scan through to find the key and remove the whole item

# 7 - Exit         





