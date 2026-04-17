#list ->> []
#tuple ->> ()
# set ->> {}
#set: unique items collection. No duplicate.

numbers = [12,56,98,78,12,56,98,78]
print(numbers) #this will print the list with duplicates

numbers_set = set(numbers) #this will convert the list to a set and remove duplicates
print(numbers_set) #this will print the set with unique items   
# sets are unordered, so we cannot access items by index    
# sets are mutable, we can add or remove items from a set   
numbers_set = set(numbers)
print(numbers_set) #this will print the set with unique items
numbers_set.add(55)
print(numbers_set)
numbers_set.remove(56)
print(numbers_set)

#numbers_set[0] = 100 #this will give an error because sets are unordered and do not support indexing
for item in numbers_set:
    print(item) #this will print each item in the set on a new line

    if 9  in numbers_set:
        print('9 is present in the set')    
    elif 98 in numbers_set:
        print('98 is present in the set')
        
        A = {1, 2, 3, 4}    
        B = {3, 4, 5, 6}    

        print(A & B)
        print(A | B) #AUB
        print(A - B) #A-B
        print(B - A) #B-A
        print(A ^ B) #symmetric difference (A-B)U(B-A)
        
