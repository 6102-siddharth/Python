# #1. Store following word meanings dict:
# table:"A piece of furniture","list of facts & figures"
# cat:"a small animal"

dict={"table":["A piece of Furniture","List of facts and Figures"],
      "cat":"A Small Animal"}
print(dict)

# 2. You are given a list of subjects for students . Assume one classroom is required for 1 subject . 
# How many classrooms are needed by all students.
# "python","java","c++","python","js","java","python","java","c++","c"
subjects={
    "python","java","c++","python","js","java","python","java","c++","c"
}
print(subjects)
len_s=len(subjects)
print("TOtal Requires Classroms =",len_s)

# 3.WAP to enter marks of 3 subjects from user and store them in a dictinary .
#  start with an empty dictinary and one by one . 
# Use subject name as key and marks as value
marks={}

s1=int(input("Enter Chemistry Marks:"))
marks.update({"chem":s1})

s2=int(input("Enter Maths Marks:"))
marks.update({"mat":s2})

s3=int(input("Enter Physics Marks:"))
marks.update({"phy":s3})

print(marks)

# 4. Figure out a way to store 9 and 9.0 as seperate values in the set
# (you can take help of builtin data types)
# Method 1:

values={9,"9.0"}
print(values)

# Method 2:
values={("int",9),
        ("float",9.0)}
print(values)