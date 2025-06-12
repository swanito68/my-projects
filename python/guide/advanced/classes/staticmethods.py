# Static methods = A method that belongs t a class rather than any object from that class (instance)
#                  Usuallt used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

# Let's make an employee class:
class Employee:
    def __init__(self, name, position):  # the constructor
        self.name = name
        self.position = position

    # Let's make an instance method to get the info of the employee:
    def get_info(self):
        return f"His name is {self.name}, and he's a {self.position}"

    # This is an instance method, meaning other classes can inherit from it.
    # Now let's make a static method:
    @staticmethod  # we need a decorator to make need
    def is_valid_position(
        position,
    ):  # we do not need to work with any object from the constructor, therefore we do not put "self" in the parentheses
        valid_positions = ["cook", "janitor", "cashier", "manager"]
        return position.strip().lower() in valid_positions

    # We just made a static method


# We do not need to make an object for a static method:
# You put the class name, then the name of the method
print(Employee.is_valid_position("cook"))  # it should return True
print(Employee.is_valid_position("gooner"))  # it should return false

# Now let's make some objects:
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

# To get their info, in this case, you use the get_info method:
print(employee1.get_info(), employee2.get_info(), employee3.get_info())
