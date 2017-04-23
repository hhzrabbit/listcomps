def union(s1, s2):
    return s1 + [y for y in s2 if not y in s1]

def intersection(s1, s2):
    return [x for x in s1 if x in s2]

def set_difference(s1, s2):
    return [x for x in s1 if not x in s2]

def symmetric_difference(s1, s2):
    return set_difference(s1, s2) + set_difference(s2, s1)

def cartesian_product(s1, s2):
    return [(x, y) for x in s1 for y in s2]

a = [1, 2, 3]
b = [2, 3, 4]

print union(a, b)
print intersection(a, b)
print set_difference(a, b)
print set_difference(b, a)
print symmetric_difference(a, b)
print cartesian_product(a, b)
