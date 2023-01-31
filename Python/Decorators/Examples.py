from datetime import datetime
import functools
import math
import random

from Decorators import (
    PLUGINS,
    do_twice,
    slow_down,
    timer,
    debug,
    register
)

# Simple decorator
@do_twice
def say_whee():
    print("Wheee!")

# Simple decorator using a positional argument
@do_twice
def greet(name):
    print(f"Hello {name}")


# Returning a value from a function that has a decorator attached to it
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return (f"Hi {name}")

# Times a function
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

# Debugs a function
@debug
def make_greeting(name, age=None):
    if not age:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

# Approximate Eulers number using a series expansion
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1/math.factorial(n) for n in range(terms))


# Apply a rate limit to a function
@slow_down
def countdown(from_number):
    if from_number < 1:
        print("liftoff")
    else:
        print(from_number)
        countdown(from_number - 1)


# Registering plugins
@register
def say_hello(name):
    return f'Hello {name}'

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(random.choice(list(PLUGINS.items())))
    print(greeter, greeter_func)
    print(f"Using {greeter!r}")
    return greeter_func(name)

randomly_greet("ab")
print(approximate_e())