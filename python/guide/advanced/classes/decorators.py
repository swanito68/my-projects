# Decorator = A functions that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

# Let's define a decorator:
def add_sprinkles(func):  # We will pass a function to the decorator function
    def wrapper(
        *args, **kwargs
    ):  # We need to define an inner function, and add args and kwargs to accept any number of arguments and keyword arguments
        print("*You add sprinkles*")
        func(*args, **kwargs)  # Same here

    return wrapper


# Let's add more:
def add_fudge(func):
    def wrapper():
        print("*You add fudge*")
        func()

    return wrapper


# Let's make a function:
@add_sprinkles  # You put @<func name>
@add_fudge  # You can add as many as you need
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")


get_ice_cream("vanilla")  # Let's call that function
