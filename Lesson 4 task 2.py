def decor(old_f):
    def new_func(arg):
        print ("new value %d", arg*3)
        return old_f(arg) * 3
    return new_func

@decor
def old_func(n):
    print("old value - %d", n)
    return n

print(old_func(2))


