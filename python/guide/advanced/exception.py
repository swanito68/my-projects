# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2. except, 3. finally

# There are many exceptions in python;
# ZeroDivisionError, when you divide by 0: 1 / 0
# TypeError, where, for example, you add 2 objects of the wrong type: 1 + "2"
# ValueError, where you typecast an object that you can't typecase: int(pizza)

# Let's try the exception handling:
try:  # We make a try block and indent whatever you need to put under it
    number = int(input("Enter a number: "))
    number2 = int(input("Enter an other number: "))
    print(f"{number} / {number2} = {number / number2}")
except (
    ZeroDivisionError
):  # You type in "except <exception>:" and indent what's under it.
    print("You cannot divide by 0!!")
except ValueError:  # You can put as many exceptions you need
    print("That is not a number you dumbo jumbo.. :/")
    # You can also put "except Exception" which applies a block of code to all exceptions, but
    # that is bad practice, because it's better to tell what the user did
finally:  # This is code that always runs no matter if there is an error or not
    print("this place is dirty. Do some cleanup here")

# There also is a lot more exceptions that you can look up n the python docs
