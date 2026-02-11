# WAP to print the length of a list (list is a parameter)
def l_list(li):
    return len(li)

le=l_list("Siddharth Vadgaonkar")
print(le)

print("**********************************************")
# WAP to print the element of a list in a single line (list is the parameter)
city=["Miraj","Sangli","Pune","Kolhapur"]

def s_line(list):
    for item in list:
        print(item,end=" ")

s_line(city)


# WAP to find the Factorial of n (n is the paramaeter)
print("\n-------------------------------------------")
def factorial(n):
    if (n < 0):
        print("Negative number not Exists")
    elif( n == 0):
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact

num=int(input("Enter Number to find the Factorial:"))
facto= factorial(num)
print(facto)
        

# WAP to convert USD to INR

def cash_converter(usd_value):
    inr_val=usd_value * 91.75
    print(usd_value,"USD = ",inr_val,"INR")


amount=float(input("Enter USD Doller to convrt in INR:"))
am=cash_converter(amount)


# Practice Question

def Numbers(n):
    if (n %2 == 0):
        print("Even Number")
    else:
        print("Odd Number")
    
nums=int(input("Enter Number to see Even or Odd:"))
Numbers(nums)