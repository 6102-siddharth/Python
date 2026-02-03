str1="This is a string. \n Here are new \t  String"
print(str1)

print("String operations")
# Concatination
str2="my name is "
str3="Siddharth"

print(str2+str3)
n=len(str3)
print(n)

print("String Indexing")

str="Siddharth"
ch=str[5]
print("The given index value of char is:",ch)

# slicing the string
print("Slicing method")

str1="APNACOLLEGE"
# slc=str1[1:4]
print(str1[1:4])
print(str1[::4])
print(str1[-7:])  #reverse string

#string functions
str="i am studying python from ApnaCollege"
print(str.endswith("ege"))
print(str.startswith("I"))

print(str.capitalize())
print(str)

newstr=str.replace("ApnaCollege"," self study")
print(newstr)

# returning index
print(str.find("from"))

# count function

print(str.count("a"))


