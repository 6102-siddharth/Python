# Creating class and objects

#Easy example 

# class Car:
#     color='blue'
#     brand="Mercedes"


# c1=Car()
# print(c1.color)
# print(c1.brand)

# Constructor

class Student:
    name="siddharth"
    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding new student in Database...")



s1=Student("Siddharth",89)
print(s1.name,s1.marks)

s2=Student("Siddhu",90)
print(s2.name,s2.marks)