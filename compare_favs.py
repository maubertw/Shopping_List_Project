with open('mali_fav_foods.txt') as mali_fave:
    fav_foods_mr = mali_fave.readlines()
with open('mary_fav_food.txt') as mary_fave:
    fav_foods_mw = mary_fave.readlines()


# print fav_foods_mr
# print fav_foods_mw

# for item in fav_foods_mw:
#     print item

def compare_favs (list1, list2):
    shared_items = []
    for item in list1:
        if item in list2:
            shared_items.append(item)
            print "item appended"
            print shared_items

    if shared_items == False:
        print item
        print "Our favorite foods are different"
    else:
        print shared_items


compare_favs(fav_foods_mr, fav_foods_mw)