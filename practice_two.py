import math
import numpy as np

def compute_area(radius):
    return math.pi * radius**2

for r in np.arange(1.0, 100.0, 0.5):
    area = compute_area(r)
    print(f"Radius: {r}, Area: {area}")
    if area > 1000:
        print("Area exceeded 1000, stopping computation.")
        break
print("\n")
# This code computes the area of circles with increasing radius until the area exceeds 1000.

new_range = np.arange(1.0, 100.0, 0.5)
for r in new_range:
    area = compute_area(r)
    while area <= 2500:
        print(f"Radius: {r}, Area: {area}")
        break
    if area > 2500:
        print("Area exceeded 2500, stopping computation.")
        break
print("\n")
# This code computes the area of circles with increasing radius until the area exceeds 2500.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Ruffles", 2)
dog2 = Dog("Butch", 10)
dog3 = Dog("Helga", 3)

print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old.")
print(f"{dog3.name} is {dog3.age} years old.")

dog2.bark()
# This code defines a Dog class and creates instances of dogs, printing their details and making one bark.
