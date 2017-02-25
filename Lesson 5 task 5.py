class test_class (object):

    def __init__(self, name):
        self.name = name

    def say_my_name (self):
        print (self.name)

    def print_this (self,arg):
        print (arg)


test = test_class("1st")
test2 = test_class("2nd")


test.say_my_name()
test2.say_my_name()

print(test, test2)

