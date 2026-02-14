# Recursion:
    # Recursion means when a function calls itself Repeatedly


#I want to show numbers like 5,4,3,2,1 

def show(n):
    if (n ==0):
        return
    print(n)
    show(n-1)

show(5)


# For Factorial we can use a Recursion also
fact =1
def factorials(n):
    if (n==1 or n==0):
        return 1
    return fact(n-1) *n


print(factorials(5))