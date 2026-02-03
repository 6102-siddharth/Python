# List :   A list is a built in data type which stores a set of a value

marks=[90,80,78,88,79]
print(type(marks))
print("Marks of 0 th index",marks[0])
print("Marks of 1 st index",marks[1])
print("------------------------------------")
str=["siddhu",90,77,"SIDHU"]
print(str[0])
str[0]="Vadgaonkar"     #adding new str in old list 
print(str)

print(len(str))     #Taking lenth of string or a list

print(str[2:])      #slicing the list like string
print(str[-4:])
print("-------------------------------------------------")
my_list=[3,1,2]
print(my_list)

my_list.append(4)
print("Added new element in list = ",my_list)

my_list.sort()
print("Sorted List = ",my_list)

my_list.sort(reverse=True)
print("Sorted in desc order = ",my_list)

my_list.reverse()
print("Reverse a list by reverse method = ",my_list)

my_list.insert(5,7)
print("inserted new element in a list method = ",my_list)