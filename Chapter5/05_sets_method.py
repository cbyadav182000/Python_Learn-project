# s={1,5,32,54,5,5,5,"chandar"}

# print(s, type(s))

# #add
# s.add(56)
# print(s,type(s))

#create a set
my_set = {1, 2, 3}
another_set = set([4, 5, 6])
my_set.add(4)

#remove set
my_set.remove(2)

#discard()
my_set.discard(3)

#Removing and Returning an Arbitrary Element
element = my_set.pop()

#Clearing All Elements:
my_set.clear()

#Union of Sets:\
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # {1, 2, 3, 4, 5}

#Intersection of Sets:
intersection_set = set1.intersection(set2)  # {3}

#Difference of Sets:
difference_set = set1.difference(set2)  # {1, 2}

#Symmetric Difference of Sets:

symmetric_difference_set = set1.symmetric_difference(set2)  # {1, 2, 4, 5}

#Checking Subset:
subset = {1, 2}
print(subset.issubset(set1))  # True

#Checking Superset:
print(set1.issuperset(subset))  # True

#Checking Disjoint Sets:
set3 = {6, 7, 8}
print(set1.isdisjoint(set3))  # True

#Copying a Set:
set_copy = set1.copy()

