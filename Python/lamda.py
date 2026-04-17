#lamda  

def double(x):
     return x*2

double = lambda num: num*2
square = lambda num: num**2     


result =  double(44)
print(result)
add = lamda x, y : x + y  


numbers = [12,56,98,78,12,56,98,78]         
doubled_numbers = list(map(lambda x: x*2, numbers)) #this will create a new list with each number in the original list doubled      

actors = [
     {'name': 'Sakib Khan', 'age': 35, 'profession': 'actor'},
     {'name': 'Salman Shah', 'age': 55, 'profession': 'actor'},
     {'name': 'Sabila Nur', 'age': 25, 'profession': 'actor'}
]

juniors = filter(lambda actor : actor['age'] < 40,  actors)
Fivers = filter(lambda actor : actor['age'] >= 40,  actors)