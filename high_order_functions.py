# Lambda function: Function without a name
# ----------------------------------------

# Palindrome is a variable that contains a function.

# Sintaxis:

# Identificator (Name) = lambda Argument (or parameter): expresion (what you are evaluating) 

palindrome = lambda string: string == string[::-1]

# A string is the input or parameter and string == string[::-1] is the expression. Result would be True or False

print (palindrome("LUZAZUL"))

# -----------------------------------------------------------------------------------------------------------------

# High Order Functions: Function which input is other function.

# Filter:
# -------

my_list = [0,1,2,3,4,5,6,7,8,9]

# odds = lambda lst: lst % 2 != 0
# #When I try this code, I got a function object.

# odds = list(lambda lst: lst % 2 != 0)
# # TypeError as function object is not iterable.

# odds = filter(lambda lst: lst % 2 != 0, my_list)
# When I try this code, I got a Filter object

odds = list(filter(lambda lst: lst % 2 != 0, my_list))
#With this code, I get odds numbers. Filter object seems to be an iterable.

print(odds)

# Map:
# --------
square = list(map(lambda lst: lst ** 2,my_list))

print(square)

# Reduce:
# ---------
from functools import reduce

sum_list = reduce(lambda a, b : a + b, my_list)

print(sum_list)

