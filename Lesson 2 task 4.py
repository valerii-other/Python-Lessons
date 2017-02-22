my_dict = {'apple': ['malum', 'pomum', 'popula'],
           'fruit': ['baca', 'bacca', 'popum'],
           'punishment': ['malum', 'multa']
           }

print len(my_dict), my_dict
old_keys = my_dict.keys()

for dict_item_key, dict_item_value in my_dict.items():
    for list_item in dict_item_value:
        if list_item in my_dict:
            my_dict[list_item].append(dict_item_key)
        else:
            my_dict.update({list_item: [dict_item_key]})

for x in old_keys: del my_dict[x]
print (len(my_dict), my_dict)
