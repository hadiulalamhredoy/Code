#def
def sum(num1,num2, num3=0,num4=0,num5=0):
    result = num1 + num2 + num3 + num4 + num5
    return result  

total = sum(34,45,5)
print('total: ',total)

#args  
def all_sum(num1 ,num2, *numbers):
     print(numbers)
     sum = 0
     for num in numbers:
         print(num)
         sum += num
     return sum

    #   sum = sum + num   
     

      

     total  = all_sum(34,45,5,6) 
     
