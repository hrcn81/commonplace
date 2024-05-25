'''
TUPLE:

()
Immutable
Can be ordered
Can keep duplicate values
'''


tup1 = (1,2,3,4,5,5,6)					# len = 7
print(tup1)
print(len(tup1))

# # Slicing
print('\nSlicing')
print(tup1[1:4])				  # (2, 3, 4)
print(tup1[::-1])			  	# (6, 5, 5, 4, 3, 2, 1)

# # Concatenate
print('\nConcatenate')
contup1 = (1,2,3,4,5)
contup2 = (4,5,6,7,8)
con = contup1 + contup2
print(con)						      # (1, 2, 3, 4, 5, 4, 5, 6, 7, 8)
print(tuple(sorted(con)))		# (1, 2, 3, 4, 4, 5, 5, 6, 7, 8)

# # Iterating
print('\nIterating')
tupiter = ('a','b','c','d','e','f')
for i in tupiter:
	print(i,end = ' ')			# a b c d e f
print()

# # Checking Element in tuple
print('\nChecking Element in tuple')
print(2 in tup1)				  # True
print(88 in tup1)				  # False

# # Checking Count
print('\nChecking Count')
tupcount = (1,1,1,2,2,3,4,4,5,5,5,5,6,7,8,9)
print(tupcount.count(1))		# 3
print(tupcount.count(5))		# 4
print(tupcount.count(88))		# 0

# # Finding Index
print('\nFinding Index')
tupind = (1,2,3,4,5,6,7,8)
print(tupind.index(5))			  # 4
# print(tupind.index(88))			# ERROR

# # Multiplying Tuple
print('\nMultiplying Tuple')
tupmul = (1,11,2,22)
print(tupmul * 2)				      # Duplicates the tuple --> (1, 11, 2, 22, 1, 11, 2, 22)
