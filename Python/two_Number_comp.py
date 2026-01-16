"""Let a and b is two integers which is user-defined. Compare 3 conditions a>b, a<b, and a==b """

a = int(input("Enter (a)number: "))
b = int(input("Enter (b)number: "))

c = a < b
d = a > b
e = a == b

print(f"a is {a} and b is {b}, a < b is", c)
print(f"a is {a} and b is {b}, a > b is", d)
print(f"a is {a} and b is {b}, a = b is", e) #f-string is formatted string literal