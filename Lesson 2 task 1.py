import random

my_list = []

for x in range(10):
    my_list.append(random.randint(1, 100))

print(my_list)
my_list.sort()
print(my_list)
