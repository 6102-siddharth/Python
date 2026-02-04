# # #WAP to ask the user to enter names of their 3 favorite movies and store them in a list

# # list0=input("Enter First Movie name:")
# # list1=input("Enter Second Movie Name:")
# # list2=input("Enter Third Movie Name:")
# # list=[list0,list1,list2]
# # print("New List =",list)

# # # print("--------------------------------------")
print("Another Method ")
list=[]
print(list)
list.append(input("Enter First Movie Name:"))
list.append(input("Enter Second Movie Name:"))
list.append(input("Enter Third Movie Name:"))
print("New List",list)

# #WAP to check if a list contains a palidrome of elements (hint copy() method)
list1=[1,2,1]
list2=[1,2,3]

copy_list=list1.copy()
copy_list.reverse()

if(list1==copy_list):
    print("It is Palindrome")
else:
    print("It is not Palindrome")

#WAP to count the number of Students with the "A" grade in the following tuple
#["c","D","A","A","B","B","A"]

tuple=("C","D","A","A","B","B","A")
print("Repeted of A is=")
print(tuple.count("A"))



#Store the above Values in a list and store them from "A" to "D"
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)