numbers=[12,56,98,78,12,56,98,78]
person1 = ['Kala chan', 'kalipur',24,'student']
person2 = ['Sakib Khan', 'Dhaka', 35, 'actor']
#key vaule pair  
#dictionary 
#object  
#hash table
#overlap with set  
#{keyu:vaule, key : vaule, key : vaule}
person = {'name': 'Sakib Khan', 'age': 35, 'profession': 'actor'}       
print(person) #this will print the dictionary
print(person['name']) #this will print 'Sakib Khan' 
print(person['age']) #this will print 35    
person['age'] = 36 #this will change the value of 'age' to 36   
print(person) #this will print the updated dictionary   
person['country'] = 'Bangladesh' #this will add a new key-value pair to the dictionary
print(person) #this will print the updated dictionary with the new key-value pair
print(person.keys()) #this will print the keys of the dictionary
print(person.values()) #this will print the values of the dictionary

#special dictionary looking 

for key, vaule in person.items():
    print(key,vaule) #this will print each key-value pair on a new line in the format 'key: value'  

