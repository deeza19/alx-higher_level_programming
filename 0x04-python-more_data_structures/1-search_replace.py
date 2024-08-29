#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_list = my_list.copy()
    for item in replaced_list:
        if search == item:
            index = replaced_list.index(item)
            replaced_list[index] = replace
        else:
            return replaced_list
        return replaced_list
