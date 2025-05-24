# Class methods =   Allow operations related to the class itself
#                   Take (cls) as the first parameter, which represents the class itself.

# Let's make a student class:
class Student:
    count = 0  # We make a class variable of count to count the amount of students
    total_gpa = 0  # We make an other one to count the total gpa

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        # Each time we make an object with Student, we are gonna add 1 to count:
        Student.count += 1
        # Each time the GPA is registered, we are gonna add it to the total gpa:
        Student.total_gpa += gpa

    # Let's make an instance method of "get_info":
    def get_info(self):
        return f"Name: {self.name}", f"GPA: {self.gpa}"

    # Let's make a class method that uses the class's data:
    @classmethod  # we make a decorator
    def get_count(cls):  # Instead of self, we use cls as a first parameter
        return f"Number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return False
        else:
            return f"Average GPA: {cls.total_gpa / cls.count}"


# Let's make some objects:
student1 = Student("Spongebob", 3.2)
student2 = Student("Squidward", 2.8)
student3 = Student("Patrick", -0.1)
# Let's test the class method:
print(
    student1,  # ofc the objects to print
    student2,
    student3,
    Student.get_count(),  # To invoke a class method, you put the class name and then the method name
    Student.get_average_gpa(),
)
