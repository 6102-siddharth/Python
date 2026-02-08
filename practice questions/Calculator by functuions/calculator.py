def Calculator(a,b,opp):
    if ( opp =="+"):
        return a+b
    elif( opp =="-"):
        return a-b
    elif(opp =="*"):
        return a*b
    elif(opp =="/"):
        return a /b
    elif(opp =="%"):
        return a%b
    else:
        return "Error"