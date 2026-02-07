# Print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]

# input=[1,4,9,16,25,36,49,64,81,100]

# for i in input:
#     print(i)
#  Search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]
imp=(1,4,9,16,25,36,49,64,81,100,16)
find=16
index=0

for i in imp:
    if (i == find):
        print("Number Found at index:",index)
        break
    index=index+1


print("*****************************************************")

#  Print numbers from 1 to 100
for i in range (1,100):
    print(i)


# print numbers from 100 to 1
for i in range(100,1,-1):
    print(i)


# print the multiplication table of a number n
n = int(input("Enter number to perform a Table:"))
for k in range(1,11):
    print(n,"*",k,"=",n*k)

print("888888888888888888888888888888888888888888888888888888888888")


# WAP to find the sum of first n numbers (using whiole)



# WAP to find the factorial of first n numbers( using for)