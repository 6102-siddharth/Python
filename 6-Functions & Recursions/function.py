# Creating function for Calculations like sum

def calcualte_sum(a,b):
    return a+b


sum=calcualte_sum(4,5)
print("Sum=",sum)


# WAP to calculate the avg of 3 numbers

def avg_3nums(a,b,c):
    avg=(a+b+c)/3
    return avg

avg=avg_3nums(6,6,6)
print("Average of given 3 numbers are",avg)

# Build in Function Print() in Python 

print("Siddharth","Vadgaonkar")

print("Siddharth", end="$")
print("Vadgaonkar")


print("------------------------------------")

# Default parameter in function in python

def cal_multi(a=1,b=1):
    return a*b

cal=cal_multi(4,8)
print(cal)