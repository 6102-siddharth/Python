# File reading or Writing Operation in i/p and o/p file

f=open("demo.txt","+r")

data=f.read()
print(data)
print(type(data))
f.close()