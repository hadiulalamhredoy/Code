numbers = [1,2,3,4,5,6,7,8,9,10]

odds = []
for num in numbers:  
    if num % 2 == 1 and num % 5 == 0:  
        odds.append(num)

print(odds)
odd_nums = [num for num in numbers if num % 2 == 1]
#  odd_nums=[num for num in numbers if num %2  == 1]

print(odd_nums)

players = ['sakib', 'tamim', 'mushfiq', 'mustafiz']
ages = [34, 36, 38, 27]

ages_comb = []



for player in players:  
    print('player: ', player)
    for age in ages:  
        print(player, age)
        ages_comb.append([player, age])
print(ages_comb)

age_comb2 = [[player, age] for player in players for age in ages]       
print(age_comb2)    
