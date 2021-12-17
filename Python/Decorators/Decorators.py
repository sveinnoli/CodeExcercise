# Example of a function inside a function and returning reference to said inner functions
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"
    
    if num == 1:
        return first_child
    else:
        return second_child

print(parent(1)())
print(parent(2)())


# Example demonstrating Decorators

def my_decorator(func):
    def wrapper():
        print("Something is happening before function")
        func()
        print("Something is happening after function")
    return wrapper

@my_decorator
def say_whee():
    print("Wheeee!")


# say_whee = my_decorator(say_whee)
# say_whee()
print(say_whee())

