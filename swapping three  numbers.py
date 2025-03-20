a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

temp = a
a=b
b=c
c=temp

print("numbers after swapping are")
print("a=",a)
print("b=",b)
print("c=",c)