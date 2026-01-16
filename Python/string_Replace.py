letter = '''
Dear <|NAME|>, 
    I hope you are doing well. 
    I am happy to inform you that you have been selected for the position of <|POSITION|> at our company. 
    
    <|DATE|>
'''

print(letter.replace("<|NAME|>", "Tasfin").replace("<|POSITION|>", "Software Engineer").replace("<|DATE|>", "1st Dec 2025"))

#Explaination: The replace() method in Python is used to replace occurrences of a specified substring with another substring. 
# In this code, we have a multi-line string letter that contains placeholders for a name, position, and date. 
# We use the replace() method three times in a chained manner to replace each placeholder with the corresponding actual value. \
# The final output is a personalized letter with the placeholders replaced by "Tasfin", "Software Engineer", and "1st Dec 2025" respectively.