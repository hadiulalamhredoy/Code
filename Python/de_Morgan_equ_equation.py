# p -> q is logically equivalent to it contrapositive
# not(p) -> not(q) same as p -> q
# prove negation(p conjunction q) == negation p disjunction negation q, it's give you TRUE in return

p = True
q = False

r = not(p and q)
s = not(p) or not(q)

print('This is ',r == s)
print('Proved')