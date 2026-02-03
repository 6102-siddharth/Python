# Write a program to check if a number entered by user is odd or even
num=int(input("Enter a number to check Even="))
if( num %2==0):
    print("Even Number ")
else:
    print("Odd number")


print("-------------------------------------------------------------")
# Write a program to find the greatest of 3 numbers entered by the user
num1=int(input("Enter First Number:"))
num2=int(input("Enter second Number:"))
num3=int(input("Enter Third number:"))

if (num1 >num2 and num1>num3):
    print("First number is greater and number is =",num1)
elif(num2 >num1 and num2>num3):
    print("Second Number is Greater and number is =",num2)
else:
    print("Third Number is greater and number is =",num3)


print("-------------------------------------------------------------")

# Write a program to check if a number is a multiple of 7 or not
num=int(input("Enter to number check 7's multiple:"))
if num ==0:
    print("Enter another number zero is not valid")
elif(num %7 ==0):
    print("It is Multiple")
else:
    print("It is not multiple")