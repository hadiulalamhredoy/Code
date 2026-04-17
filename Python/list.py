# index =  0 1 2 3 4 5 6 7 8 9
numbers = [1,2,3,4,5,6,7,8,9,10]

#index  = -10 -9 -8 -7 -6 -5 -4 -3 -2 -1    
print(numbers[3],numbers[-3])

#list (start : end)  
print(numbers[2:5])  # 2,3,4
print(numbers[2:])   # 2,3,4,5,6,7,8,9,10   
print(numbers[:5])   # 1,2,3,4,5

#list (start : end : step)
print(numbers[1:10:2])  # 2,4,6,8,10    
print(numbers[::2])     # 1,3,5,7,9 
print(numbers[1::2])    # 2,4,6,8,10    
print(numbers[1,2,3])