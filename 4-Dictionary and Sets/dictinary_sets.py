info={
    "name":"Siddharth",
    "age":22,
    "Education":"Bachlor's Of Technology",
    "College_CGPA":"7.2"
}
print(info)
print("------------------------------------------")

list={
    "name":"Siddharth",
    "CGPA":7.2,
    "marks":"[90,88,67,77,56]",
    "subjects":"(mat,sci,ss,bio,chem)" ,
    12:111,
    7.2:"College"
}
print(list)

#dictionary does not allow duplicate keys 
# in dict we access value by there key

print("name=",list["name"])
print(list["subjects"])
print(list[12])

#we can also change teh value by using key
list["name"]="Siddharth"
list["surname"]="'Vadgaonkar"
print(list)

n_dict={}
n_dict["name"]="Siddharth"              #adding new key value in dectionary
print(n_dict)

dict={
    "name":"Siddharth",
    "subjects":{
        "maths":89,
        "phy":80,
        "chem":88            
    }
}
print(dict)
print("Total Keys ",len(dict))  # len is used to calculate keys
print(dict["subjects"])  # accessing the nested dictionary
print(dict.keys())       # is shows all keys names
print(dict.values())     #It shows all values presenjt in the dictionary
print(dict.items())      # it returns all keys and values
print(dict.get("name"))  # we can access by key

print(dict.items())
# dict1={
#     "name":"sid",
#     "sname":"Vadgaonkar",
#     }
# print(dict1)

# pair = list(dict1.items())
# print(pair)

student={
    "name":"sid",
    "sname":"Vadgaonkar",
    "sub":{
        "math":90,
        "chem":80
    }
    
    }
print(student["name"])          #if variable name is wrong it shows error in code
print(student.get("sname"))     #if variable is wrong it shows none to output
student.update({"city":"Miraj"})
print(student)

print("method 2 to add another dict")
nem_dict={"city1":"sangli"}
student.update(nem_dict)
print(student)

print("---------------------------------------------")

print("Sets in python")
collection={1,2,3,4,(77,99)}
print(collection)
print(type(collection))
# set={1,2,2}
# print(set)
cols= set()
print(type(cols))

cols.add(99)
print(cols)

cols.add(88)
print(cols)

cols.remove(88)
print(cols)

cols.add(77)
print(cols)

cols.pop()
print(cols)
cols.add(1000)
print(cols)

cols.clear()
print(cols)

set1= {1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))

print(set1.intersection(set2))

