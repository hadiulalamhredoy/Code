# draw pyramid
for i in range(1, n + 1):
    
    spaces = " " * (n - i) 
    stars = "*" * (2 * i - 1)
    
    
    line = spaces + stars
    
    print(line)