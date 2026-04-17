def full_name(first, last):
    name = f'full name is : {first} {last}'
    return name 

# take parameters  in order(serial wise)
# name = full_name('jannatul', 'sneha')
name = full_name(last='sneha', first='jannatul')
print(name)

def famous_name(first,last,title,addition):
    name =  f'{title} {first} {last} {addition}'        
    
    for key, value in addition.items():
        print(key, value)   
      
    
    return name 
    
    name = famous_name(first='tAHER',last='Ali', title='Dr.', addition='PhD')

    # def function_name(num1,num2, *args, **kargs):

    def a_lot(num1,num2):  
        sum  =  num1 + num2
        mult = num1 * num2      
        sub = num1 - num2               
        
        return sum,mult,sub
    
    #    everything = a_lot(34,45)        
    #      print(everything)  
    