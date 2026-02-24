a=int(input("Enter First Number:"))
b=int(input("Enter Second Number"))

print("\n Select Operator To perform Operations:")

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Floor Division")

choice =int(input("Enter Number (1-5) for Opearations="))

if choice == 1:
    print("Addition of",a,"and",b,"is =",a+b)
elif choice ==2:
    print("Substraction of",a,"and",b,"is =",a-b)
elif choice ==3:
    if (b!=0):
     print("Multiplication of",a,"and",b,"is =",a*b)
elif choice ==4:
   print("Division of",a,"and",b,"is =",a/b)
elif choice ==5:
   print("Modulus of",a,"and",b,"is =",a%b)
elif( choice ==6):
   print("Floor Diviaion of",a,"and",b"is=",a//b)

else:
   print("Invalid Input",choice)