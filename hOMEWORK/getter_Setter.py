# yeh homework hai 

# Getter–Setter = Class ke attributes ko control karne ka system
#  Class ke attributes (department, salary, role, age, price, etc.)

# Jinko hum self.variable kehte hain.

# Agar hum in attributes ko directly change nahi dena chahte
# ya validation lagana chahte hain,
# ya secure rakhna chahte hain…

# To hum getter–setter use karte hain.


# Getter–Setter class ke attributes ko read/write karne ka controlled, safe, aur validated way hota hai.

# 

# Setter → Attribute change karne ka controlled way
# Data ko direct access se protect karna

# Validation add karna

# Only-read ya only-write banana

# Encapsulation ensure karna

# Modern Getter/Setter using @property (Pythonic Way)
class Student:
    def __init__(self, name, age):
        self._age = age
        self._name = name

    @property
    def age(self):
        # getter
        return self._age

    @age.setter
    def age(self, value):
        # setter
        if value < 0:
            print("Age negative nahi ho sakti!")
        else:
            self._age = value
