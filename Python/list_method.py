numbers = [12,45,98,68]
numbers.append(34)  # add element at the end of the list
print(numbers)  
numbers.insert(2, 100)  # add element at specific index 
print(numbers)  
numbers.remove(45)  # remove element by value   
print(numbers)  
numbers.pop()  # remove last element of the list    
print(numbers)  
numbers.pop(2)  # remove element by index   
print(numbers)  

if 98 in numbers:
    numbers.remove(98)
    if 8 in numbers:  
        numbers.remove(8)
print(numbers)

last = numbers.pop()  # remove last element and return it
print('last element: ', last)   
#  index  = numbers.index(68)  # find the index of an element
# print(index)
