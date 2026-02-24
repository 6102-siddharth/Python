# Del keyword is used to delete a object or object properties
class Student():
    def __init__(self,name):
        self.name=name

s1=Student("Siddharth")    # Here object is created

print(s1.name)         
del s1.name          #Here object is deleted
print(s1.name)