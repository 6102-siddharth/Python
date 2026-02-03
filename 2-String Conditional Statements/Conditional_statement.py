#Conditional Statements

#if-elif-else

#age=21
age=int(input("Enter Your age:"))
if(age >=18):
    print("You are eligible for Voting")
    print("You can drive a bike")

print("--------------------------------------------------------------")
#printing the students marks

marks=int(input("Enter students marks:"))
if(marks >=90):
    print("Excellent")
elif(marks >=75):
    print(" Very Good")
elif(marks >=50):
    print("TO study more")
else:
    print("Fail")


# #voting eligible
# age=int(input("Enter Your Age="))

# if(age >= 18):
#     print("You are Eligible For voting")
#     print("You are Eligible for Driving a bike and Car")

# print("-------------------------------------------------")

# #checking students marks with conditinal staements

# mark=int(input("Enter marks to see student result = "))
# if(mark>=80):
#     print("Excellent")
# elif(mark >= 60):
#     print("Good")
# elif(mark >= 36 and mark <60):
#     print("TO study more")
# else:
#     print("fail")