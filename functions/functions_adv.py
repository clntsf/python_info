# --------------------------- (somewhat) Advanced Examples of Use of Functions --------------------------- #


# --- Typehinting --- #

# our same function to square its input, but something is different...
def square_me(x: int) -> int:
    return x**2

# note the (x: int) -> int notation.
# this tells our user (and the text editor they use) the suggested type of the parameter(s) for the function,
# and the type of the item it will return. This is called typehinting, and it is very helpful to make code more readable

# note that python will not throw an error if the user enters a parameter of a different type, that is up to you

# we can typehint with 'complex types' to specify more if we have something specific in mind. for example:
def sort_list(l1: list[int | float], descending: bool = False) -> list[int|float]:
    return sorted(l1, reverse = descending)

# here, we indicate the following to the user:

# 1. "l1: list[int | float]"  -  the variable given for parameter "l1"
# should be a list where each item has type int OR float (| means OR )

# 2. "descending: bool = False"  -  the parameter "descending" should be
# a boolean (bool - True/False), and its default value is False (see Basic)

# 3. "-> list[int | float]"  -  the type of the variable this function
# returns will be a list, where each item has type int OR float


# Again, this is all totally optional and it is not enforced by python, but the fact
# that we can show all this to anyone reading with just a bit of notation lets us
# write very clean, understandable code and makes it easier to debug



# --- Lambda / Anonymous functions --- #

# these have a much lesser use-case, and can be entirely avoided if desired, but sometimes we need the functionality of a function
# for some small operation without wanting to define one ourselves (see the map(), filter() etc. of Intermediate as examples)

# In these cases, we can use lambda functions, which look like this

double = lambda x: x * 2
print(double(3))            # we can call this function just like a normal one

# the syntax for this is as follows
# ---------------------------------

# 1. assigning to the variable "double", the name of our function

# 2. "lambda", to tell the program this is a lambda function

# 3. a comma-separated list of parameters - here we just have x,
# but the function could look like

#  > lambda a,b,c, etc... : [something] if we have many parameters (normally wouldn't use a lambda with more than 2 params)
#  > lambda: [something] if we have no parameters, which is also possible but not that likely

# 4. a colon (:) to separate our parameters and what the function will do

# 5. "x * 2" what our function will return, usually a very simple, single expression.


# this function is syntactically identical to
def double_me(x): return x*2

# but if we only need to use it once, in a function like map() or filter(), we can define a lambda function in-line to save space
list1 = [1,2,3,4,5]

list2 = list(map( lambda x: x*2, list1 ))   # very slick and compact, and no need for a def double_me(x): ... that we never use again
print(list2)

# note that this does make our program less readable, but given the simplicity of lambda functions,
# it will most likely not be that difficult for an experienced reader to figure out