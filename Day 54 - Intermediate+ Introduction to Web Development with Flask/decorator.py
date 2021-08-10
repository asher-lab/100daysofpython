## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(4)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")


# Weird syntx

# What you are doing here is you are assigning
# a function to a decorator
# the decorator is named "decorated_function"
decorated_function = delay_decorator(say_greeting)

# add () to the variableFunc, to call it
decorated_function()
