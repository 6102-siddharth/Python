# Write a recursive function to calculate the sum of first n natural numbers 

def natural_sum(n):
    if (n ==0):
        return 0
    return natural_sum(n-1) + n
num=int(input("Enter Number to see addition of the numbers from 0="))
sum=natural_sum(num)
print(sum)



# Write a Recursive Function to print all elements in a list
# ( Hint:- USe list and index as paramaeter)
def print_list(list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=["Apple","Banana","Litchi"]
print_list(fruits)