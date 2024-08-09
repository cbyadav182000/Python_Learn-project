# Creating sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = {5, 6, 7}

# Adding elements
set_a.add(8)

# Removing elements
set_a.remove(1)
set_b.discard(5)

# Union
union_ab = set_a.union(set_b)

# Intersection
intersection_ab = set_a.intersection(set_b)

# Difference
difference_ab = set_a.difference(set_b)

# Symmetric difference
symmetric_difference_ab = set_a.symmetric_difference(set_b)

# Checking subset and superset
subset_check = {2, 3}
print(subset_check.issubset(set_a))  # True
print(set_a.issuperset(subset_check))  # True

# Checking disjoint sets
print(set_a.isdisjoint(set_c))  # False

# Copying a set
set_copy = set_a.copy()

print(set_a)
print(set_b)
print(set_c)
print(union_ab)
print(intersection_ab)
print(difference_ab)
print(symmetric_difference_ab)
print(set_copy)
