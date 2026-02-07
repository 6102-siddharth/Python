# Q. WAP to print numbers from 1 to 100
i=1
while(i<=100):
    print(i)
    i=i+1


# Q WAP to print numbers from 100 to 1
i=100
while (i>=1):
    print(i)
    i=i-1


# Q. WAP to print the multiplication table os  a number n
n=int(input("Enter number to perform Table:"))
i=1
while(i <=10):
    print(n,"*",i,"=",n*i)
    i=i+1


# WAP to print the element of the following list using loop:
input=[1,4,9,16,25,36,49,64,81,100]
ind=0

while(ind < len(input)):
    print(input[ind])
    ind+=1

# Another Example:
ip=["sid","say","ans","sar","sam"]
idx=0
while (idx <len(ip)):
    print(ip[idx])
    idx=idx+1

# WAP to search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]
inp=[1,4,9,16,25,36,49,64,81,100]

find=36
i=0
while (i < len(inp)):
    if(inp[i]== find ):
        print("Found Element at index:",i)
    i=i+1
