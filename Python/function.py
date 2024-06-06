
'''
FUNCTIONS

'def' : Keyword used to define the function
'''

def greet():						# greet ---> name of the function
	print(i,"Hey! Mayank. Your function is working")
greet()								# Hey! Mayank. Your function is working

for i in range(1,100 + 1):
	print(i,greet())				# Gives None
	print(i,end = ' ')
	greet()						# Won't give None

[greet() for i in range(10)]		# runs greet function 10 times


'''
In function if you use same fucntion again then the last function you've written will be executed
'''
def updating():
	print('First Update')
def updating():
	print('Second Update')
def updating():
	print('Third Update')

# updating()
'''
In above all functions have same name 'updating()'.So, the last updated function will work
'''


# Global variable & Local variable (Scope of the function)
g_val = 10						# Global Variable
def greet():
	l_val = 5					# Local Variable
	print(g_val,l_val)
greet()							# 10 5
print(g_val)					# 10
# print(l_val)					# ERROR :- B'koz l_val is the local variable for the function.So, it can't be called/printed outside of the function



# Multiple variable in function

def greet(n):
	print('Hello!',n.upper())
greet('Mayank')						# Hello! MAYANK

def greet(n):
	print('Hello!',n.upper())
greet()								# ERROR

def greet(n = 'Nothing to pass'):		# Default parameter
	print('Hello!',n.upper())
greet()								# Hello! NOTHING TO PASS


def subm(a = 0,b = 0):
	print(a,b,a+b)

subm(5,2)					# 5 2 7
subm(9)						# 9 0 9
# subm(,5)					# ERROR
subm(a = 5,b = 10)			# 5 10 15
subm(a = 10,b = 5)			# 10 5 15
# subm(x = 2,y = 3)			# ERROR :- B'koz input in function is (a,b)
subm()						# 0 0 0


# RETURN
def subm(a = 0,b = 0):
	return a,b,a + b			# If parameters are more than one than it return on the tuple

var1 = subm(5,2)
print(var1)						# (5, 2, 7)
print(type(var1))				# <class 'tuple'>


def subm(a = 0,b = 0):
	return (a + b)

var1 = subm(5,2)
print(var1)						# 7
print(type(var1))				# <class 'int'>


# Packing | Unpacking
def fun1(a=0,b=0,c=0):
	sum1 = a + b + c
	mul1 = a * b * c
	return sum1,mul1

s1,s2 = fun1(1,2,3)
print(s1,s2)				# 6 6



# Square of list in function
l1 = [1,2,3,4,5]
def square_list(mayank):
	return [i**2 for i in mayank]

print(square_list(l1))			# [1, 4, 9, 16, 25]


# Cube of list in function
l2 = [1,2,3,4,5]
def cube_list(mayank):
	return [i**3 for i in mayank]

print(cube_list(l2))			# [1, 8, 27, 64, 125]


def final(list1,list2):
	return square_list(list1) + cube_list(list2)		# adding both lists using above function
print(final(l1,l2))				# [1, 4, 9, 16, 25, 1, 8, 27, 64, 125]

'''
FUNCTIONS

'def' : Keyword used to define the function
'''

def greet():						# greet ---> name of the function
	print(i,"Hey! Mayank. Your function is working")
greet()								# Hey! Mayank. Your function is working

for i in range(1,100 + 1):
	print(i,greet())				# Gives None
	print(i,end = ' ')
	greet()						# Won't give None

[greet() for i in range(10)]		# runs greet function 10 times


'''
In function if you use same fucntion again then the last function you've written will be executed
'''
def updating():
	print('First Update')
def updating():
	print('Second Update')
def updating():
	print('Third Update')

# updating()
'''
In above all functions have same name 'updating()'.So, the last updated function will work
'''


# Global variable & Local variable (Scope of the function)
g_val = 10						# Global Variable
def greet():
	l_val = 5					# Local Variable
	print(g_val,l_val)
greet()							# 10 5
print(g_val)					# 10
# print(l_val)					# ERROR :- B'koz l_val is the local variable for the function.So, it can't be called/printed outside of the function



# Multiple variable in function

def greet(n):
	print('Hello!',n.upper())
greet('Mayank')						# Hello! MAYANK

def greet(n):
	print('Hello!',n.upper())
greet()								# ERROR

def greet(n = 'Nothing to pass'):		# Default parameter
	print('Hello!',n.upper())
greet()								# Hello! NOTHING TO PASS


def subm(a = 0,b = 0):
	print(a,b,a+b)

subm(5,2)					# 5 2 7
subm(9)						# 9 0 9
# subm(,5)					# ERROR
subm(a = 5,b = 10)			# 5 10 15
subm(a = 10,b = 5)			# 10 5 15
# subm(x = 2,y = 3)			# ERROR :- B'koz input in function is (a,b)
subm()						# 0 0 0


# RETURN
def subm(a = 0,b = 0):
	return a,b,a + b			# If parameters are more than one than it return on the tuple

var1 = subm(5,2)
print(var1)						# (5, 2, 7)
print(type(var1))				# <class 'tuple'>


def subm(a = 0,b = 0):
	return (a + b)

var1 = subm(5,2)
print(var1)						# 7
print(type(var1))				# <class 'int'>


# Packing | Unpacking
def fun1(a=0,b=0,c=0):
	sum1 = a + b + c
	mul1 = a * b * c
	return sum1,mul1

s1,s2 = fun1(1,2,3)
print(s1,s2)				# 6 6



# Square of list in function
l1 = [1,2,3,4,5]
def square_list(mayank):
	return [i**2 for i in mayank]

print(square_list(l1))			# [1, 4, 9, 16, 25]


# Cube of list in function
l2 = [1,2,3,4,5]
def cube_list(mayank):
	return [i**3 for i in mayank]

print(cube_list(l2))			# [1, 8, 27, 64, 125]


def final(list1,list2):
	return square_list(list1) + cube_list(list2)		# adding both lists using above function
print(final(l1,l2))				# [1, 4, 9, 16, 25, 1, 8, 27, 64, 125]

'''
FUNCTIONS

'def' : Keyword used to define the function
'''

def greet():						# greet ---> name of the function
	print(i,"Hey! Mayank. Your function is working")
greet()								# Hey! Mayank. Your function is working

for i in range(1,100 + 1):
	print(i,greet())				# Gives None
	print(i,end = ' ')
	greet()						# Won't give None

[greet() for i in range(10)]		# runs greet function 10 times


'''
In function if you use same fucntion again then the last function you've written will be executed
'''
def updating():
	print('First Update')
def updating():
	print('Second Update')
def updating():
	print('Third Update')

# updating()
'''
In above all functions have same name 'updating()'.So, the last updated function will work
'''


# Global variable & Local variable (Scope of the function)
g_val = 10						# Global Variable
def greet():
	l_val = 5					# Local Variable
	print(g_val,l_val)
greet()							# 10 5
print(g_val)					# 10
# print(l_val)					# ERROR :- B'koz l_val is the local variable for the function.So, it can't be called/printed outside of the function



# Multiple variable in function

def greet(n):
	print('Hello!',n.upper())
greet('Mayank')						# Hello! MAYANK

def greet(n):
	print('Hello!',n.upper())
greet()								# ERROR

def greet(n = 'Nothing to pass'):		# Default parameter
	print('Hello!',n.upper())
greet()								# Hello! NOTHING TO PASS


def subm(a = 0,b = 0):
	print(a,b,a+b)

subm(5,2)					# 5 2 7
subm(9)						# 9 0 9
# subm(,5)					# ERROR
subm(a = 5,b = 10)			# 5 10 15
subm(a = 10,b = 5)			# 10 5 15
# subm(x = 2,y = 3)			# ERROR :- B'koz input in function is (a,b)
subm()						# 0 0 0


# RETURN
def subm(a = 0,b = 0):
	return a,b,a + b			# If parameters are more than one than it return on the tuple

var1 = subm(5,2)
print(var1)						# (5, 2, 7)
print(type(var1))				# <class 'tuple'>


def subm(a = 0,b = 0):
	return (a + b)

var1 = subm(5,2)
print(var1)						# 7
print(type(var1))				# <class 'int'>


# Packing | Unpacking
def fun1(a=0,b=0,c=0):
	sum1 = a + b + c
	mul1 = a * b * c
	return sum1,mul1

s1,s2 = fun1(1,2,3)
print(s1,s2)				# 6 6



# Square of list in function
l1 = [1,2,3,4,5]
def square_list(mayank):
	return [i**2 for i in mayank]

print(square_list(l1))			# [1, 4, 9, 16, 25]


# Cube of list in function
l2 = [1,2,3,4,5]
def cube_list(mayank):
	return [i**3 for i in mayank]

print(cube_list(l2))			# [1, 8, 27, 64, 125]


def final(list1,list2):
	return square_list(list1) + cube_list(list2)		# adding both lists using above function
print(final(l1,l2))				# [1, 4, 9, 16, 25, 1, 8, 27, 64, 125]

'''
FUNCTIONS

'def' : Keyword used to define the function
'''

def greet():						# greet ---> name of the function
	print(i,"Hey! Mayank. Your function is working")
greet()								# Hey! Mayank. Your function is working

for i in range(1,100 + 1):
	print(i,greet())				# Gives None
	print(i,end = ' ')
	greet()						# Won't give None

[greet() for i in range(10)]		# runs greet function 10 times


'''
In function if you use same fucntion again then the last function you've written will be executed
'''
def updating():
	print('First Update')
def updating():
	print('Second Update')
def updating():
	print('Third Update')

# updating()
'''
In above all functions have same name 'updating()'.So, the last updated function will work
'''


# Global variable & Local variable (Scope of the function)
g_val = 10						# Global Variable
def greet():
	l_val = 5					# Local Variable
	print(g_val,l_val)
greet()							# 10 5
print(g_val)					# 10
# print(l_val)					# ERROR :- B'koz l_val is the local variable for the function.So, it can't be called/printed outside of the function



# Multiple variable in function

def greet(n):
	print('Hello!',n.upper())
greet('Mayank')						# Hello! MAYANK

def greet(n):
	print('Hello!',n.upper())
greet()								# ERROR

def greet(n = 'Nothing to pass'):		# Default parameter
	print('Hello!',n.upper())
greet()								# Hello! NOTHING TO PASS


def subm(a = 0,b = 0):
	print(a,b,a+b)

subm(5,2)					# 5 2 7
subm(9)						# 9 0 9
# subm(,5)					# ERROR
subm(a = 5,b = 10)			# 5 10 15
subm(a = 10,b = 5)			# 10 5 15
# subm(x = 2,y = 3)			# ERROR :- B'koz input in function is (a,b)
subm()						# 0 0 0


# RETURN
def subm(a = 0,b = 0):
	return a,b,a + b			# If parameters are more than one than it return on the tuple

var1 = subm(5,2)
print(var1)						# (5, 2, 7)
print(type(var1))				# <class 'tuple'>


def subm(a = 0,b = 0):
	return (a + b)

var1 = subm(5,2)
print(var1)						# 7
print(type(var1))				# <class 'int'>


# Packing | Unpacking
def fun1(a=0,b=0,c=0):
	sum1 = a + b + c
	mul1 = a * b * c
	return sum1,mul1

s1,s2 = fun1(1,2,3)
print(s1,s2)				# 6 6



# Square of list in function
l1 = [1,2,3,4,5]
def square_list(mayank):
	return [i**2 for i in mayank]

print(square_list(l1))			# [1, 4, 9, 16, 25]


# Cube of list in function
l2 = [1,2,3,4,5]
def cube_list(mayank):
	return [i**3 for i in mayank]

print(cube_list(l2))			# [1, 8, 27, 64, 125]


def final(list1,list2):
	return square_list(list1) + cube_list(list2)		# adding both lists using above function
print(final(l1,l2))				# [1, 4, 9, 16, 25, 1, 8, 27, 64, 125]

'''
FUNCTIONS

'def' : Keyword used to define the function
'''

def greet():						# greet ---> name of the function
	print(i,"Hey! Mayank. Your function is working")
greet()								# Hey! Mayank. Your function is working

for i in range(1,100 + 1):
	print(i,greet())				# Gives None
	print(i,end = ' ')
	greet()						# Won't give None

[greet() for i in range(10)]		# runs greet function 10 times


'''
In function if you use same fucntion again then the last function you've written will be executed
'''
def updating():
	print('First Update')
def updating():
	print('Second Update')
def updating():
	print('Third Update')

# updating()
'''
In above all functions have same name 'updating()'.So, the last updated function will work
'''


# Global variable & Local variable (Scope of the function)
g_val = 10						# Global Variable
def greet():
	l_val = 5					# Local Variable
	print(g_val,l_val)
greet()							# 10 5
print(g_val)					# 10
# print(l_val)					# ERROR :- B'koz l_val is the local variable for the function.So, it can't be called/printed outside of the function



# Multiple variable in function

def greet(n):
	print('Hello!',n.upper())
greet('Mayank')						# Hello! MAYANK

def greet(n):
	print('Hello!',n.upper())
greet()								# ERROR

def greet(n = 'Nothing to pass'):		# Default parameter
	print('Hello!',n.upper())
greet()								# Hello! NOTHING TO PASS


def subm(a = 0,b = 0):
	print(a,b,a+b)

subm(5,2)					# 5 2 7
subm(9)						# 9 0 9
# subm(,5)					# ERROR
subm(a = 5,b = 10)			# 5 10 15
subm(a = 10,b = 5)			# 10 5 15
# subm(x = 2,y = 3)			# ERROR :- B'koz input in function is (a,b)
subm()						# 0 0 0


# RETURN
def subm(a = 0,b = 0):
	return a,b,a + b			# If parameters are more than one than it return on the tuple

var1 = subm(5,2)
print(var1)						# (5, 2, 7)
print(type(var1))				# <class 'tuple'>


def subm(a = 0,b = 0):
	return (a + b)

var1 = subm(5,2)
print(var1)						# 7
print(type(var1))				# <class 'int'>


# Packing | Unpacking
def fun1(a=0,b=0,c=0):
	sum1 = a + b + c
	mul1 = a * b * c
	return sum1,mul1

s1,s2 = fun1(1,2,3)
print(s1,s2)				# 6 6



# Square of list in function
l1 = [1,2,3,4,5]
def square_list(mayank):
	return [i**2 for i in mayank]

print(square_list(l1))			# [1, 4, 9, 16, 25]


# Cube of list in function
l2 = [1,2,3,4,5]
def cube_list(mayank):
	return [i**3 for i in mayank]

print(cube_list(l2))			# [1, 8, 27, 64, 125]


def final(list1,list2):
	return square_list(list1) + cube_list(list2)		# adding both lists using above function
print(final(l1,l2))				# [1, 4, 9, 16, 25, 1, 8, 27, 64, 125]
