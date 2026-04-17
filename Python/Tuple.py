def multiple():
    return 1, 2, 3  
# print(multiple()) #this will return a tuple (1, 2, 3)   
things =  'pen', 'pencil', 'eraser' #this will also create a tuple ('pen', 'pencil', 'eraser')
#print(tyoe(things)) #this will print <class 'tuple'>
# print(things[0]) #this will print 'pen' 
# print(things[-2])
# print(things[3:6])

if 'phone' in things:
    print('phone is present in things')

    for item in things:
         print(item)
         

things[0]='Python with Tamim Bhai'
#this will give an error because tuples 

#ignore 
print(len(things)) #this will print 3 because there are 3 items in the tuple
mega = ([1, 2, 3], 'hello', (4, 5, 6)) #this is a tuple that contains a list, a string, and another tuple
print(mega[0]) #this will print [1, 2, 3]
print(mega[1]) #this will print 'hello'
mega[0][1]=666
print(mega) #this will print ([1, 666, 3], 'hello', (4, 5, 6)) because we changed the second element of the list inside the tuple
