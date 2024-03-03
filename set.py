'''
SETS:

{values_(Empty curly brackets is by default dictionary)}:set()
Mutable
Unordered
Unique Values
'''
set1 = {1,2,3,4,5,'a','b','c','d','e'}			# len = 10
print(set1)
print(type(set1))
print('-'*30)

# # Adding
set1.add(6)
print(set1)

# # Pop
popped_s1 = set1.pop()			# For pop() use another variable
print(popped_s1)
print(set1)

# # Remove
set1.discard('b')
print(set1)

# # Iterating
for i in set1:
	print(i)

# # Checking Values in set1:
print(2 in set1)				# True
print('b' in set1)				# True
print('xx' in set1)				# False

# # Set operations:
seta = {1,2,3,4,5,'a','b','c'}				# len = 8
setb = {4,5,6,7,8,'aa','bb','cc'}			# len = 8

# # Union
print('\nUnion')
print(seta | setb)					# All elements of 'seta' and 'setb'

# # Intersect
print('\nIntersection')
print(seta & setb)					# Mutual elements of 'seta' and 'setb'

# # Difference
print('\nDifference')
print(seta - setb)					# Shows remaining elements of 'seta' which are not mutual with 'setb'
print(setb - seta)					# Shows remaining elements of 'setb' which are not mutual with 'seta'

# # Symmetric Differencce
print('\nSymmetric Difference')
print(seta ^ setb)					# Removes all mutual elements

# # Clearing
myset1 = {1,2,3,4,5,6,7,8,9}
print(myset1)
print('Clearing')
myset1.clear()
print(myset1)
print('Cleared')
