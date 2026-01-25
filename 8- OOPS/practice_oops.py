# By Normal method
class Student:
    def __init__ (self,name,s1,s2,s3):
        self.name=name
        self.s1=s1
        self.s2=s2
        self.s3=s3

s1=Student("Siddharth",80,80,89)
print(s1.name,s1.s1,s1.s2,s1.s3)

print("--------------------------------------------")

# By List menas Marks are given in list
class Students:
    def __init__(self,name1,marks):
        self.name1=name1 
        self.marks=marks

    def get_avg(self):
        sum=0
        for value in self.marks:
            sum +=value
        print("Hii",self.name1,"Your Average Score is:",sum/3)

s1=Students("Siddhu",[80,88,89])
s1.get_avg()