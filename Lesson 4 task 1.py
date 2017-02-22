
def fibi_1(n):
# simple calculation
    a,b = 0,1
    i = 1
    while i < n:
        i+=1
        a,b = b, a+b
    return(a)


def fibi_2(n):
# recursion
    if (n-1) == 0:
        return 0
    elif (n-1) == 1:
        return 1
    else:
        return fibi_2(n-1)+fibi_2(n-2)


user_index = input("Please enter index for Fib number in row: ")
print("Nth Fib number is: ", fibi_1(user_index))
print("Nth Fib number is: ", fibi_2(user_index))


