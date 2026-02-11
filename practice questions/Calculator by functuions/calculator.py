def Calculator(a,b,opp):
    if ( opp =="+"):
        return "Addition=",a+b
    elif( opp =="-"):
        return "Substraction=",a-b
    elif(opp =="*"):
        return "Multiplication=",a*b
    elif(opp =="/"):
        return "Division=",a /b
    elif(opp =="%"):
        return "Modulus=",a%b
    elif(opp == "//"):
        return "Floor Division=",a//b
    else:
        return "Error"
    
sum=Calculator(4,3,"//")
print(sum)