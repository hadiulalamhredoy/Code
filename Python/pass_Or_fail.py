a = int(input("Enter your mark: "))

if a >= 80 and a <= 100:
    print("You got A+")
elif a >= 70 and a <= 79:
    print("You got A")
elif a >= 60 and a <= 69:
    print("You got A-")
elif a >= 50 and a <= 59:
    print("You got B")
elif a >= 40 and a <= 49:
    print("You got C")
elif a >= 30 and a <= 33:
    print("You got D")
elif a >= 32 and a <= 0:
    print("You Failed") 
else: 
    print("Invalid Input")