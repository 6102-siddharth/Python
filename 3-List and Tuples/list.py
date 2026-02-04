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

#printing Whole list
my_list=[3,1,2]
print(my_list)

#append menas added new element at last
my_list.append(4)
print("Added new element in list = ",my_list)

#list is sorted in asc
my_list.sort()
print("Sorted List = ",my_list)

#list is sorted in desc order
my_list.sort(reverse=True)
print("Sorted in desc order = ",my_list)

#list is reversed
my_list.reverse()
print("Reverse a list by reverse method = ",my_list)

#insert method means adding new element with index and element
my_list.insert(5,7)
print("inserted new element in a list method = ",my_list)

#remove method means removing one element from the list
print(my_list)
my_list.remove(1)
print("Removed One element from list",my_list)

#Pop method means remove
print(my_list)
my_list.pop(1)
print("Poped the element  at index 2",my_list)



