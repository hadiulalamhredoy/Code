a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))

c = a+b #without defining the type it takes string as a input and if we use + it mainly concateneted the string 

s = type(a)
d = type(c)

print("1st number was: ",a)
print("2nd number was: ",b)
print("Sum of two number: ", a+b)

print("Type of a is", s)
print("Type of a is", d)
