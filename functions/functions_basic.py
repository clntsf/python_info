# --------------------------- Basic Examples of Use of Functions --------------------------- #


def say_hello():        # this function returns nothing, and just prints. It also does not take any arguments/parameters
    print("Hello!")

say_hello()             # to call our first function, I just need to give its name and parentheses.
                        # it does not take any arguments so I can leave the parentheses empty

def my_function(x):     # this function takes one argument, x, and returns x squared
    say_hello()             # note, I can call functions in other functions! super useful for repetition
    return x ** 2

# It is better to give functions descriptive names.
# for example, this one might be called square(x) or square_me(x)

x = int(input("Enter x: "))
print("X is", x)
x_squared = my_function(x)  # notice how it isn't clear what this does unless you read the function, something to avoid

print("X squared is", x_squared)

numbers = range(10)
for n in numbers():                         # here we use a loop to print the squares of numbers from 0 to 9 inclusive
    print(n, "squared is", my_function(n))  # notice how we do not need to assign the output to a variable and can print it straight up!

# Functions are really handy for cases where we have a common task, as it saves us the hassle
# of writing and changing the lines of code at many different places in our file. It also reduces
# line count and increases readability (how easy it is to understand our code)

# --- Default Arguments --- #

def say_message(message = "Hello!"):        # notice that we have '= "Hello!"' inside our parameters. This is called a default argument
    print(message)                          # and it means that this parameter is optional, and its default value is "Hello!"

say_message()                               # if we call the function without giving this parameter, it will use its default. otherwise, it will use
say_message("Goodbye!")                     # what we give it. We can use anything we like (with a few technical exceptions) as a default argument