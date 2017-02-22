my_dict={'item1':15,'item2':20,'item3':10,'item4':2}

print ("initial order  - ", my_dict)
print ("sorted by cost - ", sorted(my_dict,key=my_dict.__getitem__))
