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



# # Binary Search Tree = BST
# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         self.root = self._insert(self.root, key)
#
#     def _insert(self, root, key):
#         if root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self._insert(root.left, key)
#         elif key > root.key:
#             root.right = self._insert(root.right, key)
#         return root
#
#     def delete(self, key):
#         self.root = self._delete(self.root, key)
#
#     def _delete(self, root, key):
#         if root is None:
#             return root
#         if key < root.key:
#             root.left = self._delete(root.left, key)
#         elif key > root.key:
#             root.right = self._delete(root.right, key)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             temp = self._min_value_node(root.right)
#             root.key = temp.key
#             root.right = self._delete(root.right, temp.key)
#         return root
#
#     def _min_value_node(self, node):
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current
#
#     def search(self, key):
#         return self._search(self.root, key)
#
#     def _search(self, root, key):
#         if root is None or root.key == key:
#             return root
#         if key < root.key:
#             return self._search(root.left, key)
#         return self._search(root.right, key)
#
#     def inorder_traversal(self):
#         self._inorder_traversal(self.root)
#
#     def _inorder_traversal(self, root):
#         if root:
#             self._inorder_traversal(root.left)
#             print(root.key, end=" ")
#             self._inorder_traversal(root.right)
#
#
# # Example usage:
# bst = BinarySearchTree()
# bst.insert(50)
# bst.insert(30)
# bst.insert(20)
# bst.insert(40)
# bst.insert(70)
# bst.insert(60)
# bst.insert(80)
#
# print("Inorder Traversal:")
# bst.inorder_traversal()
# print("\n")
#
# print("Search for 40:", bst.search(40))
# print("Search for 100:", bst.search(100))
#
# bst.delete(30)
# print("\nAfter deleting 30:")
# bst.inorder_traversal()


# from collections import deque
#
#
# class TreeNode:
# 	def __init__ ( self, key ):
# 		self.key = key
# 		self.left = None
# 		self.right = None
#
#
# class BinarySearchTree:
# 	def __init__ ( self ):
# 		self.root = None
#
# 	def insert ( self, key ):
# 		self.root = self._insert( self.root, key )
#
# 	def _insert ( self, root, key ):
# 		if root is None:
# 			return TreeNode( key )
# 		if key < root.key:
# 			root.left = self._insert( root.left, key )
# 		elif key > root.key:
# 			root.right = self._insert( root.right, key )
# 		return root
#
# 	def delete ( self, key ):
# 		self.root = self._delete( self.root, key )
#
# 	def _delete ( self, root, key ):
# 		if root is None:
# 			return root
# 		if key < root.key:
# 			root.left = self._delete( root.left, key )
# 		elif key > root.key:
# 			root.right = self._delete( root.right, key )
# 		else:
# 			if root.left is None:
# 				return root.right
# 			elif root.right is None:
# 				return root.left
# 			temp = self._min_value_node( root.right )
# 			root.key = temp.key
# 			root.right = self._delete( root.right, temp.key )
# 		return root
#
# 	def _min_value_node ( self, node ):
# 		current = node
# 		while current.left is not None:
# 			current = current.left
# 		return current
#
# 	def search ( self, key ):
# 		return self._search( self.root, key )
#
# 	def _search ( self, root, key ):
# 		if root is None or root.key == key:
# 			return root
# 		if key < root.key:
# 			return self._search( root.left, key )
# 		return self._search( root.right, key )
#
# 	def level_order_traversal ( self ):
# 		if self.root is None:
# 			return
#
# 		queue = deque()
# 		queue.append( self.root )
#
# 		while queue:
# 			level_size = len( queue )
# 			for _ in range( level_size ):
# 				node = queue.popleft()
# 				print( node.key, end = " " )
#
# 				if node.left:
# 					queue.append( node.left )
# 				if node.right:
# 					queue.append( node.right )
#
# 			print()
#
#
# # Example usage:
# bst = BinarySearchTree()
# bst.insert( 50 )
# bst.insert( 30 )
# bst.insert( 20 )
# bst.insert( 40 )
# bst.insert( 70 )
# bst.insert( 60 )
# bst.insert( 80 )
#
# print( "Level Order Traversal:" )
# bst.level_order_traversal()
#
# print( "\nAfter deleting 30:" )
# bst.delete( 30 )
# bst.level_order_traversal()




# def diff(s,x):
# 	if len(s) < len(x):
# 		return 'False'
# 	for i in range(len(s) - len(x) + 1):
# 		print(len(s),(len(x) + 1))
# 		if s[i:i + len(x)] == x:
# 			print(i,i+len(x))
# 			print(s[i:i + len(x)])
# 			print( x )
# 			return i
# 	return -1
#
# # Example usage:
# s = "GeeksForGeeks"
# x = "For"
# print(diff(s, x))





# # # Basic Network Theory:
# # Components:
# class basic_network_theory:
# 	def components( self ):
# 		print('Charge 	: q(t) Unit Columb')
# 		print('Current : I(t) = dq(t)/dt Unit Ampere')
# 		print('Voltage : V(t) = dw/dq Unit Voltage')
# 		print('Power 	: P(t) = I(t)*V(t) or dw(t)/dt Unit Watt')
#
# bnt = basic_network_theory()
# bnt.components()

# # Binary Search Tree = BST
# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         self.root = self._insert(self.root, key)
#
#     def _insert(self, root, key):
#         if root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self._insert(root.left, key)
#         elif key > root.key:
#             root.right = self._insert(root.right, key)
#         return root



# # BST :
# class Node:
# 	def __init__ ( self, value ):
# 		self.value = value
# 		self.left = None
# 		self.right = None
#
# class BinarySearchTree:
# 	def __init__ ( self ):
# 		self.root = None
# 	def insert ( self, value ):
# 		self.root = self.insert_after( self.root, value )
# 	def insert_after ( self, root, value ):
# 		if root is None:
# 			return Node( value )
# 		if value < root.value:
# 			root.left = self.insert_after( root.left, value )
# 		elif value > root.value:
# 			root.right = self.insert_after( root.right, value )
# 		return root
# 	def inorder ( self, node ):
# 		if node is not None:
# 			self.inorder( node.left )
# 			print( node.value )
# 			self.inorder( node.right )
#
# 	def preorder ( self, node ):
# 		if node is not None:
# 			print( node.value )
# 			self.preorder ( node.left )
# 			self.preorder ( node.right )
#
# 	def postorder ( self, node ):
# 		if node is not None:
# 			self.postorder ( node.left )
# 			self.postorder ( node.right )
# 			print( node.value )
#
# 	def print_tree ( self, traversal_type = 'preorder' ):
# 		if traversal_type == 'preorder':
# 			self.preorder ( self.root )
# 		if traversal_type == 'inorder':
# 			self.inorder ( self.root )
# 		if traversal_type == 'postorder':
# 			self.postorder ( self.root )
# 		else:
# 			print( "Invalid traversal type" )
#
# bst = BinarySearchTree()
# l1 = [7,3,5,8,9,2,10,1,11]
# for i in l1:
# 	bst.insert(i)
# print(bst.root.value)
# bst.print_tree()
#
# print("\nPreorder traversal:")
# bst.print_tree('preorder')
#
# print("\nInorder traversal:")
# bst.print_tree('inorder')
#
# print("\nPostorder traversal:")
# bst.print_tree('postorder')




# # # Singaly Linked List:
# class Node:
# 	def __init__( self,data ):
# 		self.data = data
# 		self.next = None
#
# class singlylinkelist:
# 	def __init__( self ):
# 		self.head = None
# 	def display( self ):
# 		temp = self.head
# 		if self.head is None:
# 			print('Empty')
# 		else:
# 			temp = self.head
# 			while temp:
# 				# temp = temp.next
# 				print( temp.data ,end = ' ')
# 				if temp.next :
# 					print('--->',end = ' ')
# 				else:
# 					print(' Ended !')
# 				temp = temp.next
# 	def insertatbegining( self,data ):
# 		nb = Node(data)
# 		nb.next = self.head
# 		self.head = nb
# 	def insertatend( self,data ):
# 		ne = Node(data)
# 		temp = self.head
# 		if temp is None:
# 			self.head = ne
# 		else:
# 			while temp.next:
# 				temp = temp.next
# 			temp.next = ne
# 	def insertatmid( self,data,pos ):
# 		if pos == 0:
# 			self.insertatbegining(data)
#
# 		else:
# 			nm = Node( data )
# 			temp = self.head
# 			for i in range( pos - 1 ):
# 				temp = temp.next
# 			nm.data = data
# 			nm.next = temp.next
# 			temp.next = nm
# 	def deleteatbegining( self ):
# 		temp = self.head
# 		self.head = temp.next
# 		temp.next = None
# 		print('\nRemoved from Begining :',temp.data)
# 	def deleteatend( self ):
# 		temp = self.head.next
# 		prev = self.head
# 		while temp.next is not None:
# 			temp = temp.next
# 			prev = prev.next
# 		prev.next = None
# 		print('\nRemoved from End :',temp.data)
# 	def deleteatmid( self,pos ):
# 		temp = self.head.next
# 		prev = self.head
# 		for i in range(1,pos - 1):
# 			temp = temp.next
# 			prev = prev.next
# 		prev.next = temp.next
# 		temp.next = None
# 		print('\nRemoved',temp.data, 'from Position',pos)
#
#
# l1 = singlylinkelist()
# n = Node(10)
# l1.head = n
# n1 = Node(20)
# l1.head.next = n1
# n2 = Node(30)
# n1.next = n2
# n3 = Node(40)
# n2.next = n3
# l1.insertatbegining(-10)
# l1.insertatbegining(-20)
# l1.insertatend(88)
# l1.insertatend(99)
# l1.insertatmid('mid1',2)
# l1.insertatmid('mid2',4)
# l1.insertatmid('mid3',5)
# l1.insertatmid('mid0',0)
# l1.display()
# l1.deleteatbegining()
# l1.display()
# l1.deleteatend()
# l1.display()
# l1.deleteatmid(2)
# l1.display()




'''
Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array. 
Equilibrium point in an array is an index (or position) such that the sum of all elements before 
that index is same as sum of elements after it.

Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

Example 1:
Input: 
n = 5 
A[] = {1,3,5,2,2} 
Output: 
3 
Explanation:  
equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2).

Example 2:
Input:
n = 1
A[] = {1}
Output: 
1
Explanation:
Since there's only element hence its only the equilibrium point.

Your Task:
The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium.
'''
# class ghost:
#     def equilibriumPoint(self, lst, num):
#         lst = list(lst)
#         print(lst)
#         addition = sum(lst)
#         left = 0
#         for i in range(num - 1):
#             addition -= lst[i]
#             if left == addition:
#                 return i + 1
#             left += lst[i]
#         return -1
#
# list1 = {1,3,5,2,2}
# g1 = ghost()
# print(g1.equilibriumPoint(list1,5))



# # enumerate()
# list1 = ["Data-Science", "Power BI", "Python"]
# for index, subject in enumerate(list1):
#     print(f"Index: {index + 1}, Subj: {subject}")

# l1 = ['Defender','Range Rover','Discovery','Land Rover']
# for i,j in enumerate(l1):
# 	print(f"Rank : {i + 1} , Model : { j }")




# print("Dictionary Iteration")
# d = dict()
#
# d['key1'] = "val1"
# d['key2'] = 345
# for i in d:
# 	print(i, d[i])



# def armstrong(val):
# 	num_str = str(val)
# 	len_str = len(num_str)
# 	check = sum(int(i) ** len_str for i in num_str)
# 	return check == val
#
# n = int(input('Enter number to check whether it\'s armdtrong or not : '))
#
# if armstrong(n):
#     print(f"{n} is an Armstrong number.")
# else:
#     print(f"{n} is not an Armstrong number.")




# from collections import deque
#
# # Creating a Deque
# people_line = deque(['Alice', 'Bob', 'Charlie'])
# print(people_line)
# # Joining and Leaving
# people_line.append('David')
# print(people_line)
# people_line.pop()
# print(people_line)



# Student_info = [21, 'Rose', "CSE", 30, 40, 50, 120]
# print("Student_roll :", Student_info[0], end=' , ')
# print("Student_name :", Student_info[1], end=', ')
# print("Student_totalMarks :", Student_info[-1], end=' ')



# Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
# Student_info[2] = "HSC"
# Student_info[1] = 'Mayank'
# print(Student_info)




# def count_word_occurrences(sentence):
#     word_list = sentence.split()
#     unique_words = []
#     word_counts = []
#
#     for i in word_list:
#         # Check if the word is already in the unique_words list
#         if i in unique_words:
#             index = unique_words.index(i)
#             word_counts[index] += 1
#         else:
#             # Add the word to the unique_words list and initialize its count to 1
#             unique_words.append(i)
#             word_counts.append(1)
#
#     return unique_words, word_counts
#
# # User input
# user_sentence = input("Enter a sentence: ")
#
# unique_words, word_counts = count_word_occurrences(user_sentence)
# print("Word occurrences in the sentence:")
# for i, count in zip(unique_words, word_counts):
#     print(f"{i}: {count}")




# List1 = [ [ 1, 2, 3, 5 ], [ 4, 6, 7, 9 ], [ 8, 10, 11, 13 ] ]
# # Accesing the rows of the list
# for i in List1:
# 	print( i, end = ' -- ' )
#
# # Accessing each element of a 2D-list
# print( "\n" )
# print(len(List1))
# for i in range( len( List1 ) ):
# 	for j in range( len( List1[ i ] ) ):
# 		print( List1[ i ][ j ], end = " , " )
# 		print(i,j)



# multidimensional_dict = {
#         'first_level': {
#              'second_level_1': {
#                      'third_level_1': 1,
#                      'third_level_2': 2
#                },
#         'second_level_2': {
#                     'third_level_3': 3,
#                     'third_level_4': 4
#                    }
#               },
#  'another_first_level': {
#                 'second_level_3': {
#                              'third_level_5': 5,
#                              'third_level_6': 6
#                              },
#               'second_level_4': {
#                             'third_level_7': 7,
#                             'third_level_8': 8
#                     }
#              }
#         }
# print(multidimensional_dict)




# def two_sum_tuples(nums, target):
#     num_indices = {}  # Dictionary to store indices of elements
#
#     for i, num in enumerate(nums):
#         complement = target - num
#
#         # Check if the complement is already in the dictionary
#         if complement in num_indices:
#             return (complement, num)
#
#         # Add the current element to the dictionary
#         num_indices[num] = i
#
#     return None
#
# nums = [2, 7, 11, 15]
# target = 9
# result = two_sum_tuples(nums, target)
# print("Tuple of Elements:", result)






# class Solution:
#     # Function to reverse every sub-array group of size k.
#     def reverseInGroups(self, arr, N, K):
#         arr_list = list(arr)  # Convert set to a list
#         for i in range(0, N, K):
#             left = i
#             right = min(i + K - 1, N - 1)
#             while left < right:
#                 arr_list[left], arr_list[right] = arr_list[right], arr_list[left]
#                 left += 1
#                 right -= 1
#         return arr_list
#
#
#
#
# N = 5
# K = 3
# arr = {1,2,3,4,5}
# s1 = Solution()
# print(s1.reverseInGroups(arr,N,K))




# record = {1001: {'Name': "5 Star"         , "Price" : 10 , "Qn" : 200},
#           1002: {'Name': "Bar-One"        , "Price" : 20 , "Qn" : 100 },
#           1003: {'Name': "Candy"          , "Price" : 2  , "Qn" : 1000},
#           1004: {'Name': "Chocolate Cake" , "Price" : 550, "Qn" : 8 },
#           1005: {'Name': "Blueberry Cake" , "Price" : 650, "Qn" : 5 }}
#
# # print(record[1001]['Name'], record[1001]['Qn'])
# # print(record[1001],record[1005])
# # print(record)
#
# # for i in record:
# # 	print(i)
#
# print('-'*25,'Menu','-'*25)
# for i in record:
# 	print(i,':',record[i]['Name'],'|',record[i]['Price'],'|',record[i]['Qn'])
# print('-'*56)
#
# ui_pr = int(input('Enter Product ID : '))
# ui_qn = int(input('Enter Quentity : '))
#
# print('-'*25,'Bill','-'*25)
#
# print('Name 			:',record[ui_pr]['Name'])
# print('Price (Rs.) 	:',record[ui_pr]['Price'])
# print('Quentity 		:',ui_qn)
# print('-'*56)
#
# print('Price (Rs.) 	:',ui_qn * record[ui_pr]["Price"],"(Rs.)")
#
# print('-'*56)




'''
Updating
'''
# import json
#
# record = {1001: {'Name': "5 Star"         , "Price" : 10 , "Qn" : 200},
#           1002: {'Name': "Bar-One"        , "Price" : 20 , "Qn" : 100 },
#           1003: {'Name': "Candy"          , "Price" : 2  , "Qn" : 1000},
#           1004: {'Name': "Chocolate Cake" , "Price" : 550, "Qn" : 8 },
#           1005: {'Name': "Blueberry Cake" , "Price" : 650, "Qn" : 5 }}
#
# print('-'*25,'Menu','-'*25)
# for i in record:
# 	print(i,':',record[i]['Name'],'|',record[i]['Price'],'|',record[i]['Qn'])
# print('-'*56)
#
# ui_pr = int(input('Enter Product ID : '))
# ui_qn = int(input('Enter Quentity : '))
#
# print('-'*25,'Bill','-'*25)
#
# print('Name 			:',record[ui_pr]['Name'])
# print('Price (Rs.) 	:',record[ui_pr]['Price'])
# print('Quentity 		:',ui_qn)
# print('-'*56)
#
# print('Price (Rs.) 	:',ui_qn * record[ui_pr]["Price"],"(Rs.)")
#
# print('-'*56)
# json.dumps(record)





# import nltk
# # nltk.download( 'stopwords' )
# from nltk.corpus import stopwords
# # To check all the English stop words
# print( stopwords.words( 'english' ) )
# print('-'*30)
# x = 0
# for i in stopwords.words( 'english' ):
# 	x += 1
# print(x)
# print('-'*30)
# print(sum(1 for i in stopwords.words('english')))
# print('-'*30)
#
#
# from nltk.tokenize import word_tokenize,sent_tokenize
# txt="This is not a good time to talk."
# txt=word_tokenize(txt)
# for i in txt:
#     print(i)
# print('-'*30)
# stopwords=stopwords.words('english')
# for word in txt:
#     if((word.lower() not in stopwords) and (len(word)>=2)):
#         print(word)
# print('-'*30)
#
# crps = ('In its reply, the government said that a 100% door-to-door enumeration of castes and '
# 		'communities in the State was carried out in 1983, following the directions issued by '
# 		'the Supreme Court on October 14, 1982, and that data was being used till now for '
# 		'providing reservation to the backward classes, most backward classes and denotified communities.')
# crps = sent_tokenize(crps)
# stopwords=stopwords.words('english')
# for i in crps:
# 	if ((i.lower() not in stopwords) & (len(i) > 2)):
# 		print(i)


# crps_sentences = sent_tokenize(crps)
# for sentence in crps_sentences:
#     words = word_tokenize(sentence)
#     for word in words:
#         if word.lower() not in stopwords and len(word) > 2:
#             print(word)

# crps = sent_tokenize(crps)
# x = 0
# y = 0
# for ii in crps:
# 	words = word_tokenize(ii)
# 	for i in words:
# 		if i.lower() not in stopwords and len(i) > 2:
# 			x += 1
# 		y += 1
# print(x,y)
# print(100 - (27/63) * 100)





'''
Updating
'''
# import json
#
# record = {1001: {'Name': "5 Star         ", "Price" : 10 , "Qn" : 200},
#           1002: {'Name': "Bar-One        ", "Price" : 20 , "Qn" : 100 },
#           1003: {'Name': "Candy          ", "Price" : 2  , "Qn" : 1000},
#           1004: {'Name': "Chocolate Cake " ,"Price" : 550, "Qn" : 8 },
#           1005: {'Name': "Blueberry Cake " ,"Price" : 650, "Qn" : 5 }}
#
# print('-'*25,'Menu','-'*25)
# for i in record:
# 	print(i,':',record[i]['Name'],'|',record[i]['Price'],'|',record[i]['Qn'])
# print('-'*56)
#
# ui_pr = int(input('Enter Product ID : '))
# ui_qn = int(input('Enter Quentity : '))
#
# print('-'*25,'Bill','-'*25)
#
# print('Name 			:',record[ui_pr]['Name'])
# print('Price (Rs.) 	:',record[ui_pr]['Price'])
# print('Quentity 		:',ui_qn)
# print('-'*56)
#
# print('Price (Rs.) 	:',ui_qn * record[ui_pr]["Price"],"(Rs.)")
#
# print('-'*56)
# json.dumps(record)
#
# print('-'*25,'Bill','-'*25)
#
# print('Name 			:',record[ui_pr]['Name'])
# print('Price (Rs.) 	:',record[ui_pr]['Price'])
# print('Quentity 		:',ui_qn)
# print('-'*56)

# print("--------------------MENU---------------------")
# for key in record.keys():
#     print(key, record[key]['Name'], record[key]['Price'], record[key]['Name'],record[key]['Qn'])
# print("---------------------------------------------")
# print('')
#
# ui_pr = int(input("Enter product ID : "))
# ui_qn = int(input("Enter Quantity   : "))
#
# # print("---------------------------------------------")
# # print('')
# #
# # print("Name      : ", record[ui_pr]["Name"])
# # print("Price (Rs): ", record[ui_pr]["Price"])
# # print("Quantity  : ", ui_qn)
# # print("---------------------------------------------")
# # print("Billing   : ", ui_qn * record[ui_pr]["Price"], "Rs")
# # print("---------------------------------------------")
#
# if record[ui_pr]['Qn'] < ui_qn:
# 	print('Insufficien Quentity')
# 	print(f"There're only {record[ui_pr]['Qn']} Quantity left")
# else:
# 	print( "---------------------------------------------" )
# 	print( '				  Bill				' )
# 	print( "Name      			: ", record[ ui_pr ][ "Name" ] )
# 	print( "Price (Rs)			: ", record[ ui_pr ][ "Price" ] )
# 	print( "Quantity  			: ", ui_qn )
# 	print( "---------------------------------------------" )
# 	print( "Billing   			: ", ui_qn * record[ ui_pr ][ "Price" ], "Rs" )
# 	print( "---------------------------------------------" )
# 	record[ui_pr]['Qn'] = record[ui_pr]['Qn'] - ui_qn
# 	print( '' )
# 	print( "---------------------------------------------" )
# 	print( "  Thanks for your order, Inventory Updated!  " )
# 	print( "---------------------------------------------" )
#
# 	print( "\n--------------------MENU---------------------" )
# 	for key in record.keys():
# 		print( key, record[ key ][ 'Name' ], record[ key ][ 'Price' ], record[ key ][ 'Name' ], record[ key ][ 'Qn' ] )
# 	print( "---------------------------------------------" )





# class conducting_materials:
# 	def types_of_conducting_materials( self ):
# 		print("There're 3 types of materials.")
# 		print("\t1.Conducting"
# 			  "\n\t2.Magnetic"
# 			  "\n\t3.Insulating")
# 	def conducting_materials( self ):
# 		print("\nThere're 2 types of conducting materials.")
# 		print("1.Highly conducting materials"
# 			  "\n\tCu,Al,Ag,Au ----> Used in windings"
# 			  "\n\tCu 	   -> in Windings"
# 			  "\n\tAl 	   -> in tanks"
# 			  "\n\tCarbon -> in brush")
# 		print("2.Highly resistive materials"
# 			  "\n\t-> Alloys (mixing of multiple materials)"
# 			  "\n\t-> Used in heating elements"
# 			  "\n\t-> Low temp. resistive coefficient")
# 	def properties_of_highly_conducting_materials( self ):
# 		print("\nProperties of Highly Conducting materials:"
# 			  "\n\t-> Highest possible conductivity"
# 			  "\n\t-> Adequate mechanical strength and absense of brittleness"
# 			  "\n\t-> Corrosion resistance"
# 			  "\n\t-> Low temp. resistive coefficient"
# 			  "\n\t-> Valding and soldering resisrance should be less"
# 			  "\n\t-> Rollability and drawability")
#
# cm = conducting_materials()
# cm.types_of_conducting_materials()
# cm.conducting_materials()
# cm.properties_of_highly_conducting_materials()




'''
Single Linked List
'''
'''
Displaying
'''
# class node:
# 	def __init__( self,data ):
# 		self.data = data
# 		self.next = None
#
# class singlelinkedlist:
# 	def __init__( self ):
# 		self.head = None
# 	def display( self ):
# 		if self.head is None:
# 			print('List is empty')
# 		else:
# 			temp = self.head
# 			while temp:
# 				print(temp.data,end = ' ')
# 				if temp.next:
# 					print('--->',end=' ')
# 				temp = temp.next
#
# sll = singlelinkedlist()
# n1 = node(10)
# sll.head = n1
# n2 = node(20)
# n1.next = n2
# n3 = node(30)
# n2.next = n3
# sll.display()




# Home Work

# def remove_html_tags(reviews):
#     return re.sub(r'<[^<]+?>','',reviews)
#
# def remove_url(text):
#     return re.sub(r'http[s]?://\S+|www.\S+','',text)
#
# exclude = string.punctuation
#
# def remove_punctuation(text):
#     for char in exclude:
#         text = text.replace(char,'')
#     return text
#
# def remove_punctuation(text):
#     return text.translate(str.maketrans('','',string.punctuation))
#
# def spelling_correlation(text):
#     return TextBlob(text).correct()
#
# def remove_stopwords(text):
#     return [i for i in text.split() if i not in stop_words]
#
# def remove_emoji(text):
#     emoji_pattern = re.compile("["
#                                u"\U0001F600-\U0001F64F"
#                                # emoticons
#                                u"\U0001F300-\U0001F5FF"
#                                # symbols & pictographs
#                                u"\U0001F680-\U0001F6FF"
#                                # transport & map symbols
#                                u"\U0001F1E0-\U0001F1FF"
#                                # flags (105)
#                                u"\U00002702-\U00002780"
#                                u"\U000024C2-\U0001F251"
#                                "]+", flags=re.UNICODE)
#     return emoji_pattern.sub(r'', text)
# ps = PorterStemmer()
# def stem_words(text):
#     return " ".join([ps.stem(word) for word in word_tokenize(text)])
# sample = 'walk walking walked'





# for i in range(0,2):
# 	for j in range(0,6):
# 		print('*',end = ' ')
# 	print()


# x = 0
# for i in range(5):
# 	for j in range(5):
# 		x += 1
# 		print(x,end = ' ')
# 	print()



# for i in range(5):
# 	for j in range(5):
# 		print(i,end = ' ')
# 	print()



# for i in range(5):
# 	for j in range(5):
# 		print(j,end = ' ')
# 	print()



# for i in range(5,0,-1):
# 	for j in range(4,0,-1):
# 		print(i,end = ' ')
# 	print()



# for i in range(5,0,-1):
# 	for j in range(5,0,-1):
# 		print(j,end= ' ')
# 	print()



# x = int(input('Enter Rows Number   : '))
# y = int(input('Enter Column Number : '))
# for i in range(x):
# 	for j in range(y):
# 		print('*',end = ' ')
# 	print()



# for i in range(1,6):
# 	for j in range(1,4):
# 		print(i,end= ' ')
# 	print()



# for i in range(1,6):
# 	for j in range(1,4):
# 		print(j,end= ' ')
# 	print()



# x = 1
# for i in range(6):
# 	for j in range(6):
# 		print(x,end = ' ')
# 		x += 1
# 	print()



# for i in range(5):
# 	for j in range(3):
# 		print(j+1,i+1,end = ' ')
# 	print()




# ## Fibonacci Series
# a = 0
# b = 1
# n = int(input('Enter Number : '))
# print(a,b,end = ' ')
# for i in range(n-2):
# 	c = a + b
# 	a = b
# 	b = c
# 	print(c,end = ' ')



# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# chart_data = pd.DataFrame(np.random.randn(20,3),columns = ['Line_1','Line_2','Line_3'])
#
# st.header('1 Charts with random numbers')
# st.subheader('1.1 Line Chart')
# st.line_chart(chart_data)
#
# st.subheader('1.2 Area Chart')
# st.area_chart(chart_data)
#
# st.subheader('1.3 Bar Chart')
# st.bar_chart(chart_data)
#
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# st.header('2 Data Visualization with Matplotlib and Seaborn')
# st.subheader('2.1 Loading Dataframe')
# df = pd.read_csv(r"D:\DataScience\Iant\python\streamlit\iris.csv")
# st.dataframe(df)
#
# st.subheader('2.2 Bar graph with  matplotlib')
# fig = plt.figure(figsize=(15,8))
# df['species'].value_counts().plot(kind= 'bar')
# st.pyplot(fig)
#
# st.subheader('2.3 Distribution plot with seaborn')
# fig = plt.figure(figsize= (15,8))
# sns.distplot(df['sepal_length'])
# st.pyplot(fig)
#
# st.header('Multiple Graph')
# col1,col2 = st.columns(2)
# with col1:
#     col1.header = 'KDE = False'
#     # col1.write('KDE = False')
#     fig1 = plt.figure(figsize=(5,5))
#     sns.distplot(df['sepal_length'],kde = False)
#     st.pyplot(fig1)
# with col2:
#     col2.header = 'Hist = False'
#     # col2.write('Hist = False')
#     fig1 = plt.figure(figsize=(5,5))
#     sns.distplot(df['sepal_length'],hist = False)
#     st.pyplot(fig1)


# N1 = int(input('Enter Number:'))
# for i in range(1,N1+1):
# 	for j in range(1,N1+1):
# 		if j == 1 or i == N1 or j == N1:
# 			print('*',end = ' ')
# 		else :
# 			print(' ',end = ' ')
# 	print()



# N = 5
# for i in range( 1, N + 1 ):
# 	for j in range( N+1, i, -1 ):
# 		print( '*', end = ' ' )
# 	print()



# n,count = 5,0
# for _ in range(n):
# 	n -= 1
# 	count += 1
# print(count)


# def swap(a,b):
# 	return b,a
#
# a = int(input('Enter Number a: '))
# b = int(input('Enter Number b: '))
# a,b = swap(a,b)
# print(a - b)



# x = 0
# if False or [False] or (False):
# 	x += 1
# print(x)



# s = 'abc'
# for _ in range(10):
# 	s = tuple(s)
# print(s)
# print(len(s))



# t = [1, 2, 3, 4]
# x = t.pop() > t.pop() > t.pop()
# print(x)
# print(t)
# t.append(x)
# print(t)
# print(len(t))


# x = [1,2,3,20,1]
# print(x)
# m = x.pop() < x.pop() > x.pop()
# print(m)
# print(x)



# t = [1, 2, 3, 4,2]
# print(t)
# x = (t.pop() < t.pop()), t.pop()
# print(t)
# print(x)
# print(type(x))
# t.extend(x)
# print(t)
# print(len(t))



# t = [0, 1, 2]
# print(t)
# a = [10,20,30]
# t.extend([])
# print('extend',t)	# extend [0, 1, 2]
# t.append([])
# print('append',t)	# append [0, 1, 2, []]
# print(len(t))




# t = [0, 1, [2], 3]
# print(t)
# y = t[2]
# print(y)	# [2]
# y.append(20)
# print(y)	# [2, 20]
# print(t)	# [0, 1, [2, 20], 3]
# print(t[2])	# [2, 20]



# class1 = {"c1":"Mayank","c2":"Miral"}
#
# # print(type(class1))
# print(class1.keys())		# dict_keys(['c1', 'c2'])
# print(class1.values())		# dict_values(['Mayank', 'Miral'])
# print(class1.items())		# dict_items([('c1', 'Mayank'), ('c2', 'Miral')])
# # print(class1['c3'])			# KeyError
# print(class1.remove('c1'))



# import random
# import time
# Player1_HP = 100
# Player2_HP = 100
# turn = 1
#
# while (Player1_HP > 0 and Player2_HP > 0):
#     print("\n-----Turn Start-----")
#     print('Player 1 HP:',Player1_HP)
#     print('Player 2 HP:',Player2_HP)
#
#     if turn == 1:
#         # player1 turn
#         print('Player1 turn')
#         input('Press Enter to attack')
#         damage = random.randint(50,100) # Random 10 20 can be the attack damage
#         print('Generating attack.....💥')
#         time.sleep(2)
#         # Player2_HP = Player2_HP - damage
#         Player2_HP -= damage
#         print('Player 1 has attacked Player 2 for',damage,'damage ! ⚔️')
#
#         turn = 2
#
#     else:
#         # player2 turn
#         print('Player2 turn')
#         input('Press Enter to attack')
#         damage = random.randint(10,20) # Random 10 20 can be the attack damage
#         print('Generating attack.....💥')
#         time.sleep(2)
#         # Player2_HP = Player2_HP - damage
#         Player1_HP -= damage
#         print('Player 2 has attacked Player 1 for',damage,'damage ! ⚔️')
#
#         turn = 1
#
# print()
# if Player1_HP > 0:
#     print('Player 1 is winner 🏆')
# else:
#     print('Player 2 is winner 🏆')



# num = int(input('Enter Number:'))
# if num % 3 == 0 and num % 5 == 0:
# 	print('FizzBuzz')
# if num % 3 == 0 and num % 5 != 0:
# 	print('Fizz')
# if num % 5 == 0 and num % 3 != 0:
# 	print('Buzz')
# if num % 3 != 0 and num % 5 != 0:
# 	print(num)



# even_numbers_1 = [x for x in range(2,21) if x % 2 == 0]
# print(even_numbers_1)	# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# even_numbers_2 = list(range(2,21,2))
# print(even_numbers_2)	# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# even_numbers_3 = []
# for i in range(2,21):
# 	if i % 2 == 0:
# 		even_numbers_3.append(i)	# In snippet there's no mention of print statement
# print(even_numbers_3)	# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# even_numbers_4 = [2*i for i in range(1,11)]
# print(even_numbers_4)	# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



# age_1 = int(input('Enter your age : '))
# print(age_1)
# print(type(age_1))
#
# age_2 = input('Enter your age : ')
# age_2o1 = int(age_2)
# print(age_2o1)
# print(type(age_2o1))



# x = float(input('Enter number with decimal : '))
# print(x)
# print(type(x))
# x1 = int(x)
# print(x1)
# print(type(x1))



# x = 10
# x1 = str(x)
# print(x)
# print(type(x))
# print(x1)
# print(type(x1))




# # Option 1	Dissenting
# print('Option 1')
# month = int(input('Enter month number : '))
# if 3 <= month <= 5:
# 	print('Spring')
# if 6 <= month <= 8:
# 	print('Summer')
# if 9 <= month <= 11:
# 	print('Autumn')
# else:
# 	print('Winter')



# # option 2	Affirmative
# print('\nOption 2')
# month = int(input('Enter month number : '))
# if 3 <= month <= 5:
# 	print('Spring')
# if 6 <= month <= 8:
# 	print('Summer')
# if 9 <= month <= 11:
# 	print('Autumn')
# if month in [1,2,12]:
# 	print('Winter')



# # Option 3	Dissenting
# print('\nOption 3')
# month = int(input('Enter month number : '))
# season = 'Winter' if month in [12,1,2] else 'Spring' if 3 <= month <= 5 else 'Summer' if 6 <= month <= 8 else 'Autumn'
# print(season)



# # Option 4		Dissenting
# print('\nOption 4')
# month = int(input('Enter number of month : '))
# season = ['Winter','Winter','Spring','Spring','Spring','Summer','Summer','Summer','Summer','Autumn','Autumn','Autumn','Winter'][month - 1]
# print(season)



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



# # Binary Search Tree = BST
# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         self.root = self._insert(self.root, key)
#
#     def _insert(self, root, key):
#         if root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self._insert(root.left, key)
#         elif key > root.key:
#             root.right = self._insert(root.right, key)
#         return root
#
#     def delete(self, key):
#         self.root = self._delete(self.root, key)
#
#     def _delete(self, root, key):
#         if root is None:
#             return root
#         if key < root.key:
#             root.left = self._delete(root.left, key)
#         elif key > root.key:
#             root.right = self._delete(root.right, key)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             temp = self._min_value_node(root.right)
#             root.key = temp.key
#             root.right = self._delete(root.right, temp.key)
#         return root
#
#     def _min_value_node(self, node):
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current
#
#     def search(self, key):
#         return self._search(self.root, key)
#
#     def _search(self, root, key):
#         if root is None or root.key == key:
#             return root
#         if key < root.key:
#             return self._search(root.left, key)
#         return self._search(root.right, key)
#
#     def inorder_traversal(self):
#         self._inorder_traversal(self.root)
#
#     def _inorder_traversal(self, root):
#         if root:
#             self._inorder_traversal(root.left)
#             print(root.key, end=" ")
#             self._inorder_traversal(root.right)
#
#
# # Example usage:
# bst = BinarySearchTree()
# bst.insert(50)
# bst.insert(30)
# bst.insert(20)
# bst.insert(40)
# bst.insert(70)
# bst.insert(60)
# bst.insert(80)
#
# print("Inorder Traversal:")
# bst.inorder_traversal()
# print("\n")
#
# print("Search for 40:", bst.search(40))
# print("Search for 100:", bst.search(100))
#
# bst.delete(30)
# print("\nAfter deleting 30:")
# bst.inorder_traversal()


# from collections import deque
#
#
# class TreeNode:
# 	def __init__ ( self, key ):
# 		self.key = key
# 		self.left = None
# 		self.right = None
#
#
# class BinarySearchTree:
# 	def __init__ ( self ):
# 		self.root = None
#
# 	def insert ( self, key ):
# 		self.root = self._insert( self.root, key )
#
# 	def _insert ( self, root, key ):
# 		if root is None:
# 			return TreeNode( key )
# 		if key < root.key:
# 			root.left = self._insert( root.left, key )
# 		elif key > root.key:
# 			root.right = self._insert( root.right, key )
# 		return root
#
# 	def delete ( self, key ):
# 		self.root = self._delete( self.root, key )
#
# 	def _delete ( self, root, key ):
# 		if root is None:
# 			return root
# 		if key < root.key:
# 			root.left = self._delete( root.left, key )
# 		elif key > root.key:
# 			root.right = self._delete( root.right, key )
# 		else:
# 			if root.left is None:
# 				return root.right
# 			elif root.right is None:
# 				return root.left
# 			temp = self._min_value_node( root.right )
# 			root.key = temp.key
# 			root.right = self._delete( root.right, temp.key )
# 		return root
#
# 	def _min_value_node ( self, node ):
# 		current = node
# 		while current.left is not None:
# 			current = current.left
# 		return current
#
# 	def search ( self, key ):
# 		return self._search( self.root, key )
#
# 	def _search ( self, root, key ):
# 		if root is None or root.key == key:
# 			return root
# 		if key < root.key:
# 			return self._search( root.left, key )
# 		return self._search( root.right, key )
#
# 	def level_order_traversal ( self ):
# 		if self.root is None:
# 			return
#
# 		queue = deque()
# 		queue.append( self.root )
#
# 		while queue:
# 			level_size = len( queue )
# 			for _ in range( level_size ):
# 				node = queue.popleft()
# 				print( node.key, end = " " )
#
# 				if node.left:
# 					queue.append( node.left )
# 				if node.right:
# 					queue.append( node.right )
#
# 			print()
#
#
# # Example usage:
# bst = BinarySearchTree()
# bst.insert( 50 )
# bst.insert( 30 )
# bst.insert( 20 )
# bst.insert( 40 )
# bst.insert( 70 )
# bst.insert( 60 )
# bst.insert( 80 )
#
# print( "Level Order Traversal:" )
# bst.level_order_traversal()
#
# print( "\nAfter deleting 30:" )
# bst.delete( 30 )
# bst.level_order_traversal()




# def diff(s,x):
# 	if len(s) < len(x):
# 		return 'False'
# 	for i in range(len(s) - len(x) + 1):
# 		print(len(s),(len(x) + 1))
# 		if s[i:i + len(x)] == x:
# 			print(i,i+len(x))
# 			print(s[i:i + len(x)])
# 			print( x )
# 			return i
# 	return -1
#
# # Example usage:
# s = "GeeksForGeeks"
# x = "For"
# print(diff(s, x))





# # # Basic Network Theory:
# # Components:
# class basic_network_theory:
# 	def components( self ):
# 		print('Charge 	: q(t) Unit Columb')
# 		print('Current : I(t) = dq(t)/dt Unit Ampere')
# 		print('Voltage : V(t) = dw/dq Unit Voltage')
# 		print('Power 	: P(t) = I(t)*V(t) or dw(t)/dt Unit Watt')
#
# bnt = basic_network_theory()
# bnt.components()

# # Binary Search Tree = BST
# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         self.root = self._insert(self.root, key)
#
#     def _insert(self, root, key):
#         if root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self._insert(root.left, key)
#         elif key > root.key:
#             root.right = self._insert(root.right, key)
#         return root



# # BST :
# class Node:
# 	def __init__ ( self, value ):
# 		self.value = value
# 		self.left = None
# 		self.right = None
#
# class BinarySearchTree:
# 	def __init__ ( self ):
# 		self.root = None
# 	def insert ( self, value ):
# 		self.root = self.insert_after( self.root, value )
# 	def insert_after ( self, root, value ):
# 		if root is None:
# 			return Node( value )
# 		if value < root.value:
# 			root.left = self.insert_after( root.left, value )
# 		elif value > root.value:
# 			root.right = self.insert_after( root.right, value )
# 		return root
# 	def inorder ( self, node ):
# 		if node is not None:
# 			self.inorder( node.left )
# 			print( node.value )
# 			self.inorder( node.right )
#
# 	def preorder ( self, node ):
# 		if node is not None:
# 			print( node.value )
# 			self.preorder ( node.left )
# 			self.preorder ( node.right )
#
# 	def postorder ( self, node ):
# 		if node is not None:
# 			self.postorder ( node.left )
# 			self.postorder ( node.right )
# 			print( node.value )
#
# 	def print_tree ( self, traversal_type = 'preorder' ):
# 		if traversal_type == 'preorder':
# 			self.preorder ( self.root )
# 		if traversal_type == 'inorder':
# 			self.inorder ( self.root )
# 		if traversal_type == 'postorder':
# 			self.postorder ( self.root )
# 		else:
# 			print( "Invalid traversal type" )
#
# bst = BinarySearchTree()
# l1 = [7,3,5,8,9,2,10,1,11]
# for i in l1:
# 	bst.insert(i)
# print(bst.root.value)
# bst.print_tree()
#
# print("\nPreorder traversal:")
# bst.print_tree('preorder')
#
# print("\nInorder traversal:")
# bst.print_tree('inorder')
#
# print("\nPostorder traversal:")
# bst.print_tree('postorder')




# # # Singaly Linked List:
# class Node:
# 	def __init__( self,data ):
# 		self.data = data
# 		self.next = None
#
# class singlylinkelist:
# 	def __init__( self ):
# 		self.head = None
# 	def display( self ):
# 		temp = self.head
# 		if self.head is None:
# 			print('Empty')
# 		else:
# 			temp = self.head
# 			while temp:
# 				# temp = temp.next
# 				print( temp.data ,end = ' ')
# 				if temp.next :
# 					print('--->',end = ' ')
# 				else:
# 					print(' Ended !')
# 				temp = temp.next
# 	def insertatbegining( self,data ):
# 		nb = Node(data)
# 		nb.next = self.head
# 		self.head = nb
# 	def insertatend( self,data ):
# 		ne = Node(data)
# 		temp = self.head
# 		if temp is None:
# 			self.head = ne
# 		else:
# 			while temp.next:
# 				temp = temp.next
# 			temp.next = ne
# 	def insertatmid( self,data,pos ):
# 		if pos == 0:
# 			self.insertatbegining(data)
#
# 		else:
# 			nm = Node( data )
# 			temp = self.head
# 			for i in range( pos - 1 ):
# 				temp = temp.next
# 			nm.data = data
# 			nm.next = temp.next
# 			temp.next = nm
# 	def deleteatbegining( self ):
# 		temp = self.head
# 		self.head = temp.next
# 		temp.next = None
# 		print('\nRemoved from Begining :',temp.data)
# 	def deleteatend( self ):
# 		temp = self.head.next
# 		prev = self.head
# 		while temp.next is not None:
# 			temp = temp.next
# 			prev = prev.next
# 		prev.next = None
# 		print('\nRemoved from End :',temp.data)
# 	def deleteatmid( self,pos ):
# 		temp = self.head.next
# 		prev = self.head
# 		for i in range(1,pos - 1):
# 			temp = temp.next
# 			prev = prev.next
# 		prev.next = temp.next
# 		temp.next = None
# 		print('\nRemoved',temp.data, 'from Position',pos)
#
#
# l1 = singlylinkelist()
# n = Node(10)
# l1.head = n
# n1 = Node(20)
# l1.head.next = n1
# n2 = Node(30)
# n1.next = n2
# n3 = Node(40)
# n2.next = n3
# l1.insertatbegining(-10)
# l1.insertatbegining(-20)
# l1.insertatend(88)
# l1.insertatend(99)
# l1.insertatmid('mid1',2)
# l1.insertatmid('mid2',4)
# l1.insertatmid('mid3',5)
# l1.insertatmid('mid0',0)
# l1.display()
# l1.deleteatbegining()
# l1.display()
# l1.deleteatend()
# l1.display()
# l1.deleteatmid(2)
# l1.display()




'''
Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array. 
Equilibrium point in an array is an index (or position) such that the sum of all elements before 
that index is same as sum of elements after it.

Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

Example 1:
Input: 
n = 5 
A[] = {1,3,5,2,2} 
Output: 
3 
Explanation:  
equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2).

Example 2:
Input:
n = 1
A[] = {1}
Output: 
1
Explanation:
Since there's only element hence its only the equilibrium point.

Your Task:
The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium.
'''
# class ghost:
#     def equilibriumPoint(self, lst, num):
#         lst = list(lst)
#         print(lst)
#         addition = sum(lst)
#         left = 0
#         for i in range(num - 1):
#             addition -= lst[i]
#             if left == addition:
#                 return i + 1
#             left += lst[i]
#         return -1
#
# list1 = {1,3,5,2,2}
# g1 = ghost()
# print(g1.equilibriumPoint(list1,5))



# # enumerate()
# list1 = ["Data-Science", "Power BI", "Python"]
# for index, subject in enumerate(list1):
#     print(f"Index: {index + 1}, Subj: {subject}")

# l1 = ['Defender','Range Rover','Discovery','Land Rover']
# for i,j in enumerate(l1):
# 	print(f"Rank : {i + 1} , Model : { j }")




# print("Dictionary Iteration")
# d = dict()
#
# d['key1'] = "val1"
# d['key2'] = 345
# for i in d:
# 	print(i, d[i])



# def armstrong(val):
# 	num_str = str(val)
# 	len_str = len(num_str)
# 	check = sum(int(i) ** len_str for i in num_str)
# 	return check == val
#
# n = int(input('Enter number to check whether it\'s armdtrong or not : '))
#
# if armstrong(n):
#     print(f"{n} is an Armstrong number.")
# else:
#     print(f"{n} is not an Armstrong number.")




# from collections import deque
#
# # Creating a Deque
# people_line = deque(['Alice', 'Bob', 'Charlie'])
# print(people_line)
# # Joining and Leaving
# people_line.append('David')
# print(people_line)
# people_line.pop()
# print(people_line)



# Student_info = [21, 'Rose', "CSE", 30, 40, 50, 120]
# print("Student_roll :", Student_info[0], end=' , ')
# print("Student_name :", Student_info[1], end=', ')
# print("Student_totalMarks :", Student_info[-1], end=' ')



# Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
# Student_info[2] = "HSC"
# Student_info[1] = 'Mayank'
# print(Student_info)




# def count_word_occurrences(sentence):
#     word_list = sentence.split()
#     unique_words = []
#     word_counts = []
#
#     for i in word_list:
#         # Check if the word is already in the unique_words list
#         if i in unique_words:
#             index = unique_words.index(i)
#             word_counts[index] += 1
#         else:
#             # Add the word to the unique_words list and initialize its count to 1
#             unique_words.append(i)
#             word_counts.append(1)
#
#     return unique_words, word_counts
#
# # User input
# user_sentence = input("Enter a sentence: ")
#
# unique_words, word_counts = count_word_occurrences(user_sentence)
# print("Word occurrences in the sentence:")
# for i, count in zip(unique_words, word_counts):
#     print(f"{i}: {count}")




# List1 = [ [ 1, 2, 3, 5 ], [ 4, 6, 7, 9 ], [ 8, 10, 11, 13 ] ]
# # Accesing the rows of the list
# for i in List1:
# 	print( i, end = ' -- ' )
#
# # Accessing each element of a 2D-list
# print( "\n" )
# print(len(List1))
# for i in range( len( List1 ) ):
# 	for j in range( len( List1[ i ] ) ):
# 		print( List1[ i ][ j ], end = " , " )
# 		print(i,j)



# multidimensional_dict = {
#         'first_level': {
#              'second_level_1': {
#                      'third_level_1': 1,
#                      'third_level_2': 2
#                },
#         'second_level_2': {
#                     'third_level_3': 3,
#                     'third_level_4': 4
#                    }
#               },
#  'another_first_level': {
#                 'second_level_3': {
#                              'third_level_5': 5,
#                              'third_level_6': 6
#                              },
#               'second_level_4': {
#                             'third_level_7': 7,
#                             'third_level_8': 8
#                     }
#              }
#         }
# print(multidimensional_dict)




# def two_sum_tuples(nums, target):
#     num_indices = {}  # Dictionary to store indices of elements
#
#     for i, num in enumerate(nums):
#         complement = target - num
#
#         # Check if the complement is already in the dictionary
#         if complement in num_indices:
#             return (complement, num)
#
#         # Add the current element to the dictionary
#         num_indices[num] = i
#
#     return None
#
# nums = [2, 7, 11, 15]
# target = 9
# result = two_sum_tuples(nums, target)
# print("Tuple of Elements:", result)






# class Solution:
#     # Function to reverse every sub-array group of size k.
#     def reverseInGroups(self, arr, N, K):
#         arr_list = list(arr)  # Convert set to a list
#         for i in range(0, N, K):
#             left = i
#             right = min(i + K - 1, N - 1)
#             while left < right:
#                 arr_list[left], arr_list[right] = arr_list[right], arr_list[left]
#                 left += 1
#                 right -= 1
#         return arr_list
#
#
#
#
# N = 5
# K = 3
# arr = {1,2,3,4,5}
# s1 = Solution()
# print(s1.reverseInGroups(arr,N,K))




# record = {1001: {'Name': "5 Star"         , "Price" : 10 , "Qn" : 200},
#           1002: {'Name': "Bar-One"        , "Price" : 20 , "Qn" : 100 },
#           1003: {'Name': "Candy"          , "Price" : 2  , "Qn" : 1000},
#           1004: {'Name': "Chocolate Cake" , "Price" : 550, "Qn" : 8 },
#           1005: {'Name': "Blueberry Cake" , "Price" : 650, "Qn" : 5 }}
#
# # print(record[1001]['Name'], record[1001]['Qn'])
# # print(record[1001],record[1005])
# # print(record)
#
# # for i in record:
# # 	print(i)
#
# print('-'*25,'Menu','-'*25)
# for i in record:
# 	print(i,':',record[i]['Name'],'|',record[i]['Price'],'|',record[i]['Qn'])
# print('-'*56)
#
# ui_pr = int(input('Enter Product ID : '))
# ui_qn = int(input('Enter Quentity : '))
#
# print('-'*25,'Bill','-'*25)
#
# print('Name 			:',record[ui_pr]['Name'])
# print('Price (Rs.) 	:',record[ui_pr]['Price'])
# print('Quentity 		:',ui_qn)
# print('-'*56)
#
# print('Price (Rs.) 	:',ui_qn * record[ui_pr]["Price"],"(Rs.)")
#
# print('-'*56)




'''
Updating
'''
# import json
#
# record = {1001: {'Name': "5 Star"         , "Price" : 10 , "Qn" : 200},
#           1002: {'Name': "Bar-One"        , "Price" : 20 , "Qn" : 100 },
#           1003: {'Name': "Candy"          , "Price" : 2  , "Qn" : 1000},
#           1004: {'Name': "Chocolate Cake" , "Price" : 550, "Qn" : 8 },
#           1005: {'Name': "Blueberry Cake" , "Price" : 650, "Qn" : 5 }}
#
# print('-'*25,'Menu','-'*25)
# for i in record:
# 	print(i,':',record[i]['Name'],'|',record[i]['Price'],'|',record[i]['Qn'])
# print('-'*56)
#
# ui_pr = int(input('Enter Product ID : '))
# ui_qn = int(input('Enter Quentity : '))
#
# print('-'*25,'Bill','-'*25)
#
# print('Name 			:',record[ui_pr]['Name'])
# print('Price (Rs.) 	:',record[ui_pr]['Price'])
# print('Quentity 		:',ui_qn)
# print('-'*56)
#
# print('Price (Rs.) 	:',ui_qn * record[ui_pr]["Price"],"(Rs.)")
#
# print('-'*56)
# json.dumps(record)





# import nltk
# # nltk.download( 'stopwords' )
# from nltk.corpus import stopwords
# # To check all the English stop words
# print( stopwords.words( 'english' ) )
# print('-'*30)
# x = 0
# for i in stopwords.words( 'english' ):
# 	x += 1
# print(x)
# print('-'*30)
# print(sum(1 for i in stopwords.words('english')))
# print('-'*30)
#
#
# from nltk.tokenize import word_tokenize,sent_tokenize
# txt="This is not a good time to talk."
# txt=word_tokenize(txt)
# for i in txt:
#     print(i)
# print('-'*30)
# stopwords=stopwords.words('english')
# for word in txt:
#     if((word.lower() not in stopwords) and (len(word)>=2)):
#         print(word)
# print('-'*30)
#
# crps = ('In its reply, the government said that a 100% door-to-door enumeration of castes and '
# 		'communities in the State was carried out in 1983, following the directions issued by '
# 		'the Supreme Court on October 14, 1982, and that data was being used till now for '
# 		'providing reservation to the backward classes, most backward classes and denotified communities.')
# crps = sent_tokenize(crps)
# stopwords=stopwords.words('english')
# for i in crps:
# 	if ((i.lower() not in stopwords) & (len(i) > 2)):
# 		print(i)


# crps_sentences = sent_tokenize(crps)
# for sentence in crps_sentences:
#     words = word_tokenize(sentence)
#     for word in words:
#         if word.lower() not in stopwords and len(word) > 2:
#             print(word)

# crps = sent_tokenize(crps)
# x = 0
# y = 0
# for ii in crps:
# 	words = word_tokenize(ii)
# 	for i in words:
# 		if i.lower() not in stopwords and len(i) > 2:
# 			x += 1
# 		y += 1
# print(x,y)
# print(100 - (27/63) * 100)





'''
Updating
'''
# import json
#
# record = {1001: {'Name': "5 Star         ", "Price" : 10 , "Qn" : 200},
#           1002: {'Name': "Bar-One        ", "Price" : 20 , "Qn" : 100 },
#           1003: {'Name': "Candy          ", "Price" : 2  , "Qn" : 1000},
#           1004: {'Name': "Chocolate Cake " ,"Price" : 550, "Qn" : 8 },
#           1005: {'Name': "Blueberry Cake " ,"Price" : 650, "Qn" : 5 }}
#
# print('-'*25,'Menu','-'*25)
# for i in record:
# 	print(i,':',record[i]['Name'],'|',record[i]['Price'],'|',record[i]['Qn'])
# print('-'*56)
#
# ui_pr = int(input('Enter Product ID : '))
# ui_qn = int(input('Enter Quentity : '))
#
# print('-'*25,'Bill','-'*25)
#
# print('Name 			:',record[ui_pr]['Name'])
# print('Price (Rs.) 	:',record[ui_pr]['Price'])
# print('Quentity 		:',ui_qn)
# print('-'*56)
#
# print('Price (Rs.) 	:',ui_qn * record[ui_pr]["Price"],"(Rs.)")
#
# print('-'*56)
# json.dumps(record)
#
# print('-'*25,'Bill','-'*25)
#
# print('Name 			:',record[ui_pr]['Name'])
# print('Price (Rs.) 	:',record[ui_pr]['Price'])
# print('Quentity 		:',ui_qn)
# print('-'*56)

# print("--------------------MENU---------------------")
# for key in record.keys():
#     print(key, record[key]['Name'], record[key]['Price'], record[key]['Name'],record[key]['Qn'])
# print("---------------------------------------------")
# print('')
#
# ui_pr = int(input("Enter product ID : "))
# ui_qn = int(input("Enter Quantity   : "))
#
# # print("---------------------------------------------")
# # print('')
# #
# # print("Name      : ", record[ui_pr]["Name"])
# # print("Price (Rs): ", record[ui_pr]["Price"])
# # print("Quantity  : ", ui_qn)
# # print("---------------------------------------------")
# # print("Billing   : ", ui_qn * record[ui_pr]["Price"], "Rs")
# # print("---------------------------------------------")
#
# if record[ui_pr]['Qn'] < ui_qn:
# 	print('Insufficien Quentity')
# 	print(f"There're only {record[ui_pr]['Qn']} Quantity left")
# else:
# 	print( "---------------------------------------------" )
# 	print( '				  Bill				' )
# 	print( "Name      			: ", record[ ui_pr ][ "Name" ] )
# 	print( "Price (Rs)			: ", record[ ui_pr ][ "Price" ] )
# 	print( "Quantity  			: ", ui_qn )
# 	print( "---------------------------------------------" )
# 	print( "Billing   			: ", ui_qn * record[ ui_pr ][ "Price" ], "Rs" )
# 	print( "---------------------------------------------" )
# 	record[ui_pr]['Qn'] = record[ui_pr]['Qn'] - ui_qn
# 	print( '' )
# 	print( "---------------------------------------------" )
# 	print( "  Thanks for your order, Inventory Updated!  " )
# 	print( "---------------------------------------------" )
#
# 	print( "\n--------------------MENU---------------------" )
# 	for key in record.keys():
# 		print( key, record[ key ][ 'Name' ], record[ key ][ 'Price' ], record[ key ][ 'Name' ], record[ key ][ 'Qn' ] )
# 	print( "---------------------------------------------" )





# class conducting_materials:
# 	def types_of_conducting_materials( self ):
# 		print("There're 3 types of materials.")
# 		print("\t1.Conducting"
# 			  "\n\t2.Magnetic"
# 			  "\n\t3.Insulating")
# 	def conducting_materials( self ):
# 		print("\nThere're 2 types of conducting materials.")
# 		print("1.Highly conducting materials"
# 			  "\n\tCu,Al,Ag,Au ----> Used in windings"
# 			  "\n\tCu 	   -> in Windings"
# 			  "\n\tAl 	   -> in tanks"
# 			  "\n\tCarbon -> in brush")
# 		print("2.Highly resistive materials"
# 			  "\n\t-> Alloys (mixing of multiple materials)"
# 			  "\n\t-> Used in heating elements"
# 			  "\n\t-> Low temp. resistive coefficient")
# 	def properties_of_highly_conducting_materials( self ):
# 		print("\nProperties of Highly Conducting materials:"
# 			  "\n\t-> Highest possible conductivity"
# 			  "\n\t-> Adequate mechanical strength and absense of brittleness"
# 			  "\n\t-> Corrosion resistance"
# 			  "\n\t-> Low temp. resistive coefficient"
# 			  "\n\t-> Valding and soldering resisrance should be less"
# 			  "\n\t-> Rollability and drawability")
#
# cm = conducting_materials()
# cm.types_of_conducting_materials()
# cm.conducting_materials()
# cm.properties_of_highly_conducting_materials()




'''
Single Linked List
'''
'''
Displaying
'''
# class node:
# 	def __init__( self,data ):
# 		self.data = data
# 		self.next = None
#
# class singlelinkedlist:
# 	def __init__( self ):
# 		self.head = None
# 	def display( self ):
# 		if self.head is None:
# 			print('List is empty')
# 		else:
# 			temp = self.head
# 			while temp:
# 				print(temp.data,end = ' ')
# 				if temp.next:
# 					print('--->',end=' ')
# 				temp = temp.next
#
# sll = singlelinkedlist()
# n1 = node(10)
# sll.head = n1
# n2 = node(20)
# n1.next = n2
# n3 = node(30)
# n2.next = n3
# sll.display()




# Home Work

# def remove_html_tags(reviews):
#     return re.sub(r'<[^<]+?>','',reviews)
#
# def remove_url(text):
#     return re.sub(r'http[s]?://\S+|www.\S+','',text)
#
# exclude = string.punctuation
#
# def remove_punctuation(text):
#     for char in exclude:
#         text = text.replace(char,'')
#     return text
#
# def remove_punctuation(text):
#     return text.translate(str.maketrans('','',string.punctuation))
#
# def spelling_correlation(text):
#     return TextBlob(text).correct()
#
# def remove_stopwords(text):
#     return [i for i in text.split() if i not in stop_words]
#
# def remove_emoji(text):
#     emoji_pattern = re.compile("["
#                                u"\U0001F600-\U0001F64F"
#                                # emoticons
#                                u"\U0001F300-\U0001F5FF"
#                                # symbols & pictographs
#                                u"\U0001F680-\U0001F6FF"
#                                # transport & map symbols
#                                u"\U0001F1E0-\U0001F1FF"
#                                # flags (105)
#                                u"\U00002702-\U00002780"
#                                u"\U000024C2-\U0001F251"
#                                "]+", flags=re.UNICODE)
#     return emoji_pattern.sub(r'', text)
# ps = PorterStemmer()
# def stem_words(text):
#     return " ".join([ps.stem(word) for word in word_tokenize(text)])
# sample = 'walk walking walked'





# for i in range(0,2):
# 	for j in range(0,6):
# 		print('*',end = ' ')
# 	print()


# x = 0
# for i in range(5):
# 	for j in range(5):
# 		x += 1
# 		print(x,end = ' ')
# 	print()



# for i in range(5):
# 	for j in range(5):
# 		print(i,end = ' ')
# 	print()



# for i in range(5):
# 	for j in range(5):
# 		print(j,end = ' ')
# 	print()



# for i in range(5,0,-1):
# 	for j in range(4,0,-1):
# 		print(i,end = ' ')
# 	print()



# for i in range(5,0,-1):
# 	for j in range(5,0,-1):
# 		print(j,end= ' ')
# 	print()



# x = int(input('Enter Rows Number   : '))
# y = int(input('Enter Column Number : '))
# for i in range(x):
# 	for j in range(y):
# 		print('*',end = ' ')
# 	print()



# for i in range(1,6):
# 	for j in range(1,4):
# 		print(i,end= ' ')
# 	print()



# for i in range(1,6):
# 	for j in range(1,4):
# 		print(j,end= ' ')
# 	print()



# x = 1
# for i in range(6):
# 	for j in range(6):
# 		print(x,end = ' ')
# 		x += 1
# 	print()



# for i in range(5):
# 	for j in range(3):
# 		print(j+1,i+1,end = ' ')
# 	print()




# ## Fibonacci Series
# a = 0
# b = 1
# n = int(input('Enter Number : '))
# print(a,b,end = ' ')
# for i in range(n-2):
# 	c = a + b
# 	a = b
# 	b = c
# 	print(c,end = ' ')



# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# chart_data = pd.DataFrame(np.random.randn(20,3),columns = ['Line_1','Line_2','Line_3'])
#
# st.header('1 Charts with random numbers')
# st.subheader('1.1 Line Chart')
# st.line_chart(chart_data)
#
# st.subheader('1.2 Area Chart')
# st.area_chart(chart_data)
#
# st.subheader('1.3 Bar Chart')
# st.bar_chart(chart_data)
#
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# st.header('2 Data Visualization with Matplotlib and Seaborn')
# st.subheader('2.1 Loading Dataframe')
# df = pd.read_csv(r"D:\DataScience\Iant\python\streamlit\iris.csv")
# st.dataframe(df)
#
# st.subheader('2.2 Bar graph with  matplotlib')
# fig = plt.figure(figsize=(15,8))
# df['species'].value_counts().plot(kind= 'bar')
# st.pyplot(fig)
#
# st.subheader('2.3 Distribution plot with seaborn')
# fig = plt.figure(figsize= (15,8))
# sns.distplot(df['sepal_length'])
# st.pyplot(fig)
#
# st.header('Multiple Graph')
# col1,col2 = st.columns(2)
# with col1:
#     col1.header = 'KDE = False'
#     # col1.write('KDE = False')
#     fig1 = plt.figure(figsize=(5,5))
#     sns.distplot(df['sepal_length'],kde = False)
#     st.pyplot(fig1)
# with col2:
#     col2.header = 'Hist = False'
#     # col2.write('Hist = False')
#     fig1 = plt.figure(figsize=(5,5))
#     sns.distplot(df['sepal_length'],hist = False)
#     st.pyplot(fig1)


# N1 = int(input('Enter Number:'))
# for i in range(1,N1+1):
# 	for j in range(1,N1+1):
# 		if j == 1 or i == N1 or j == N1:
# 			print('*',end = ' ')
# 		else :
# 			print(' ',end = ' ')
# 	print()



# N = 5
# for i in range( 1, N + 1 ):
# 	for j in range( N+1, i, -1 ):
# 		print( '*', end = ' ' )
# 	print()



# n,count = 5,0
# for _ in range(n):
# 	n -= 1
# 	count += 1
# print(count)


# def swap(a,b):
# 	return b,a
#
# a = int(input('Enter Number a: '))
# b = int(input('Enter Number b: '))
# a,b = swap(a,b)
# print(a - b)



# x = 0
# if False or [False] or (False):
# 	x += 1
# print(x)



# s = 'abc'
# for _ in range(10):
# 	s = tuple(s)
# print(s)
# print(len(s))



# t = [1, 2, 3, 4]
# x = t.pop() > t.pop() > t.pop()
# print(x)
# print(t)
# t.append(x)
# print(t)
# print(len(t))


# x = [1,2,3,20,1]
# print(x)
# m = x.pop() < x.pop() > x.pop()
# print(m)
# print(x)



# t = [1, 2, 3, 4,2]
# print(t)
# x = (t.pop() < t.pop()), t.pop()
# print(t)
# print(x)
# print(type(x))
# t.extend(x)
# print(t)
# print(len(t))



# t = [0, 1, 2]
# print(t)
# a = [10,20,30]
# t.extend([])
# print('extend',t)	# extend [0, 1, 2]
# t.append([])
# print('append',t)	# append [0, 1, 2, []]
# print(len(t))




# t = [0, 1, [2], 3]
# print(t)
# y = t[2]
# print(y)	# [2]
# y.append(20)
# print(y)	# [2, 20]
# print(t)	# [0, 1, [2, 20], 3]
# print(t[2])	# [2, 20]



# class1 = {"c1":"Mayank","c2":"Miral"}
#
# # print(type(class1))
# print(class1.keys())		# dict_keys(['c1', 'c2'])
# print(class1.values())		# dict_values(['Mayank', 'Miral'])
# print(class1.items())		# dict_items([('c1', 'Mayank'), ('c2', 'Miral')])
# # print(class1['c3'])			# KeyError
# print(class1.remove('c1'))



# import random
# import time
# Player1_HP = 100
# Player2_HP = 100
# turn = 1
#
# while (Player1_HP > 0 and Player2_HP > 0):
#     print("\n-----Turn Start-----")
#     print('Player 1 HP:',Player1_HP)
#     print('Player 2 HP:',Player2_HP)
#
#     if turn == 1:
#         # player1 turn
#         print('Player1 turn')
#         input('Press Enter to attack')
#         damage = random.randint(50,100) # Random 10 20 can be the attack damage
#         print('Generating attack.....💥')
#         time.sleep(2)
#         # Player2_HP = Player2_HP - damage
#         Player2_HP -= damage
#         print('Player 1 has attacked Player 2 for',damage,'damage ! ⚔️')
#
#         turn = 2
#
#     else:
#         # player2 turn
#         print('Player2 turn')
#         input('Press Enter to attack')
#         damage = random.randint(10,20) # Random 10 20 can be the attack damage
#         print('Generating attack.....💥')
#         time.sleep(2)
#         # Player2_HP = Player2_HP - damage
#         Player1_HP -= damage
#         print('Player 2 has attacked Player 1 for',damage,'damage ! ⚔️')
#
#         turn = 1
#
# print()
# if Player1_HP > 0:
#     print('Player 1 is winner 🏆')
# else:
#     print('Player 2 is winner 🏆')



# num = int(input('Enter Number:'))
# if num % 3 == 0 and num % 5 == 0:
# 	print('FizzBuzz')
# if num % 3 == 0 and num % 5 != 0:
# 	print('Fizz')
# if num % 5 == 0 and num % 3 != 0:
# 	print('Buzz')
# if num % 3 != 0 and num % 5 != 0:
# 	print(num)



# even_numbers_1 = [x for x in range(2,21) if x % 2 == 0]
# print(even_numbers_1)	# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# even_numbers_2 = list(range(2,21,2))
# print(even_numbers_2)	# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# even_numbers_3 = []
# for i in range(2,21):
# 	if i % 2 == 0:
# 		even_numbers_3.append(i)	# In snippet there's no mention of print statement
# print(even_numbers_3)	# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# even_numbers_4 = [2*i for i in range(1,11)]
# print(even_numbers_4)	# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



# age_1 = int(input('Enter your age : '))
# print(age_1)
# print(type(age_1))
#
# age_2 = input('Enter your age : ')
# age_2o1 = int(age_2)
# print(age_2o1)
# print(type(age_2o1))



# x = float(input('Enter number with decimal : '))
# print(x)
# print(type(x))
# x1 = int(x)
# print(x1)
# print(type(x1))



# x = 10
# x1 = str(x)
# print(x)
# print(type(x))
# print(x1)
# print(type(x1))




# # Option 1	Dissenting
# print('Option 1')
# month = int(input('Enter month number : '))
# if 3 <= month <= 5:
# 	print('Spring')
# if 6 <= month <= 8:
# 	print('Summer')
# if 9 <= month <= 11:
# 	print('Autumn')
# else:
# 	print('Winter')



# # option 2	Affirmative
# print('\nOption 2')
# month = int(input('Enter month number : '))
# if 3 <= month <= 5:
# 	print('Spring')
# if 6 <= month <= 8:
# 	print('Summer')
# if 9 <= month <= 11:
# 	print('Autumn')
# if month in [1,2,12]:
# 	print('Winter')



# # Option 3	Dissenting
# print('\nOption 3')
# month = int(input('Enter month number : '))
# season = 'Winter' if month in [12,1,2] else 'Spring' if 3 <= month <= 5 else 'Summer' if 6 <= month <= 8 else 'Autumn'
# print(season)



# # Option 4		Dissenting
# print('\nOption 4')
# month = int(input('Enter number of month : '))
# season = ['Winter','Winter','Spring','Spring','Spring','Summer','Summer','Summer','Summer','Autumn','Autumn','Autumn','Winter'][month - 1]
# print(season)





# # Opt1	Affirmative
# sq = [i**2 for i in range(1,11)]
# print(sq)		# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # Opt 2	Affirmative
# sq = [(x-1)*(x-1) for x in range(2,12)]
# print(sq)		# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # Opt 3	Affirmative
# sq = []
# for i in range(1,11):
# 	sq.append(i*i)
# print(sq)		# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # Opt 4	Dissenting
# sq = [i*i for i in range(10)]
# print(sq)		# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




# # Opt 1
# print(5/2)
# # Opt 2
# print(5//2)
# # Opt 3
# print(5%2)
# # Opt 4
# print(-5//2)



# # Opt 1		Affirmative
# num = input('Enter number with space : ').split()
# num = [int(i) for i in num]
# print(num)

# # Opt 2		Affirmative
# num = list(map(int,input('Enter num with space : ').split()))
# print(num)

# # Opt 3		Affirmative
# num = [int(x) for x in input('Enter numbers with space : ').split()]
# print(num)
#
# # Opt 4		Affirmative
# num = input('Enter numbers with spaces : ').split()
# num = list(map(int,num))
# print(num)
#
#
# print(int("3.14"))		# ValueError
# print(float("3.14"))		# 3.14
# print(str(3.14))			# 3.14
# print(bool(0))				# False



# # Leapyear:
# year = int(input('Enter Year :'))		# 100
# print('Year :',year)
# # Op-1								# Leap
# print('\nOp-1')
# if year % 4 == 0:
# 	print('Leap')
# else:
# 	print('Not leap')
#
# # Op-2								# Not leap
# print('\nOp-2')
# if year % 400 == 0:
# 	print('Leap')
# elif year % 100 == 0:
# 	print('Not leap')
# elif year % 4 == 0:
# 	print('Leap')
#
# # Op-3								# Not leap
# print('\nOp-3')
# print('Leap' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 'Not leap')
#
# # Op-4								# Not leap
# print('\nOp-4')
# is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# print('Leap'if is_leap else 'Not leap')




# print([i for i in {1:'a', 2:'b'}])

# my_tuple = 25
# print(my_tuple)


# print([1,2,3,4][-2:])



# print(10 != 10)



# import math
# print(math.floor(3.7))



# def multiply(a, b=2):
#     return a * b
#
# print(multiply(3))


# def factorial(n):
#     return 1 if n == 0 else n * factorial(n-1)
#
# print(factorial(5))



# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)





# stored_pass =  "secret123"
# user_input =  "sEcRet123"
# print(user_input.lower()  == stored_pass)




# def greet(*names):
#     for name in names:
#         print(f"Hello, {name}!",end=" ")
#
# greet("Alice", "Bob", "Charlie")



# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
#
# closure = outer(10)
# print(closure(5))


