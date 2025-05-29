# @property =   Decorator used to define a method as a property (it can be accessed like an attribute)
#               Benefit: Add additional logic when read, write, or delete attribute
#               Gives you getter, setter, and deleter method

# Let's make a class of a rectangle:
class Rectangle:
    def __init__(self, length, height):
        self._length = length  # We define all of the variables as protected (with an underscore at the start)
        self._height = height
        self._area = length * height

    # What if I wanted to make it so that it returns 1 digit after the decimal, and "cm"?
    # Well we are gonna use the decorator:
    @property
    def width(self):
        return f"Width: {self._length:.1f}cm"  # To fix the warning (line 13), we use the protected version of the
        # variables for it

    @property
    def height(self):
        return f"Height: {self._height:.1f}cm"  # same here

    @property
    def area(self):
        return f"Area: {self._area:.1f}cm²"  # and here

    # That's the getter method :))
    # Now let's go to the setter method
    # To call one, we use the decorator: @<method name>.setter:
    @width.setter
    def width(self, new_width):  # We use the same name as the getter method
        if new_width > 0:
            self._width = new_width
        else:
            print("Width is too small!!!")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.height = new_height
        else:
            print("Height is too small!!!")

    # That's the setter method :D
    # To make a deleter method, it's kinda the same as the setter method: @<method name>.deleter
    @width.deleter
    def width(self):
        del self._length
        print("Length is gone. Your rectangle is now a line")

    @height.deleter
    def height(self):
        del self._height
        print("Height is gone. Your rectangle is now a line")


# Let's print an object:
rectangle = Rectangle(3, 4)
print(
    rectangle._length
)  # We get a warning, because the self variables are protected, and are meant to be only used inside of the class. but not anymore!
print(rectangle._height)

# Let's use the getter method:
rectangle.height = 10
rectangle.width = 26

# Let's use the deleter method:
del rectangle._width

print(rectangle.area)
print(rectangle.height)
print(rectangle._length)
