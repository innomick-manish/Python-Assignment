#Create a simple Person class and its attribute
class Person:
    attribute1= 'manish'
    attribute2= '23'
    attribute3= 'trainee'

    def details(self):
        print('Name of the person: ',self.attribute1)
        print('Age of the person: ',self.attribute2)
        print('designation of the person: ',self.attribute3)

bio = Person()
bio.details()

#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 22/7

    def perimeter(self):
        return 2 * self.radius * 22/7

Newcircle = Circle(5)
print(Newcircle.area())
print(Newcircle.perimeter())

#Write a Python class to get all possible unique subsets from a set of distinct integers.
#Input : [4, 5, 6]
#Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
class solution:
    def sub_sets(self, subset):
        return self.subsetsRecur([], sorted(subset))

    def subsetsRecur(self, current, subset):
        if subset:
            return self.subsetsRecur(current, subset[1:]) + self.subsetsRecur(current + [subset[0]], subset[1:])
        return [current]

print(solution().sub_sets([4, 5, 6]))

#Write a program that show difference between class and static method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# a class method to create a Person object by birth year.
    @classmethod
    def fromschool(cls, name, age):
        return cls(name, age)

# a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 20

student1 = Student('manish', 21)
student2 = Student.fromschool('rahul', 20)

print(student1.age)
print(student2.age)

# print the result
print(Student.isAdult(15))

#Give an example which shows the difference between constructor and method
class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

result= Addition(2,5)
print(result.sum())
