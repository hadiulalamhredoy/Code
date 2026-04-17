name = 'Sakib Khan'
name2 = "Sneha"

name3 = """
This is a multi-line string.    
"""
print(name)
print(name2)        


#String is a sequence of characters. It is a data type in Python that is used to represent text. Strings are enclosed in either single quotes (' ') or double quotes (" "). They can contain letters, numbers, symbols, and whitespace characters.
for char in name2:
    print(char) 

print(name2[3]) #indexing starts from 0
print(name2[1:6])
print(name2[-2])
print(name2[::-1])

#mutable means changeable
#immutable means you can't change it  
#name2[0]= 'R' #this will give an error because strings are immutable

if 'khan' in name2:
    # print('khan is present in name2')
    print('exists')
    
print(name2.upper()) #convert to uppercase
 

