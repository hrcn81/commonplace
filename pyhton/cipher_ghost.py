'''
Important Inbuilt Libraries

1.	math
2.	random
3.	datetime
4.	collection
5.	string
'''


'''
1.	math
'''
# import math
#
# print('x:')
# x = 10.8
# print(math.ceil(x))
# print(math.floor(x))
# print(math.trunc(x))
#
#
# print('\ny:')
# y = 3
# print(math.exp(y))
# print(math.log10(y))
#
#
# print('\nz:')
# z = 90
# print(math.sin(z))
# print(math.cos(z))
# print(math.tan(z))
#
#
# print('\nOthers:')
# print(math.pi)
# print(math.e)
# print(math.factorial(10))





'''
2.	Random
'''
# import random

# print(random.random())						# Generates random number between 0 to 1
# print(random.randint(1,3))					# Generates random number from 1 to 3 both end included
# print(random.choice([1,2,3,4,5]))				# Gives any random values from the list
# print(random.sample([1, 2, 3, 4, 5, 6], 3))	# Gives 3 samples from list
# print(random.sample([1,2,3,4,5,6],4))			# Gives 4 samples from list
# print(random.uniform(1.2,1.4))				# Generates random nomber between given range



# random.seed(10)								# Everytime generates same values
# print(random.random())						# Generates random number between 0 to 1
# print(random.randint(1,3))					# Generates random number from 1 to 3 both end included
# print(random.choice([1,2,3,4,5]))				# Gives any random values from the list
# print(random.sample([1, 2, 3, 4, 5, 6], 3))	# Gives 3 samples from list
# print(random.sample([1,2,3,4,5,6],4))			# Gives 4 samples from list
# print(random.uniform(1.2,1.4))




'''
3.	datetime
'''
# import datetime

# print(datetime.datetime.now())									# Gives current date & time
# print(datetime.datetime(2000,3,18,2,18))							# 2000-03-18 02:18:00
#
# print(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))		# 11/03/24 09:25:30

# date_1 = datetime.datetime(2000,3,18,2,18)
# date_2 = datetime.datetime.now()
# print((date_2 - date_1))					# 8759 days, 7:11:15.401633
# print((date_2 - date_1).days)				# 8759
# print((date_2 - date_1).days//30)			# Months 291
# print((date_2 - date_1).days//365)		# Years 23




'''
4.	collections
'''
# from collections import Counter,defaultdict,OrderedDict

# lst = [1,2,3,4,5,5,5,6,6,7]
# print(Counter(lst))

# d = defaultdict(int)
# d['a'] += 2
# print(d)

# d1 = OrderedDict()
# d1['one'] = 1
# d1['two'] = 2
# print(d1)




'''
5.	string
'''
# str1 = 'Mayank 1832 Solanki'
# for i in str1:
# 	if i not in '1234567890':
# 		print(i)

# import string

# print(string.ascii_letters)				# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.ascii_lowercase)				# abcdefghijklmnopqrstuvwxyz
# print(string.ascii_uppercase)				# ABCDEFGHIJKLMNOPQRSTUVWXYZ
#
# print(string.digits)						# 0123456789
# print(string.hexdigits)					# 0123456789abcdefABCDEF
# print(string.octdigits)					# 01234567

# print(string.punctuation)					# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~





'''
Understanding Classes and Objects

OOPs

class:
i.e:
player --> 	name :
			health :
			strategy :

'''

# print('class person:')
# class person:
# 	# print('Hello!')
# 	name = 'Maaynk'
# 	age = 23
#
#
# print('\np1:')
# p1 = person()
# print(p1.name)
# print(p1.age)
#
# # Chnaging name and age
# print('\nUpdated:')
# p1.name = 'Melech'
# p1.age = 88
# print(p1.name)
# print(p1.age)
#
# # In new object class gives default values
# print('\np2:')
# p2 = person()
# print(p2.name)
# print(p2.age)




# print('\nclass mathematics')
# class mathematics:
# 	name = 'Math Wizard'
# 	def greet( self ):
# 		print('Hello!')
# 		print(self.name)
#
# print('\nmath:')
# math = mathematics()
# math.greet()
# print(math.name)




# class mathematics:
# 	def greet( self ):
# 		print('Hello!')
# 		return 'Hi!'
# 	def factorial( self,n ):
# 		s = 1
# 		for i in range(1,n + 1):
# 			s *= i
# 		return s
# 	def lst_mul( self,lst ):
# 		s = 1
# 		for i in lst:
# 			s *= i
# 		return s
# 	def lst_dot( self,l1,l2 ):
# 		return [l1[i]*l2[i] for i in range(len(l1))]
#
#
# print('\nmath:')
# math = mathematics()
# # math.greet()
# print(math.greet())
#
# print('\nfactorial')
# mf = math.factorial(5)
# print(mf)
#
# print('\nlst_mul')
# lst = [1,2,3,4,5,6]
# print(math.lst_mul(lst))
#
# print('\nlst_dot')
# lst1 = [1,2,3,4,5]
# lst2 = [5,4,3,2,1]
# print(math.lst_dot(lst1,lst2))




'''
Dynamic Programming
'''
# # Quicksort 1:
# def part(myList,low,high):
# 	pivot = myList[high]
# 	i = low - 1
# 	for j in range(low,high):
# 		if myList[j] <= pivot:
# 			i = i + 1
# 			(myList[i],myList[j]) = (myList[j],myList[i])
# 	(myList[i + 1],myList[high]) = (myList[high],myList[i + 1])
# 	return i + 1
#
# def quickSort(myList,low,high):
# 	if low < high:
# 		pi = part(myList,low,high)
# 		quickSort(myList,low,pi - 1)
# 		quickSort(myList,pi + 1,high)
#
# list1 = [9,8,7,6,5,4,3,2,1]
# list1 = [i for i in range(200+1,0,-1)]
# print(list1)
# n = len(list1)
# quickSort(list1,0,n - 1)
# print('Sorted List:')
# print(list1)



# # Quicksort 2:
# def quicksort(mylist,low,high):
# 	if high - low > 1:
# 		p = partition(mylist,low,high)
# 		print(mylist)
# 		quicksort(mylist, low, p)
# 		quicksort(mylist,p + 1,high)
# def partition(mylist,low,high):
# 	pivot = mylist[low]
# 	i = low + 1
# 	j = high - 1
# 	while True:
# 		while ( i <= j and mylist[j] >= pivot):
# 			j = j - 1
# 		while ( i <= j and mylist[i] <= pivot):
# 			i = i + 1
# 		if i <= j:
# 			mylist[i],mylist[j] = mylist[j],mylist[i]
# 		else:
# 			mylist[low],mylist[j] = mylist[j],mylist[low]
# 			return j

