class Student():                #class created 
       college_name="ABC College" # One Tiem called no need to call Multiple times
      
       def __init__(self,name,marks):        # Parameterised Constructor
        self.name=name
        self.marks=marks

       def welcome(self):                    # Its a function inside a class                 
           print("Welcome Students",self.name)    

       def get_marks(self):
           return self.marks
s1=Student("Siddharth",70) #Passing parameters to object
# print(s1.college_name,s1.name,s1.marks) 
# s2=Student("Ansh",67)
# print(s2.college_name,s2.name,s2.marks)
# Method is called
s1.welcome()
print("Marks of S1 Student",s1.get_marks())