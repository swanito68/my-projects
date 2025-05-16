def pause():
    input("\nPress Enter to continue...\n")


def explain_classes():
    print("\n--- What is a Class? ---")
    print(
        "A class is a blueprint for creating objects. It defines attributes (data) and methods (functions)."
    )
    pause()


def example_instance_methods():
    print("\n--- Instance Methods ---")
    print(
        "Instance methods are regular methods that take 'self' as the first parameter.\n"
    )
    print("""
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}!")

p = Person("Alice")
p.greet()  # Output: Hi, I'm Alice!
""")
    pause()


def example_class_method():
    print("\n--- Class Methods ---")
    print(
        "Class methods take 'cls' as the first parameter and can access class-level data.\n"
    )
    print("""
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"There are {cls.count} instances.")

a = Counter()
b = Counter()
Counter.show_count()  # Output: There are 2 instances.
""")
    pause()


def example_static_method():
    print("\n--- Static Methods ---")
    print(
        "Static methods do not access instance or class data. They are like regular functions inside a class.\n"
    )
    print("""
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print(MathUtils.add(3, 5))  # Output: 8
""")
    pause()


def example_inheritance():
    print("\n--- Inheritance ---")
    print("Inheritance allows one class to inherit from another.\n")
    print("""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

d = Dog("Buddy")
c = Cat("Whiskers")
d.speak()  # Buddy says Woof!
c.speak()  # Whiskers says Meow!
""")
    pause()


def explain_polymorphism():
    print("\n--- Polymorphism ---")
    print(
        "Polymorphism means different classes can define the same method in different ways.\n"
    )
    print("""
animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    animal.speak()

# Output:
# Buddy says Woof!
# Whiskers says Meow!
""")
    pause()


def quiz():
    print("\n--- Quick Quiz ---")

    q1 = input("1. What keyword is used to define a class? ").strip().lower()
    print("✅ Correct!" if q1 == "class" else "❌ It's 'class'.")

    q2 = input("2. What is the first parameter of an instance method? ").strip().lower()
    print("✅ Correct!" if q2 == "self" else "❌ It's 'self'.")

    q3 = input("3. What decorator is used for class methods? ").strip().lower()
    print("✅ Correct!" if q3 == "@classmethod" else "❌ It's '@classmethod'.")

    q4 = input("4. What is the first parameter of a class method? ").strip().lower()
    print("✅ Correct!" if q4 == "cls" else "❌ It's 'cls'.")

    q5 = input("5. What decorator is used for static methods? ").strip().lower()
    print("✅ Correct!" if q5 == "@staticmethod" else "❌ It's '@staticmethod'.")

    q6 = input("6. What is polymorphism in OOP? ").lower()
    if "same" in q6 and ("different" in q6 or "override" in q6):
        print("✅ Correct!")
    else:
        print(
            "❌ Polymorphism allows different classes to use the same method name with different behavior."
        )


def main():
    print("🐍 Welcome to the Ultimate Python OOP Tutorial!\n")
    explain_classes()
    example_instance_methods()
    example_class_method()
    example_static_method()
    example_inheritance()
    explain_polymorphism()
    quiz()
    print("\n🎉 Thanks for learning OOP with Python!")


if __name__ == "__main__":
    # Declare these here for polymorphism example to work
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            print(f"{self.name} makes a sound")

    class Dog(Animal):
        def speak(self):
            print(f"{self.name} says Woof!")

    class Cat(Animal):
        def speak(self):
            print(f"{self.name} says Meow!")

    main()
