
import string

test_string = raw_input('Please input your string: ')

test_set = set(test_string)

lower_case = float(len(test_set&set(string.ascii_lowercase)))/len(test_string)
upper_case = float(len(test_set&set(string.ascii_uppercase)))/len(test_string)

print("Chars in upper case {:.0%}, lower case {:.0%}, other {:.0%}.".format(lower_case,upper_case,1-lower_case-upper_case))
