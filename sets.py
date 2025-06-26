#Unordered collection of unique elements. Do not allow duplicates. Cann add and remove values.
'''
my_set = {1, 2, 3, 4, 5}
print(my_set)

#Adding a value
my_set.add(6)
print(my_set)

#Removing a value
my_set.remove(4)
print(my_set)
'''

#Operations with sets:
#Union - combines two sets and removes any duplicates.
#Intersection - finds common elements between two sets
#Difference - finds the elements that are present in one set but not the other.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2) # Union
print(union_set)

inter_set = set1.intersection(set2) # Intersection
print(inter_set)

diff_set = set1.difference(set2) # Difference - "What is in set1 that is not in set2?"
print(diff_set)