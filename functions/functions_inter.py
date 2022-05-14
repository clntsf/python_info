# --------------------------- Intermediate Examples of Use of Functions --------------------------- #


# a function that checks if a given number is even. Notice how the name allows us to easily figure out what it does
def is_even(x): return (x%2 == 0) # we can write functions as one-liners like this! only do this if the content is very simple though

list_nums = [1,2,3,4,5,6,7,8,9,10]
for num in list_nums:
    if is_even(num):            # we can use the return value of a function as a condition for an if statement!
        print(num)              # notice how much cleaner this makes the code as opposed to the below

# for num in list_nums:
#     if num%2 == 0:
#         print(num)

# It's a pretty basic example, but just by using the function it's much easier to see what we are doing



# -- filter(), map(), and sorted() (and others like them) -- #

# Notice in the following examples that the functions (is_even(), double(), and first_item()) do not
# appear with brackets or parameters when they are used as parameters for the following functions.

# When a function's name is used with brackets, we 'Call' that function, i.e. we tell it to run right now.
# but if we don't include brackets, it is just a reference to that function for some other thing to use whenever it wants



# here is a basic example:

func = is_even  # store a reference to the function is_even() in the variable func, do not call the function (no brackets)

print(func(4))  # we can now use this saved variable, func, to call our function whenever we want.
                # this is useful in scenarios where this could be one of many possible functions


# The filter() function
even_nums = list(filter(is_even, list_nums))    # we can use the filter() function to apply a function across a list
print("Even Numbers:",even_nums)                # and keep only the items the function returns True for!


# the map() function
def double(x): return x*2       # another basic function to double a number

doubled_nums = list(map(double, list_nums))     # similarly, the map() function applies a function to each item
print("Doubled Numbers:",doubled_nums)          # in a list and makes a list of the return values!

# We can also use this technique for other functions, like print(), where we do not need an output:
map(print, even_nums) # instead of "for num in even_nums: print(num)", although slightly more confusing


# the sorted() function
def first_item(list1): return list1[0]  # returns the first item in a given list

# The sorted() function has a parameter called key, which can be given a function. It will apply this function to each of the elements in
# the passed object and sort them based on the results. for example:

# just a list, where each element is a list in the form [int, str]
items = [
    [5, "apple"],
    [2, "banana"],
    [4, "cherry"],
    [1, "avocado"],
    [3, "mango"]
]

items_sorted_by_first = sorted(items, key=first_item)   # notice how we use our function first_item to sort by the first item in each list
print(items_sorted_by_first)                            # again, no brackets here, we are giving it a function to use when it wants to

# we can use this technique with many functions that have a 'key' parameter,
# like max(), min(), and the inplace list.sort() (similar to sorted())

# print( max(items, key=first_item) )
# print( min(items, key=first_item) )
# etc.