"""Let a string be "Hello,World!" 

what will be the output of s[ :7], s[7:], s[1:5], s[-5:-2] s[0:2:5] ?"""

s = "Hello,World!"
print(s[:7])    # Output: Hello,W
print(s[7:])    # Output: orld!
print(s[1:5])   # Output: ello
print(s[-5:-2]) # Output: orl
print(s[0:5:2]) # explanation: start at index 0, go up to index 5 (not including 5), step by 2 Output: Hlo