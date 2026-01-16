x = "10"

print(x * 3 + "3")  # Output: 1010103 
# Explanation: The expression x * 3 concatenates the string "10" three times to produce "101010".
# Then, "3" is concatenated to the end of "101010", resulting in "1010103".

#print(x * 2 + 3)    # This will raise a TypeError

# Explanation: The expression x * 2 concatenates the string "10" two times to produce "1010".
# However, adding an integer (3) to a string ("1010") is not allowed in Python, leading to a TypeError.

print(x * 2 + str(x)) # Output: 101010
print(x * 2 + x)    # Output: 101010