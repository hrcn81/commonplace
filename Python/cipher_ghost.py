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
#
#
# mylist = [8, 3, 1, 7, 0, 10, 2, 5]
# print("Original list:", mylist)
# quicksort(mylist, 0, len(mylist))
# print("Sorted list:", mylist)


'''
cgpa	package
6.89	3.26
5.12	1.98
7.82	3.25
7.42	3.67
6.94	3.57
'''

# def xdot(num):
# 	return print(round(8.402 - num,2))
#
# while True:
# 	n1 = eval( input( 'Enter Number:' ) )
# 	if n1 == 0:
# 		print('Exiting From Loop')
# 		break
# 	result = xdot( n1 )
# 	print(f"Result: {result}")



# def ydot(num):
# 	return round(3.146 - num,2)
#
# while True:
# 	n1 = eval(input('Enter Number:'))
# 	if n1 == 0:
# 		break
# 	result = ydot(n1)
# 	print('Result:',result)



# def nsquare(num):
# 	return round(num**2,2)
# while True:
# 	n1 = eval(input("Enter Number: "))
# 	if n1 == 0:
# 		break
# 	rslt = nsquare(n1)
# 	print(rslt)



# def multipication(n1,n2):
# 	return round(n1*n2,2)
# while True:
# 	n1 = eval( input( 'Enter Number_1: ' ) )
# 	n2 = eval( input( 'Enter Number_2: ' ) )
# 	if n1 == 0 and n2 == 0:
# 		break
# 	result = multipication(n1,n2)
# 	print('Result:',result)




# def predictor(x):
# 	return round(0.15*x + 1.8857,2)
# while True:
# 	x = eval(input('Enter Number: '))
# 	if x == 0:
# 		break
# 	result = predictor(x)
# 	print('Result: ',result)





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
#
#
# mylist = [20,15,13,18,12]
# print("Original list:", mylist)
# quicksort(mylist, 0, len(mylist))
# print("Sorted list:", mylist)




# def func(a = 1,b = 2,c = 3):
# 	return a*b*c
#
# result = func(5,c = 4)
# print(result)




# class person:
#
# 	def __init__( self,name,age ):
# 		print('__init__')
# 		# print(name)
# 		# print(age)
# 		self.name = name
# 		self.age = age
#
# 	def run( self ):
# 		print(self.name)
# 		print('run !!')
#
# # p1 = person()
# # p1.run()
# # print(p1.__init__())
#
# # p2 = person('Mayank',24)
#
# p3 = person('Melech',24)
# p3.run()





# class agent:
# 	def __init__( self,name,age):
# 		print('Welcome to the GAME')
# 		self.name = name
# 		self.age = age
# 		self.health = 100
# 		self.alive = True
#
# 	def curr_health( self ):
# 		if self.health >= 0.1:
# 			print(f"\nCurrent health of {self.name} is {self.health}.")
# 		else:
# 			print('Player is dead')
#
# 	def punched( self ):
# 		self.health -= 10
#
# 	def shooted( self ):
# 		self.health -= 50
#
# 	def is_live( self ):
# 		if self.health <= 0:
# 			self.alive = False
#
# 	def info( self ):
# 		print(f"Name	: 	{self.name}")
# 		print(f"Age		:  	{self.age}")
# 		print(f"Health	: 	{self.health}")
# 		print(f"Alive 	:	{self.alive}")
#
#
# a1 = agent('Mayank',24)
# # a2 = agent('James',30)
# # a3 = agent('Martin',28)
#
# a1.info()
# a1.curr_health()
# a1.punched()
# a1.curr_health()
# a1.shooted()
# a1.curr_health()
# a1.shooted()
# a1.curr_health()
# a1.is_live()
# a1.info()
#
# print('\n','-=-'*30,'\n')
#
#
# class boss(agent):
# 	def __init__( self,name,age ):
# 		super().__init__(name,age)
# 		self.health = 1000
# 	def blow_fire( self ):
# 		print('blow fire!')
#
# b1 = boss('Miral',25)
# b1.info()






# # Preorder

# class Node:
# 	def __init__( self,key ):
# 		self.left = None
# 		self.right = None
# 		self.val = key
# 	def preOrder( self ):			# NLR
# 		print(self.val,end = ' ')
# 		if self.left:
# 			self.left.preOrder()
# 		if self.right:
# 			self.right.preOrder()
# 	def postOrder( self ):			# LRN
# 		if self.left:
# 			self.left.postOrder()
# 		if self.right:
# 			self.right.postOrder()
# 		print(self.val,end = ' ')
# 	def inOrder( self ):			# LNR
# 		if self.left:
# 			self.left.inOrder()
# 		print(self.val,end = ' ')
# 		if self.right:
# 			self.right.inOrder()
#
#
# # post - LRN
# r1 = Node(50)
# r1.left = Node(51)
# r1.left.left = Node(44)
# r1.left.left.left = Node(40)
# r1.left.left.right = Node(41)
# r1.left.left.left.left = Node(36)
# r1.left.right = Node(30)
# r1.left.right.left = Node(34)
# r1.left.right.left.right = Node(42)
# r1.left.right.right = Node(31)
# r1.left.right.right.right = Node(51)
# r1.left.right.right.right.left = Node(33)
# r1.left.right.right.right.right = Node(1)
#
# r1.right = Node(2)
# r1.right.right = Node(3)
# r1.right.right.left = Node(8)
# r1.right.right.right = Node(5)
# r1.right.right.right.left = Node(7)
# r1.right.right.right.left.right = Node(12)
#
# r1.postOrder()




'''
Writing to a file

There are two ways to write in a file.

write() : Inserts the string str1 in a single line in the text file.
File_object.write(str1)
writelines() : For a list of string elements, each string is inserted in the text file.Used to insert multiple strings at a single time.
File_object.writelines(L) for L = [str1, str2, str3] 
Reading from a file

There are three ways to read data from a text file.

read() : Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.
File_object.read([n])
readline() : Reads a line of the file and returns in form of a string.For specified n, reads at most n bytes. However, does not reads more than one line, even if n exceeds the length of the line.
File_object.readline([n])
readlines() : Reads all the lines and return them as each line a string element in a list.
  File_object.readlines()
Note: ‘\n’ is treated as a special character of two bytes 
'''
# # Program to show various ways to read and
# # write data in a file.
# file1 = open( "myfile.txt", "w" )
# L = [ "This is Delhi \n", "This is Paris \n", "This is London \n" ]
#
# # \n is placed to indicate EOL (End of Line)
# file1.write( "Hello \n" )
# file1.writelines( L )
# file1.close()  # to change file access modes
#
# file1 = open( "myfile.txt", "r+" )
#
# print( "Output of Read function is " )
# print( file1.read() )
# print()
#
# # seek(n) takes the file handle to the nth
# # bite from the beginning.
# file1.seek( 0 )
#
# print( "Output of Readline function is " )
# print( file1.readline() )
# print()
#
# file1.seek( 0 )
#
# # To show difference between read and readline
# print( "Output of Read(9) function is " )
# print( file1.read( 9 ) )
# print()
#
# file1.seek( 0 )
#
# print( "Output of Readline(9) function is " )
# print( file1.readline( 9 ) )
#
# file1.seek( 0 )
# # readlines function
# print( "Output of Readlines function is " )
# print( file1.readlines() )
# print()
# file1.close()


# # Python program to illustrate
# # Append vs write mode
# file1 = open( "myfile.txt", "w" )
# L = [ "This is Delhi \n", "This is Paris \n", "This is London \n" ]
# file1.writelines( L )
# file1.close()
#
# # Append-adds at last
# file1 = open( "myfile.txt", "a" )  # append mode
# file1.write( "Today \n" )
# file1.close()
#
# file1 = open( "myfile.txt", "r" )
# print( "Output of Readlines after appending" )
# print( file1.readlines() )
# print()
# file1.close()
#
# # Write-Overwrites
# file1 = open( "myfile.txt", "w" )  # write mode
# file1.write( "Tomorrow \n" )
# file1.close()
#
# file1 = open( "myfile.txt", "r" )
# print( "Output of Readlines after writing" )
# print( file1.readlines() )
# print()
# file1.close()


'''
Inventory Management with Files

Inventory Management
Inventory management is the process of keeping track of inventory levels, orders, and sales in order to ensure that businesses have enough stock on hand to meet customer demand.

What is Inventory?
Inventory is a program or a database where we hold data of each and every product For eg: How much products we are having? What is the price of each product and how much products we have sold and What is the total sales?

Different Steps in the Inventory Management Project :
Step 1 : Creating a File name inventory.txt in write mode.

Step 2 : Adding the product details in the inventory.txt file ie : Id , Name , Price , Quantity and Category of the product as comma separated values.

Step 3 : Opening , Reading and Printing the content of the file .

Step 4 : Verifying if the user's desired product is actually in Inventory.

Step 5 : Generating a Bill of the products purchased by the user.

Step 6 : Updating the Inventory List .

Step 7: Adding More Functionalities i.e Prompting the user if demand of the user for an item is greater than the item in the inventory.

Step 8: Adding the details of the user and transaction the inventory in a new file sales.txt ie Name, Phone no, Quantity and Billing amount of the user.

Step 9: Observing the time of the Transaction.

Link of the Python Notebook : Click here
'''


