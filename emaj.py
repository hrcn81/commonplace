# tup1 = ('a','b','c','d')
# list1 = list(tup1)
# l1 = list1
# if l1[1] == 'b':
#     l1[1] = '8-8'
# print(l1)

# m = 2
# n = 1
# while n <= 10:
#     print('2 X ',n,'=',m)
#     n += 1
#     m = n*2


# a =1
# b =2
# while a<= 10:
#     print(b,'X',a,'=',b*a)
#     a = a+1

# while + list
# l1 = [1,2,3,4,5,6]
# i = 0
# while i <= len(l1):
#     print(l1[i])
#     i += 1

# def hello(x):
#     print('Helo World!\n',x*2)
# hello(4)


# def addp(x):
#     print(x + x)
# addp(2)

# def addr(x):
#     return x+x
# r = addr(2)
# print(r)


# def oe(x):
#     if x%2==0:
#         return f'{x} is EVEN'
#     else:
#         return f'{x} is ODD'
# x = 56
# print(oe(x))


# m = lambda x: x**3
# print(m(3))


# lambda + filter
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst = list(filter(lambda x: (x%2==0), l1))
# print(lst)
# final = [x*2 for x in lst]
# print(final)


# lambda + map
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# final = list(map(lambda x: x*2,l1))
# print(final)

# from functools import reduce
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum1 = reduce(lambda x,y:x+y,l1)
# print(sum1)

# class phone:
#     def call(self):
#         print('Calling.......')
#     def play(self):
#         print('Playning......')
# p1 = phone()
# p1.call()
# p1.play()


# class vehicle:
#     def __init__(self,mileage,cost):
#         self.cost = cost
#         self.mileage = mileage
#     def status(self):
#         print('Mileage is:',self.mileage)
#         print('Cost is',self.cost)
        # print('It\'s a vehicle')
# v1 = vehicle(300,85000)
# v1.status()

# class car(vehicle):
#     def status(self):
#         print('It\'s child')
# c1 = car(222,55555)
# c1.status()

# class car(vehicle):
#     def __init__ (self,mileage,cost,tyres,hp):
#         super().__init__(mileage,cost)
#         self.tyres = tyres
#         self.hp = hp
#     def show_car_details(self):
#         print('WHeels:',self.tyres)
#         print('Power:',self.hp)
# c1 = car(300,1000000,4,600)
# c1.status()
# c1.show_car_details()

# class bank:
#     bname = 'BOB'
#     def __init__(self,name):
#         self.name = name
#         self.accBalance = 1000
#     def withdraw(self,withamt):
#         if(self.accBalance >= withamt):
#             self.accBalance -= withamt
#         else:
#             return 'Insufficient Balance'
#     def deposite(self,depoamt):
#         self.accBalance += depoamt
#     def showbalance(self):
#         return f'{self.name} Your Balance is: {self.accBalance}'

# list1 = []
# ls1 = list1
# ls1.append(bank('Mayank Solanki'))
# ls1.append(bank('Karim Telgi'))
# ls1.append(bank('Harshad Mehta'))
# ls1.append(bank('Vijay Maalya'))
# ls1.append(bank('Nirav Modi'))
# # print(ls1)

# for i in ls1:
#     x = i.showbalance()
#     print(x)





# def arith(func):
#     print("arith ", func)
#     def inner(a,b):
#         print("inner start...")
#         if b==0:
#             print("can't Devide")
#         else:
#             print(func(a,b))
#     return inner

# @arith
# def doDivision(a,b):
#     return a/b

# print("main call ",doDivision(10,3))
# print(doDivision(10/0))

# def arith(func):
#     def inner(a, b):
#         print("inner start...")
#         if b == 0:
#             print("Can't Divide by Zero")
#         else:
#             return func(a, b)

#     return inner

# @arith
# def doDivision(a, b):
#     return a / b

# print(doDivision(10, 3))
# doDivision(10, 3)
# print(doDivision(10, 0))
# doDivision(10, 0)


# def digits(d1, d2, d3):
#         combs = [(d1,d2,d3),(d1,d3,d2),(d2,d1,d3),(d2,d3,d1),(d3,d1,d2),(d3,d2,d1)]
#         print(combs)

# digits(1,2,3)

# def prt(num):
#     if num < 10:
#         print(num)
#     else:
#         # print(num)        # Tail Recursion
#         prt(num//10)
#         # print(num)        # Head Recursion
# prt(4003)

# add
# def add_numbers(num1,num2):
#     add = num1 + num2
#     return f'Addition: {add}'
# def multiply_numbers(num1,num2):
#     mul = num1*num2
#     return f'Multiplication: {mul}'
#
# n1 = int(input('1st Number: '))
# n2 = float(input('2nd Number: '))
# print(add_numbers(n1,n2))
# print(multiply_numbers(n1,n2))

# a = int(input('Enter NUmber: '))
# if a%2 == 0.0:
#     print(f'{a} is Even')
# else:
#     print(f'{a} is Odd')


# print('''Operators...
# + for Addition
# - for Substract
# * for Multiplication
# / for Division
# Use only one Operator at a time\n''')
#
# # n1 = float(input('Enter Number 1: '))
# # if n1 != float or n1 != int:
# #     print('Enter Numeric Data')
# # n2 = float(input('Enter Number 2: '))
# # opr = input('Enter Operator: ')
# # if opr == '+':
# #     print(n1 + n2)
# # elif opr == '-':
# #     print(n1 - n2)
# # elif opr == '*':
# #     print(n1 * n2)
# # elif opr == '/':
# #     print(n1 / n2)
# # elif opr != '+' or opr != '-' or opr != '*' or opr != '/':
# #     print('Invalid Operator.')
#
# n1 = input('Enter Number 1: ')
# if not (n1.replace(".", "", 1).isdigit() or (n1.isdigit() and n1[0] == '-')):
#     print('Enter Numeric Data for Number 1')
# else:
#     n1 = float(n1)
#
#     n2 = input('Enter Number 2: ')
#     if not (n2.replace(".", "", 1).isdigit() or (n2.isdigit() and n2[0] == '-')):
#         print('Enter Numeric Data for Number 2')
#     else:
#         n2 = float(n2)
#
#         opr = input('Enter Operator: ')
#
#         if opr in ['+', '-', '*', '/']:
#             if opr == '+':
#                 print(n1 + n2)
#             elif opr == '-':
#                 print(n1 - n2)
#             elif opr == '*':
#                 print(n1 * n2)
#             elif opr == '/':
#                 if n2 != 0:
#                     print(n1 / n2)
#                 else:
#                     print('Cannot divide by zero.')
#         else:
#             print('Invalid Operator.')



# i = 1
# print(i)
# print('--------1')
# while i<= 10:
#     print('--------2')
#     print(i,'Hi')
#     i += 2
#     print(i)
#     print('--------3')


# i = 10
# while i >= 20:
#     print(i)
#     i -= 1



# x = "Mayank Solanki"
# print(x)
# print(x[3])     # Indexing
# print(x[0:6])   # Slicing
# print(x[-1::-2])


# x = 'Mayank Solanki'
# v = len(x)
# # x = x[-1::-1]     #Method 1
# x = x[-1::-1]
# print(v)
# # for n in range(v-1,-1,-1):  #Method 2
#     print(x[n],end=' ')
# # print()
#
# # for i in x:
# #     print(i,end=' ')


# x = 'Mayank Solanki'
# n = x.lower()           # All in lower-case
# print(n)
# print()
# print(x.upper())        # All in upper-case
# print()
# print(x.capitalize())   # Only 1st word will be in capital
# print()
# print(x.title())        # 1st letter of all words will be in capital


# x = 'Mayank Solanki'
# print(x.find('a',4,12))       # (char,start,last(optional))
# print(x.find('f'))            # if character you're finding is not in string then it'll return -1
# print(x.index('a',4,100))     # (char,start,last(optional))
# print(x.find('f'))            # if character you're finding is not in string then it'll return error
# print(x.isalpha())            # checks whether the values in quotation are all alphabets or not
# print(x.isdigit())            # checks whether the values in quotation are all digits or not
# print(x.isalnum())            # checks whether the values in quotation are all digits or alphabets or not



# # format()
# t1 = 'Hello it\'s {fname} {lname}'.format(fname = 'Mayank',lname = 'Solanki')     # Name indexed
# t2 = 'Hello it\'s {0} {1}'.format('Mayank','Solanki')                       # Number indexed
# t3 = 'Hello it\'s {} {}'.format('Mayank','Solanki')                         # Empty indexed
# t4 = 'Hello it\'s |-- {a:>15} --|-- {b:^15} --|-- {c:<15} --|'.format(a='Mayank',b='Solanki',c=1832)  # (^:Center Alignment),(>:Right Alignment),(<:Left Alignment)
# '''
#     (t4)O|P:Hello it's |--          Mayank --|--     Solanki     --|-- 1832            --|
# '''
# print(t1)
# print(t2)
# print(t3)
# print(t4)

# def wlcm(name):
#     print('Welcome',name) # Your code here
# wlcm('alice')
# wlcm('John')
# wlcm('Python')


# def ten1(n):
#     if n == 1:
#         return 1
#     else:
#         return n + ten1(n-1)
# x = ten1(999)
# print(x)


# def fun1(x,y=0,z=0):
#     return x+y+z
# print(fun1(5,5))


# class nokia1:
#     def setdata(self,p='No Data Found',q='\nNo data Found'):
#         self.x=p
#         self.y=q
#     def display(self):
#         print(self.x,self.y)
#
# n1 = nokia1()
# n1.setdata('p','q')
# # n1.setdata()
# n1.display()

# class Nokia1:
#     def setdata(self, p='No Data Found', q='\nNo data Found'):
#         self.x = p
#         self.y = q
#     def display(self, newline='\n'):
#         print(self.x, newline, self.y)
#
# n1 = Nokia1()
# # n1.setdata(q=88, p=99)
# n1.setdata()
# n1.display(newline=' | ')  # You can change the newline character as per your requirement


# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 19:33:38 2023

@author: DELL
"""

# class Bank:
#     bank_balance = 0
#     deposits_count = 0
#     withdrawals_count = 0
#     total_deposited_amount = 0
#     total_withdrawal_amount = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.account_balance = 1000
#         Bank.bank_balance += 1000
#         self.total_deposited_amount_of_user = 0
#         self.total_withdrawal_amount_of_user = 0
#
#     def deposit(self, amount):
#         self.account_balance += amount
#         self.total_deposited_amount_of_user += amount
#         Bank.deposits_count += 1
#         Bank.total_deposited_amount += amount
#         Bank.bank_balance += amount
#
#     def withdraw(self, amount):
#         if self.account_balance >= amount:
#             self.account_balance -= amount
#             self.total_withdrawal_amount_of_user += amount
#             Bank.total_withdrawal_amount += amount
#             Bank.withdrawals_count += 1
#             Bank.bank_balance -= amount
#         else:
#             print("Insufficient balance!")
#
#     @staticmethod
#     def get_bank_details():
#         print("Total Transaction of Deposits", Bank.deposits_count)
#         print("Total Transaction of Withdrawal", Bank.withdrawals_count)
#         print("Total Amount of Deposits", Bank.total_deposited_amount)
#         print("Total Amount of Withdrawal", Bank.total_withdrawal_amount)
#         print("Total remaining amount in Bank:", Bank.bank_balance)
#
#
# obj_list = []
#
# obj_list.append(Bank("nirav"))
# obj_list.append(Bank("shakshi"))
# obj_list.append(Bank("Parth"))
#
# obj_list[0].deposit(500)
# obj_list[0].withdraw(450)
# obj_list[1].withdraw(240)
# obj_list[2].deposit(200)
# obj_list[2].deposit(250)
#
# for i in range(len(obj_list)):
#     print("Balance for customer", obj_list[i].name, "is", obj_list[i].account_balance)
#
# for i in range(len(obj_list)):
#     print("Total deposited amount of customer", obj_list[i].name, "is", obj_list[i].total_deposited_amount_of_user)
#
# Bank.get_bank_details()


# class Bank:
#     bname = 'Laxmi Cheat Fund'
#     print('Welcome To Our Bank')
#     def __init__(self,*mynk):
#         self.name = mynk[0]
#         self.age = mynk[1]
#         self.contact = mynk[2]
#         self.accBal = mynk[3]
#     def withdraw(self, withamt):
#         if self.accBal >= withamt:
#             self.accBal -= withamt
#             print(f'Withdrawal successful.Updated balance: {self.accBal}/- ₹')
#         else:
#             print('Insufficient Balance')
#     def deposit(self, depoamt):
#         self.accBal += depoamt
#         print(f'Deposit successful.Updated balance: {self.accBal}/- ₹')
#
#     def showstatus(self):
#         print('\nHERE\'S YOUR CURRENT STATUS')
#         print(f'Name: {self.name}\nAge: {self.age}\n'
#               f'Contact No.: {self.contact}\nPrevious Balance: {acbl}/- ₹\n'
#               f'Current Balance: {self.accBal}/- ₹')
#         print(input(f'---------------------\nPress ENTER to proceed further.'))
#
# # t1 = Bank()
# name1 = ['Bipasha ', 'Raju ', 'Shyam ', 'Baburao ', 'Devi ']
# sname = ['Basu','Bhai','Bhai','Aapte','Prasad']
# desig = ['\nYour Account ID: ']
# acnum = ['BOBSRT101','BOBSRT102','BOBSRT103','BOBSRT104','BOBSRT105']
# print(Bank.bname,'\n')
# for i in range(5):
#     print('Check Your Details.\n')
#     naming = name1[i] + sname[i] + desig[0] + acnum[i]
#     print(naming)
#     aging = int(input('Enter age: '))
#     contact = int(input('Enter contact number: '))
#     acbl = float(input('Enter current account balance: '))
#
#     t1 = Bank(naming, aging, contact, acbl)
#
#     if t1.accBal != 0:
#         wd = input('Do you want to withdraw (yes/no)? ')
#         if wd == 'yes':
#             wdwamt = float(input(f'Enter withdrawal amount: '))
#             t1.withdraw(wdwamt)
#     else:
#         pass
#
#     dp = input('Do you want to deposit (yes/no)? ')
#     if dp == 'yes':
#         depoamt = float(input(f'Enter deposit amount: '))
#         t1.deposit(depoamt)
#
#     t1.showstatus()


# class Nokia1:
#     mic = 10
#     cam = 20
#     def setData(self,p,q):
#         self.x=p
#         self.y=q
#     def display(self):
#         print(self.x,self.y)
#
# # n1 = Nokia1()
# # n1.setData(5,6)       # Instance
# # n1.display()
#
# Nokia1.setData(Nokia1,12,13)      # Static
# Nokia1.display(Nokia1)



# # Static
# class Nokia1:
#     mic = 10
#     cam = 20
#
#     @staticmethod
#     def setData(p, q):
#         print(f"Setting data: {p}, {q}")
#
#     @staticmethod
#     def display():
#         print("Displaying data")
#
# # Calling static methods without creating an instance
# Nokia1.setData(12, 13)
# Nokia1.display()


# Static (self,)
# class Nokia1:
#     mic = 10
#     cam = 20
#
#     @staticmethod
#     def setData(self, p, q):
#         print(f"Setting data: {p}, {q}")
#
#     @staticmethod
#     def display(self):
#         print("Displaying data")
#
# # Calling static methods without creating an instance
# Nokia1.setData(Nokia1, 12, 13)
# Nokia1.display(Nokia1)



# class employee:
#     def __init__(self,e,*mynk):
#         self.e = e
#         self.first = mynk[0]
#         self.last = mynk[1]
#         self.pay = mynk[2]
#         self.email = self.first.lower() + '.' + self.first.lower() + '@gmail.com'
#         self.all = self.e + self.email
#
# e1 = employee('E1 ','Melech','MacAuley',60000)
# print(e1.first,e1.last,e1.pay,e1.all)
# e2 = employee('Mayank','Solanki',50000)
# print(e2.first,e2.last,e1.pay,e2.email)


# l = [10,20,30,40,50,60]
# print(l)
# print()
# del l[:2]
# print(l)
# print()
# l.pop(2)
# print(l)
# print(l.pop(0))
# print(l)
# l.remove(10)
# print(l)

# l = [10,20,30,40,50,60,70]
# # l.insert(0,'Mayank')
# print(l)
# print()
# # n = {88,99,55}
# # # l.append(n)         # [10, 20, 30, 40, 50, 60, 70, {88, 99, 55}]
# # # print(l)
# # # print()
# # l.extend(n)         # [10, 20, 30, 40, 50, 60, 70, 88, 99, 55]
# # print(l)
# x = {'fname':'Mayank','lname':'Solanki'}
# print(type(x))
# l.append(x)            # [10, 20, 30, 40, 50, 60, 70, {'fname': 'Mayank', 'lname': 'Solanki'}]
# print(l)


# l1 = [10,20,40,50,20,100]
# l2 = [3,4,77,88,'m','n']
# l3 = [56,88,99,44,55,11]
# # Method 1
# t = len(l1)
# for i in range(t):              # Gives error when no. of elements are not same in both
#     print(l1[i],l2[i],l3[i])    # No. of elements must be same in all lists
#
# # Method 2
# for i,j,k in zip(l1,l2,l3):      # No error. Prints as per the least no. of elements
#     print(i,j,k)


# ms = 'Python'
# x = 0
# for i in ms:
#     x = x + 1
#     print(ms[0:x])
# for i in ms:
#     x = x - 1
#     print(ms[0:x])

# Stack
# l = []
# while True:
#     c = int(input('''
#     1. Push Element
#     2. Pop Element
#     3. Peek Element
#     4. Display Element
#     5. Exit
#     '''))
#     if c == 1:
#         n = input('Enter Value: ')
#         l.append(n)
#         print('Stack:', l)
#     elif c == 2:
#         if len(l) == 0:
#             print('Empty Stack')
#         else:
#             p = l.pop()
#             print('Popped Element:', p)
#             print('Stack:', l)
#     elif c == 3:
#         if len(l) == 0:
#             print('Empty Stack')
#         else:
#             print('Peek Element:', l[-1])
#     elif c == 4:
#         print('Display Stack:', l)
#     elif c == 5:
#         break
#     else:
#         print('Invalid Character')


# Queue
# queue = []

# while True:
#     choice = int(input('''
#     1. Enqueue Element
#     2. Dequeue Element
#     3. Peek Element
#     4. Display Queue
#     5. Exit
#     '''))

#     if choice == 1:
#         value = input('Enter Value: ')
#         queue.append(value)
#         print('Queue:', queue)
#     elif choice == 2:
#         if len(queue) == 0:
#             print('Empty Queue')
#         else:
#             dequeued_element = queue.pop(0)
#             print('Dequeued Element:', dequeued_element)
#             print('Queue:', queue)
#     elif choice == 3:
#         if len(queue) == 0:
#             print('Empty Queue')
#         else:
#             print('Peek Element:', queue[0])
#     elif choice == 4:
#         print('Display Queue:', queue)
#     elif choice == 5:
#         break
#     else:
#         print('Invalid Character....')





# import math as mt

# x = 11.1
# print(mt.ceil(x))



# class Base:
#     def __init__(self):
#         print('Base call....')
#
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#         print('Derived call....')
#
# d1 = Derived()

# call base call....

# Explanation:
# - The class names should be capitalized according to the PEP 8 style guide.
# - The Derived class should call the __init__ method of the base class using super() to ensure that the base class is properly initialized.
# - The print statements can be left as they are, as they are already concise and clear.



# # pickle module
# import pickle
# l = [10,20,30,40,50]
# pickle.dump(l, open('data.pkl', 'wb'))
# pickle.load(open('data.pkl', 'rb'))
# # print(pickle.dump(l, open('data.pkl', 'wb')))
# print(pickle.load(open('data.pkl', 'rb')))


# Python Object to JSON Conversion
# import json
# p = '{"Name":"John","Age":30,"City":"New York"}'
# f = json.dumps(p)      # converts Python Object to JSON
# print(type(f))
# print(f)


# JSON to Python Object Conversion
# import json
# x = '{"name":"John","age":30,"city":"New York"}'
# y = json.loads(x)       # converts JSON to Python Object
# print(type(y))
# print(y)


# class a:
#         def dispa(self):
#                 print('Hello 1')
# class b(a):
#         def dispb(self):
#                 print('Hello 2')

# obj = b()
# obj.dispa()
# obj.dispb()


# import numpy as np
# np.min():
# np.amin():
# a.min():


# s = input('Enter String:')
# op = s[::-1]
# print(op)


# my_list = [1, 2, 3, 4, 3, 5, 6]
# # my_list.remove(3)       # Method 1
# # print(my_list)
# element = 3               # Method 2
# while element in my_list:
#     my_list.remove(element)
# print(my_list)


# ml = [1, 2, 3, 4, 3, 5, 6]
# # st = set(ml)      # Method 1
# # ml = list(st)
# # print(ml)
# uniquelist = []    # Method 2
# print('Original List: ',ml)
# for item in ml:
#     if item not in uniquelist:
#         uniquelist.append(item)
# print('Removed Duplicate',uniquelist)



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers[:]:
#     if num % 2 != 0:
#         numbers.remove(num)
# print('Removed Odd Numbers:',numbers)



# ol = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# print(len(ol))
# for i in ol:
#         print(i,ol,'\n')
#         print(len(ol))



# Remove words from a list that have a specific length

# Modified code:

# words = ["apple", "banana", "grape", "kiwi", "orange", "pear"]
# length_to_remove = 5
# print("Original List:", words)
# # Use list comprehension to filter out words with length equal to length_to_remove
# words1 = [word for word in words if len(word) != length_to_remove]
# print(f"List after removing words with length {length_to_remove}:", words1)
# # Print the removed words
# removed_words = [word for word in words if len(word) == length_to_remove]
# print("Removed words:", removed_words)



# # Remove elements from the beginning of a list until a condition is met
# numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
# condition_value = 5
# print("Original List:", numbers)
# numbers = [num for num in numbers if num >= condition_value]
# print("List after removing elements until the condition is met:", numbers)
# # Explanation:
# # - The original code uses a while loop and pop() method to remove elements from the list until the condition is met.
# # - The refactored code uses a list comprehension to create a new list that only contains elements that are greater than or
# #     equal to the condition value.
# # - This approach is more concise and easier to read, as it eliminates the need for a while loop and pop() method.


# Remove a specific element from the list based on user input
# Updated code:

# my_list = [10, 20, 30, 40, 50]
# print("Original List:", my_list)
# element_to_remove = int(input("Enter the element to remove: "))

# my_list = [x for x in my_list if x != element_to_remove]

# print("List after removing", element_to_remove, ":", my_list)



# # Remove multiple occurrences of a specific element from the list
# Improved and shortened code using Python's list comprehension and f-string formatting

# my_list = [1, 2, 3, 3, 4, 3, 5, 6, 3]
# element_to_remove = 3

# my_list = [x for x in my_list if x != element_to_remove]

# print(f"List after removing all occurrences of {element_to_remove}: {my_list}")



# s = 'Mayank'
# print('Even indexed:',','.join(s[::2]))
# print('Odd indexed:',','.join(s[1::2]))



# l1 = [10,20,30,40,50]
# l2 = [60,70,80,90,100]

# l = []
# for a,b in zip(l1,l2):
#     print(a,b)
# n = ((a,b) for a,b in zip(l1,l2))
# print(type(n))


# l = 'ab cd ef gh ij'
# print(l,'\n')
# n = l.split()
# print(n,'\n')
# m = ' '.join(n)
# print(m)


# class Temperature:
#         def __init__(self, tf=0, tc=0):
#                 self.far = tf
#                 self.cel = tc
#         def show(self):
#                 print('Fahrenheit :',self.far)
#                 print('Celsius    :',self.cel)

# print('''Select Conversion:
#       1. Farhenheit to Celsius
#       2. Celsius to Farhenheit
#       3. Exit''')

# n = 0
# m = int(input('Enter How Much time you want to convert: '))
# while n<m:
#         temp = int(input('Choose Your Option (1/2/3)?: '))
#         n = n+1
#         if temp == 1:
#                 tempc = float(input('Enter celsius:'))
#                 tempf = (tempc * 1.8) + 32
#         elif temp == 2:
#                 tempf = float(input('Enter fahrenheit:'))
#                 tempc = (tempf - 32) / 1.8
#         elif temp == 3:
#                 break
#         else:
#                 print('Invalid Input')

#         t = Temperature(tempf, tempc)
#         t.show()



# class temperature:
#         def __init__(self,tf,tc):
#                 self.far = tf
#                 self.cel = tc
#         def cTf(self):
#                 self.far = (self.tc * 1.8) + 32
#                 return self.far
#         def fTc(self):
#                 self.cel = (self.far - 32 )/1.8
#                 return self.cel
#         def result(self):
#                 print('Fahrenheit :',self.far)
#                 print('Celsius    :',self.cel)

# t1 = temperature(10,0)
# t1.result()



# class temperature:
#     def c2f(self, celsius):
#         return (celsius * 9/5) + 32

#     def f2c(self, fahrenheit):
#         return (fahrenheit - 32) * (5/9)

# # Example usage with user input:
# t1 = temperature()
# # Get temperature from user
# tempcel = float(input("Enter temperature in Celsius: "))
# fahrenheit_result = t1.c2f(tempcel)
# print(f"{tempcel} Celsius = {fahrenheit_result:.2f} Fahrenheit")

# # Get temperature from user
# tempfar = float(input("Enter temperature in Fahrenheit: "))
# celsius_result = t1.f2c(tempfar)
# print(f"{tempfar} Fahrenheit = {celsius_result:.2f} Celsius")



# To retrieve last name from list of names

# names = ['Mayank Solanki','Aston Martin','Melech McAuley','Max Versteppen']
# last = [x.split(' ')[-1] for x in names]
# print(last)

# names = ['Mayank Solanki', 'Aston Martin', 'Melech McAuley', 'Max Versteppen']
# lasti = [x.split(' ')[-1] for x in names if 'i' in x.split(' ')[-1]]
# print(lasti)


# Explanation:
# - Removed the unnecessary "where" keyword and replaced it with "if" for filtering the names.
# - Removed the unnecessary assignment of "names" inside the list comprehension.
# - Updated the code to use the more modern syntax for list comprehension.


# def even_squares_generator(limit):
#     for i in range(2, limit, 2):
#         yield i ** 2

# # Using the generator
# even_squares_gen = even_squares_generator(10)

# # Iterating over the generator
# for square in even_squares_gen:
#     print(square)
'''
# f = open('C:\\Users\\mayan\\OneDrive\\Desktop\\mynk.txt','r')
# print('file created......')
# f.write('mene likha hei bhai dekh liyo thik se')
# print('file written......')
# x = f.read(500)               # will read only 500 characters
# print(x)
# x = (f.readline())            # will read only one line
# print(x)
# x = f.readlines()             # will read all lines
# print(x)
# f.close()
# print('file closed.....')     # file will automatically close when you are done with it

# import os
# os.remove('C:\\Users\\mayan\\OneDrive\\Desktop\\mynk.txt')
# print('File Deleted.....')
'''


# class car:
#     model = 'Volvo'
#     color = 'Red'
# c1 = car()
# print(c1)
# print(c1.(model,color))
# print(c1.model,c1.color)
# print(c1.color)



# class car:
#         def __init__(self,mdl,clr):
#                 self.mdl = mdl
#                 self.clr = clr

# c1 = car('BMW','Blue')
# print(c1.mdl)
# print(c1.clr)


# import numpy
# import scipy
# # import matplotlib
# import pandas
# import matplotlib.pyplot as plt
#
# plt.plot([1,2,3,4],[1,4,9,16])
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.title('Mayank\'s Plot')
# print(plt.show())




# class demo():
#         a = 10
#         def sv(self):
#                 self.c = self.a*self.a
#                 print(f'{self.a}**2 = {self.c}')
#         def sv1(self,a=0,b=0):
#                 print(a + b)
# d1 = demo()
# d1.sv()
# d1.sv1('m ', '2')



# class bikeshop:
#     def __init__(self,stock):
#         self.stock = stock
#     def displaystock(self):
#         print('Total Bikes:',self.stock)
#     def rentforbike(self,q):
#         if q <= 0:
#             print('Enter Value > 0')
#         elif q > self.stock:
#             print('Enter Value less than stock')
#         else:
#             self.stock -= q
#             print('Total Prices:',n*350)
#             print('Total Bikes:',self.stock)
# while True:
#     obj = bikeshop(100)
#     uc = int(input('''
# Choose Your Option:
#     1. Display Bikes:
#     2. Rent a Bikes:
#     3. Exit:
#     '''))
#     if uc == 1:
#         obj.displaystock()
#     elif uc == 2:
#         n = int(input('Enter Qty: '))
#         obj.rentforbike(n)
#     else:
#         break


# class BikeShop:
#     def __init__(self, stock):
#         self.stock = stock
#
#     def display_stock(self):
#         print('Total Bikes:', self.stock)
#
#     def rent_for_bike(self, quantity):
#         try:
#             quantity = int(quantity)
#             if 0 < quantity <= self.stock:
#                 self.stock -= quantity
#                 print('Rent successful!')
#                 print('Total Price:', quantity * 350)
#                 print('Remaining Bikes:', self.stock)
#             else:
#                 print('Invalid quantity. Please enter a value between 1 and', self.stock)
#         except ValueError:
#             print('Invalid input. Please enter a valid number.')
#
# # Create the bikeshop object outside the loop
# bike_shop = BikeShop(100)
#
# while True:
#     print('\nWelcome to the Bike Shop!')
#     user_choice = input('Choose Your Option:\n'
#                         '1. Display Bikes\n'
#                         '2. Rent a Bike\n'
#                         '3. Exit\n'
#                         'Your choice: ')
#
#     if user_choice == '1':
#         bike_shop.display_stock()
#     elif user_choice == '2':
#         quantity = input('Enter Quantity: ')
#         bike_shop.rent_for_bike(quantity)
#     elif user_choice == '3':
#         print('Thank you for visiting the Bike Shop!')
#         break
#     else:
#         print('Invalid Option. Please choose again.')




# class Bike:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class BikeShop:
#     def __init__(self, stock):
#         self.stock = stock
#         self.bikes = {'Mountain Bike': Bike('Mountain Bike', 500),
#                       'Road Bike': Bike('Road Bike', 700),
#                       'Electric Bike': Bike('Electric Bike', 1000)}
#         self.rental_history = []
#
#     def display_stock(self):
#         print('Available Bikes:')
#         for bike in self.bikes.values():
#             print(f'{bike.name} - ${bike.price}')
#
#     def rent_bike(self, bike_type, quantity):
#         if bike_type in self.bikes:
#             bike = self.bikes[bike_type]
#             total_price = quantity * bike.price
#
#             if 0 < quantity <= self.stock[bike_type]:
#                 self.stock[bike_type] -= quantity
#                 self.rental_history.append({'bike_type': bike_type, 'quantity': quantity, 'total_price': total_price})
#                 print(f'Rental successful!\nTotal Price: ${total_price}\nRemaining {bike_type}s: {self.stock[bike_type]}')
#             else:
#                 print(f'Invalid quantity. Please enter a value between 1 and {self.stock[bike_type]}')
#         else:
#             print('Invalid bike type.')
#
# class Customer:
#     def __init__(self, name):
#         self.name = name
#         self.rented_bikes = []
#
# # Create the bikeshop object outside the loop
# bike_shop = BikeShop({'Mountain Bike': 10, 'Road Bike': 15, 'Electric Bike': 5})
#
# while True:
#     print('\nWelcome to the Bike Shop!')
#     user_choice = input('Choose Your Option:\n'
#                         '1. Display Bikes\n'
#                         '2. Rent a Bike\n'
#                         '3. View Rental History\n'
#                         '4. Exit\n'
#                         'Your choice: ')
#
#     if user_choice == '1':
#         bike_shop.display_stock()
#     elif user_choice == '2':
#         bike_type = input('Enter Bike Type (Mountain Bike/Road Bike/Electric Bike): ')
#         quantity = int(input('Enter Quantity: '))
#         bike_shop.rent_bike(bike_type, quantity)
#     elif user_choice == '3':
#         print('Rental History:')
#         for entry in bike_shop.rental_history:
#             print(f'{entry["quantity"]} {entry["bike_type"]}(s) - ${entry["total_price"]}')
#     elif user_choice == '4':
#         print('Thank you for visiting the Bike Shop!')
#         break
#     else:
#         print('Invalid Option. Please choose again.')




# from datetime import datetime, timedelta
#
# class Bike:
#     def __init__(self, name, price_per_hour, manufacturer, manufacturing_date):
#         self.name = name
#         self.price_per_hour = price_per_hour
#         self.manufacturer = manufacturer
#         self.manufacturing_date = manufacturing_date
#
#     def get_age(self):
#         today = datetime.now()
#         age = today.year - self.manufacturing_date.year - ((today.month, today.day) < (self.manufacturing_date.month, self.manufacturing_date.day))
#         return age
#
# class Customer:
#     def __init__(self, name, loyalty_points=0):
#         self.name = name
#         self.rented_bikes = []
#         self.loyalty_points = loyalty_points
#
#     def add_loyalty_points(self, points):
#         self.loyalty_points += points
#
# class Rental:
#     def __init__(self, bike, customer, duration_hours):
#         self.bike = bike
#         self.customer = customer
#         self.duration_hours = duration_hours
#         self.rental_time = datetime.now()
#
#     def calculate_price(self):
#         total_price = self.duration_hours * self.bike.price_per_hour
#         return total_price
#
# class BikeShop:
#     def __init__(self, stock):
#         self.stock = {
#             'Mountain Bike': Bike('Mountain Bike', 10, 'XYZ Bikes', datetime(2020, 1, 1)),
#             'Road Bike': Bike('Road Bike', 15, 'ABC Cycles', datetime(2019, 6, 15)),
#             'Electric Bike': Bike('Electric Bike', 20, 'EcoRide', datetime(2021, 3, 10))
#         }
#         self.customers = {}
#         self.rental_history = []
#
#     def display_stock(self):
#         print('Available Bikes:')
#         for bike_name, bike in self.stock.items():
#             age = bike.get_age()
#             print(f'{bike_name} - Fee: ${bike.price_per_hour}/hour, '
#                   f'Manufacturer: {bike.manufacturer}, Age: {age} years')
#
#     def rent_bike(self, customer_name, bike_name, duration_hours):
#         if bike_name in self.stock:
#             bike = self.stock[bike_name]
#             if customer_name not in self.customers:
#                 self.customers[customer_name] = Customer(customer_name)
#
#             customer = self.customers[customer_name]
#             rental = Rental(bike, customer, duration_hours)
#
#             total_price = rental.calculate_price()
#             discount = min(10, customer.loyalty_points)
#             discounted_price = total_price * (1 - discount / 100)
#
#             customer.add_loyalty_points(duration_hours * 2)
#             customer.rented_bikes.append(rental)
#
#             self.rental_history.append({
#                 'customer': customer_name,
#                 'bike': bike_name,
#                 'duration': duration_hours,
#                 'total_price': discounted_price
#             })
#
#             print(f'Rental successful!\nTotal Price: ${discounted_price:.2f}')
#         else:
#             print('Invalid bike name.')
#
# # Create the bikeshop object outside the loop
# bike_shop = BikeShop(None)
#
# while True:
#     print('\nWelcome to the Advanced Bike Shop!')
#     user_choice = input('Choose Your Option:\n'
#                         '1. Display Bikes\n'
#                         '2. Rent a Bike\n'
#                         '3. View Rental History\n'
#                         '4. Exit\n'
#                         'Your choice: ')
#
#     if user_choice == '1':
#         bike_shop.display_stock()
#     elif user_choice == '2':
#         customer_name = input('Enter Your Name: ')
#         bike_name = input('Enter Bike Name (Mountain Bike/Road Bike/Electric Bike): ')
#         duration_hours = int(input('Enter Rental Duration (in hours): '))
#         bike_shop.rent_bike(customer_name, bike_name, duration_hours)
#     elif user_choice == '3':
#         print('Rental History:')
#         for entry in bike_shop.rental_history:
#             print(f'{entry["customer"]} rented {entry["bike"]} for {entry["duration"]} hours. '
#                   f'Total Price: ${entry["total_price"]:.2f}')
#     elif user_choice == '4':
#         print('Thank you for visiting the Advanced Bike Shop!')
#         break
#     else:
#         print('Invalid Option. Please choose again.')



# from datetime import datetime, timedelta
# from prettytable import PrettyTable
#
# class Bike:
#     def __init__(self, name, manufacturer, price_per_hour, manufacturing_date):
#         self.name = name
#         self.manufacturer = manufacturer
#         self.price_per_hour = price_per_hour
#         self.manufacturing_date = manufacturing_date
#
#     def calculate_age(self):
#         today = datetime.now()
#         age = today.year - self.manufacturing_date.year - ((today.month, today.day) < (self.manufacturing_date.month, self.manufacturing_date.day))
#         return age
#
# class Customer:
#     def __init__(self, name, loyalty_points=0):
#         self.name = name
#         self.rented_bikes = []
#         self.loyalty_points = loyalty_points
#
#     def add_loyalty_points(self, points):
#         self.loyalty_points += points
#
# class Rental:
#     def __init__(self, bike, customer, duration_hours):
#         self.bike = bike
#         self.customer = customer
#         self.duration_hours = duration_hours
#         self.rental_time = datetime.now()
#
#     def calculate_price(self):
#         total_price = self.duration_hours * self.bike.price_per_hour
#         return total_price
#
# class BikeShop:
#     def __init__(self, stock):
#         self.stock = {bike_name: Bike(bike_name, bike_info["manufacturer"], bike_info["price_per_hour"], bike_info["manufacturing_date"])
#                       for bike_name, bike_info in stock.items()}
#         self.customers = {}
#         self.rental_history = []
#
#     def display_stock(self):
#         table = PrettyTable()
#         table.field_names = ["Bike", "Manufacturer", "Price per Hour", "Manufacturing Date", "Age"]
#
#         for bike_name, bike in self.stock.items():
#             age = bike.calculate_age()
#             table.add_row([bike.name, bike.manufacturer, f"${bike.price_per_hour}", bike.manufacturing_date.strftime("%Y-%m-%d"), age])
#
#         print("Available Bikes:")
#         print(table)
#
#     def rent_bike(self, customer_name, bike_name, duration_hours):
#         if bike_name in self.stock:
#             bike = self.stock[bike_name]
#             if customer_name not in self.customers:
#                 self.customers[customer_name] = Customer(customer_name)
#
#             customer = self.customers[customer_name]
#             rental = Rental(bike, customer, duration_hours)
#
#             total_price = rental.calculate_price()
#             discount = min(10, customer.loyalty_points)
#             discounted_price = total_price * (1 - discount / 100)
#
#             customer.add_loyalty_points(duration_hours * 2)
#             customer.rented_bikes.append(rental)
#
#             self.rental_history.append({
#                 'customer': customer_name,
#                 'bike': bike_name,
#                 'duration': duration_hours,
#                 'total_price': discounted_price
#             })
#
#             print(f'Rental successful!\nTotal Price: ${discounted_price:.2f}')
#         else:
#             print('Invalid bike name.')
#
# # Create the bikeshop object outside the loop
# bike_shop = BikeShop({
#     'Mountain Bike': {'manufacturer': 'Brand A', 'price_per_hour': 10, 'manufacturing_date': datetime(2021, 1, 1)},
#     'Road Bike': {'manufacturer': 'Brand B', 'price_per_hour': 15, 'manufacturing_date': datetime(2020, 5, 1)},
#     'Electric Bike': {'manufacturer': 'Brand C', 'price_per_hour': 20, 'manufacturing_date': datetime(2022, 8, 1)}
# })
#
# while True:
#     print('\nWelcome to the Advanced Bike Shop!')
#     user_choice = input('Choose Your Option:\n'
#                         '1. Display Bikes\n'
#                         '2. Rent a Bike\n'
#                         '3. View Rental History\n'
#                         '4. Exit\n'
#                         'Your choice: ')
#
#     if user_choice == '1':
#         bike_shop.display_stock()
#     elif user_choice == '2':
#         customer_name = input('Enter Your Name: ')
#         bike_name = input('Enter Bike Name (Mountain Bike/Road Bike/Electric Bike): ')
#         duration_hours = int(input('Enter Rental Duration (in hours): '))
#         bike_shop.rent_bike(customer_name, bike_name, duration_hours)
#     elif user_choice == '3':
#         print('Rental History:')
#         for entry in bike_shop.rental_history:
#             print(f'{entry["customer"]} rented {entry["bike"]} for {entry["duration"]} hours. '
#                   f'Total Price: ${entry["total_price"]:.2f}')
#     elif user_choice == '4':
#         print('Thank you for visiting the Advanced Bike Shop!')
#         break
#     else:
#         print('Invalid Option. Please choose again.')



# from datetime import datetime, timedelta
# from prettytable import PrettyTable
#
# class Bike:
#     def __init__(self, name, manufacturer, price_per_hour, manufacturing_date):
#         self.name = name
#         self.manufacturer = manufacturer
#         self.price_per_hour = price_per_hour
#         self.manufacturing_date = manufacturing_date
#
#     def calculate_age(self):
#         today = datetime.now()
#         age = today.year - self.manufacturing_date.year - ((today.month, today.day) < (self.manufacturing_date.month, self.manufacturing_date.day))
#         return age
#
# class Customer:
#     def __init__(self, name, loyalty_points=0):
#         self.name = name
#         self.rented_bikes = []
#         self.loyalty_points = loyalty_points
#
#     def add_loyalty_points(self, points):
#         self.loyalty_points += points
#
# class Rental:
#     def __init__(self, bike, customer, duration_hours):
#         self.bike = bike
#         self.customer = customer
#         self.duration_hours = duration_hours
#         self.rental_time = datetime.now()
#
#     def calculate_price(self):
#         total_price = self.duration_hours * self.bike.price_per_hour
#         return total_price
#
#     def get_rental_time(self):
#         return self.rental_time.strftime("%Y-%m-%d %H:%M:%S")
#
# class BikeShop:
#     def __init__(self, stock):
#         self.stock = {bike_name: Bike(bike_name, bike_info["manufacturer"], bike_info["price_per_hour"], bike_info["manufacturing_date"])
#                       for bike_name, bike_info in stock.items()}
#         self.customers = {}
#         self.rental_history = []
#
#     def display_stock(self):
#         table = PrettyTable()
#         table.field_names = ["Bike", "Manufacturer", "Price per Hour", "Manufacturing Date", "Age"]
#
#         for bike_name, bike in self.stock.items():
#             age = bike.calculate_age()
#             table.add_row([bike.name, bike.manufacturer, f"${bike.price_per_hour}", bike.manufacturing_date.strftime("%Y-%m-%d"), age])
#
#         print("Available Bikes:")
#         print(table)
#
#     def rent_bike(self, customer_name, bike_name, duration_hours):
#         if bike_name in self.stock:
#             bike = self.stock[bike_name]
#             if customer_name not in self.customers:
#                 self.customers[customer_name] = Customer(customer_name)
#
#             customer = self.customers[customer_name]
#             rental = Rental(bike, customer, duration_hours)
#
#             total_price = rental.calculate_price()
#             discount = min(10, customer.loyalty_points)
#             discounted_price = total_price * (1 - discount / 100)
#
#             customer.add_loyalty_points(duration_hours * 2)
#             customer.rented_bikes.append(rental)
#
#             self.rental_history.append({
#                 'customer': customer_name,
#                 'bike': bike_name,
#                 'duration': duration_hours,
#                 'total_price': discounted_price,
#                 'rental_time': rental.get_rental_time()
#             })
#
#             print(f'Rental successful!\nTotal Price: ${discounted_price:.2f}')
#         else:
#             print('Invalid bike name.')
#
#     def display_rental_history(self):
#         table = PrettyTable()
#         table.field_names = ["Customer", "Bike", "Duration (hours)", "Total Price", "Rental Time"]
#
#         for entry in self.rental_history:
#             table.add_row([entry["customer"], entry["bike"], entry["duration"], f"${entry["total_price"]:.2f}", entry["rental_time"]])
#
#         print('Rental History:')
#         print(table)
#
# # Create the bikeshop object outside the loop
# bike_shop = BikeShop({
#     'Mountain Bike': {'manufacturer': 'Brand A', 'price_per_hour': 10, 'manufacturing_date': datetime(2021, 1, 1)},
#     'Road Bike': {'manufacturer': 'Brand B', 'price_per_hour': 15, 'manufacturing_date': datetime(2020, 5, 1)},
#     'Electric Bike': {'manufacturer': 'Brand C', 'price_per_hour': 20, 'manufacturing_date': datetime(2022, 8, 1)}
# })
#
# while True:
#     print('\nWelcome to the Advanced Bike Shop!')
#     user_choice = input('Choose Your Option:\n'
#                         '1. Display Bikes\n'
#                         '2. Rent a Bike\n'
#                         '3. View Rental History\n'
#                         '4. Exit\n'
#                         'Your choice: ')
#
#     if user_choice == '1':
#         bike_shop.display_stock()
#     elif user_choice == '2':
#         customer_name = input('Enter Your Name: ')
#         bike_name = input('Enter Bike Name (Mountain Bike/Road Bike/Electric Bike): ')
#         duration_hours = int(input('Enter Rental Duration (in hours): '))
#         bike_shop.rent_bike(customer_name, bike_name, duration_hours)
#     elif user_choice == '3':
#         bike_shop.display_rental_history()
#     elif user_choice == '4':
#         print('Thank you for visiting the Advanced Bike Shop!')
#         break
#     else:
#         print('Invalid Option. Please choose again.')



# from datetime import datetime, timedelta
# from prettytable import PrettyTable
#
# class Bike:
#     def __init__(self, name, manufacturer, price_per_hour, manufacturing_date, maintenance_interval=100):
#         self.name = name
#         self.manufacturer = manufacturer
#         self.price_per_hour = price_per_hour
#         self.manufacturing_date = manufacturing_date
#         self.maintenance_interval = maintenance_interval
#         self.maintenance_count = 0
#
#     def calculate_age(self):
#         today = datetime.now()
#         age = today.year - self.manufacturing_date.year - ((today.month, today.day) < (self.manufacturing_date.month, self.manufacturing_date.day))
#         return age
#
#     def needs_maintenance(self):
#         return self.maintenance_count >= self.maintenance_interval
#
#     def perform_maintenance(self):
#         self.maintenance_count = 0
#
# class Customer:
#     def __init__(self, name, loyalty_points=0, is_vip=False):
#         self.name = name
#         self.rented_bikes = []
#         self.loyalty_points = loyalty_points
#         self.is_vip = is_vip
#
#     def add_loyalty_points(self, points):
#         self.loyalty_points += points
#
#     def become_vip(self):
#         self.is_vip = True
#
# class Rental:
#     def __init__(self, bike, customer, duration_hours):
#         self.bike = bike
#         self.customer = customer
#         self.duration_hours = duration_hours
#         self.rental_time = datetime.now()
#         self.return_time = None
#
#     def calculate_price(self):
#         total_price = self.duration_hours * self.bike.price_per_hour
#         return total_price
#
#     def get_rental_time(self):
#         return self.rental_time.strftime("%Y-%m-%d %H:%M:%S")
#
#     def return_bike(self):
#         self.return_time = datetime.now()
#
# class BikeShop:
#     def __init__(self, stock):
#         self.stock = {bike_name: Bike(bike_name, bike_info["manufacturer"], bike_info["price_per_hour"],
#                                       bike_info["manufacturing_date"], bike_info.get("maintenance_interval", 100))
#                       for bike_name, bike_info in stock.items()}
#         self.customers = {}
#         self.rented_bikes = []
#         self.returned_bikes = []
#
#     def display_stock(self):
#         table = PrettyTable()
#         table.field_names = ["Bike", "Manufacturer", "Price per Hour", "Manufacturing Date", "Age", "Maintenance Count"]
#
#         for bike_name, bike in self.stock.items():
#             age = bike.calculate_age()
#             table.add_row([bike.name, bike.manufacturer, f"${bike.price_per_hour}",
#                            bike.manufacturing_date.strftime("%Y-%m-%d"), age, bike.maintenance_count])
#
#         print("Available Bikes:")
#         print(table)
#
#     def rent_bike(self, customer_name, bike_name, duration_hours):
#         if bike_name in self.stock:
#             bike = self.stock[bike_name]
#             if customer_name not in self.customers:
#                 self.customers[customer_name] = Customer(customer_name)
#
#             customer = self.customers[customer_name]
#             rental = Rental(bike, customer, duration_hours)
#
#             total_price = rental.calculate_price()
#
#             # Apply VIP discount
#             if customer.is_vip:
#                 total_price *= 0.9
#
#             customer.add_loyalty_points(duration_hours * 2)
#             customer.rented_bikes.append(rental)
#             bike.maintenance_count += duration_hours
#
#             self.rented_bikes.append({
#                 'customer': customer_name,
#                 'bike': bike_name,
#                 'duration': duration_hours,
#                 'total_price': total_price,
#                 'rental_time': rental.get_rental_time(),
#                 'status': 'Rented'
#             })
#
#             print(f'Rental successful!\nTotal Price: ${total_price:.2f}')
#         else:
#             print('Invalid bike name.')
#
#     def return_bike(self, customer_name, bike_name):
#         if customer_name in self.customers and bike_name in self.stock:
#             customer = self.customers[customer_name]
#             for rental in customer.rented_bikes:
#                 if rental.bike.name == bike_name:
#                     rental.return_bike()
#                     customer.rented_bikes.remove(rental)
#                     self.returned_bikes.append({
#                         'customer': customer_name,
#                         'bike': bike_name,
#                         'duration': rental.duration_hours,
#                         'total_price': rental.calculate_price(),
#                         'rental_time': rental.get_rental_time(),
#                         'return_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                     })
#                     print(f'{customer_name} returned {bike_name}.')
#                     return True
#             print(f'{customer_name} did not rent {bike_name}.')
#         else:
#             print('Invalid customer or bike name.')
#         return False
#
#     def perform_maintenance(self, bike_name):
#         if bike_name in self.stock:
#             bike = self.stock[bike_name]
#             if bike.needs_maintenance():
#                 bike.perform_maintenance()
#                 print(f'{bike_name} underwent maintenance.')
#             else:
#                 print(f'{bike_name} does not need maintenance yet.')
#         else:
#             print('Invalid bike name.')
#
#     def display_rental_history(self, status='all'):
#         if status == 'all':
#             rental_list = self.rented_bikes + self.returned_bikes
#         elif status == 'rented':
#             rental_list = self.rented_bikes
#         elif status == 'returned':
#             rental_list = self.returned_bikes
#         else:
#             print('Invalid status. Displaying all rentals.')
#             rental_list = self.rented_bikes + self.returned_bikes
#
#         table = PrettyTable()
#         table.field_names = ["Customer", "Bike", "Duration (hours)", "Total Price", "Rental Time", "Returned Time", "Status"]
#
#         for entry in rental_list:
#             status = 'Rented' if 'status' in entry and entry['status'] == 'Rented' else 'Returned'
#             returned_time = entry.get('return_time', '-')
#             table.add_row([entry["customer"], entry["bike"], entry["duration"], f"${entry["total_price"]:.2f}",
#                            entry["rental_time"], returned_time, status])
#
#         if status == 'rented':
#             print('Rented Bikes:')
#         elif status == 'returned':
#             print('Returned Bikes:')
#         else:
#             print('Rental History (All):')
#         print(table)
#
# # Create the bikeshop object outside the loop
# bike_shop = BikeShop({
#     'Mountain Bike': {'manufacturer': 'Brand A', 'price_per_hour': 10, 'manufacturing_date': datetime(2021, 1, 1)},
#     'Road Bike': {'manufacturer': 'Brand B', 'price_per_hour': 15, 'manufacturing_date': datetime(2020, 5, 1)},
#     'Electric Bike': {'manufacturer': 'Brand C', 'price_per_hour': 20, 'manufacturing_date': datetime(2022, 8, 1)}
# })
#
# while True:
#     print('\nWelcome to the Advanced Bike Shop!')
#     user_choice = input('Choose Your Option:\n'
#                         '1. Display Bikes\n'
#                         '2. Rent a Bike\n'
#                         '3. Return a Bike\n'
#                         '4. Perform Maintenance\n'
#                         '5. View Rental History\n'
#                         '6. View Rented Bikes\n'
#                         '7. View Returned Bikes\n'
#                         '8. Exit\n'
#                         'Your choice: ')
#
#     if user_choice == '1':
#         bike_shop.display_stock()
#     elif user_choice == '2':
#         customer_name = input('Enter Your Name: ')
#         bike_name = input('Enter Bike Name (Mountain Bike/Road Bike/Electric Bike): ')
#         duration_hours = int(input('Enter Rental Duration (in hours): '))
#         bike_shop.rent_bike(customer_name, bike_name, duration_hours)
#     elif user_choice == '3':
#         customer_name = input('Enter Your Name: ')
#         bike_name = input('Enter Bike Name (Mountain Bike/Road Bike/Electric Bike) to return: ')
#         bike_shop.return_bike(customer_name, bike_name)
#     elif user_choice == '4':
#         bike_name = input('Enter Bike Name to perform maintenance: ')
#         bike_shop.perform_maintenance(bike_name)
#     elif user_choice == '5':
#         bike_shop.display_rental_history()
#     elif user_choice == '6':
#         bike_shop.display_rental_history(status='rented')
#     elif user_choice == '7':
#         bike_shop.display_rental_history(status='returned')
#     elif user_choice == '8':
#         print('Thank you for visiting the Advanced Bike Shop!')
#         break
#     else:
#         print('Invalid Option. Please choose again.')




## Single Inheritance
# class Base:
#     def __init__(self):
#         print(" Base Constructor called...")
# class Derived (Base):
#     def __init__(self):
#         print(" Derived Constructor called...")
#         super().__init__()
# d1 = Derived()


## Multi-level Inheritance
# class parent:
#     def __init__(self,*n):
#         print('Parent ',*n)
# class child1(parent):
#     def __init__(self,*n):
#         super().__init__(*n)
#         print('Child 1',*n)
# class child2(child1):
#     def __init__(self,n1,n2=0,n3=0,*n):
#         super().__init__(n1,*n)
#         print('Child 2',n1,n2,n3)
# pr = parent(10,20,30,40,50,60,70,80)
# print()
# c1 = child1(10,20,30,40,50,60)
# print()
# c2 = child2('C2',10,20,30)


## Multiple Inheritance:
# class parent:
#     def __init__(self,n):
#         print('Parent :',n)
# class child1:
#     def __init__(self,n):
#         print('Child_1:',n)
# class child2(parent,child1):
#     def __init__(self,n):
#         # super().__init__(n)
#         parent.__init__(self,n)
#         child1.__init__(self,n)
#         print('Child_2:',n)
# # pr = parent(30)
# # c1 = child1(20)
# c2 = child2(10)


## Hierarchical Inharitance
# class vw:
#     def __init__(self):
#         print('Volkswagen_Top')
# class bently(vw):
#     def __init__(self):
#         super().__init__()
#         print('Bently_2nd')
# class porsche(vw):
#     def __init__(self):
#         super().__init__()
#         print('Porsche_2nd')
# class ducati(porsche):
#     def __init__(self):
#         super().__init__()
#         print('Ducati_3rd')
# class rimac(porsche):
#     def __init__(self):
#         super().__init__()
#         print('Rimac_3rd')
# # t1 = vw()
# # m1 = bently()
# # m2 = porsche()
# # c1 = ducati()
# c2 = rimac()


## Hybrid Inharitance:
# class a11:
#     def __init__(self):
#         print('A1')
# class b11(a11):
#     def __init__(self):
#         super().__init__()
#         print('B1')
# class b12(a11):
#     def __init__(self):
#         super().__init__()
#         print('B2')
# class c11(b11,b12):
#     def __init__(self):
#         b11.__init__(self)
#         b12.__init__(self)
#         print('C1')
# # a1 = a11()
# # b1 = b11()
# # b2 = b12()
# c1 = c11()

# print()
#
# class A11:
#     def __init__(self):
#         print('A1')
#
# class B11(A11):
#     def __init__(self):
#         super().__init__()
#         print('B1')
#
# class B12(A11):
#     def __init__(self):
#         super().__init__()
#         print('B2')
#
# class C11(B11, B12):
#     def __init__(self):
#         super().__init__()  # Use super() to call the constructors of both base classes
#         print('C1')
# # Uncomment the following lines to create instances and test
# # a1 = A11()
# # b1 = B11()
# # b2 = B12()
# c1 = C11()



# Constructor Overloading
# class test:
#     def __init__(self):
#         print('Default 1')
#     def __init__(self,a):
#         self.a = a
#         print('Default 2',a)
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         print('Default 3',a,b)
# t1 = test(10,20)        # always calls last function



## Number Guessing Game:
# import random as rd
# while True:
#     cgen = rd.randint(1,5)
#     ugen = input('Do you want to play (yes/no)? ')
#     ugen = ugen.lower()
#     if Ugen == 'yes':
#         ent = int(input('Choose your number between 1 to 5: \n'))
#         if ent == cgen:
#             print('You Won')
#         elif ent != cgen:
#             print('You Lose')
    # elif ugen == 'no':
#         break
#     else:
#         print('Enter Valid Output')


# n = int(input('Enter Size of Sq.: '))
# for i in range(1,n + 1):
#     for j in range(1,n+1):
#         print('*',end = '  ')
#     print()

# n = int(input('Enter Size:'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print('i',i,end = '  ')
#     print()

# n = int(input('Enter Size:'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print('j',j,end = '  ')
#     print()

# n = int(input("Enter Number:"))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(i,end='  ')
#     print()


# n = int(input('Enter Number: '))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(j,end = '  ')
#     print()


# n = int(input('Enter Number:'))
# k = 1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print('{:2d}'.format(k),end = '  ')
#         k += 1
#     print()


# import pandas as pd
# print(pd.__version__)




# class animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species
#         # print(self.name)
#         # print(self.species)
#
#     def __init__(self,name,species,age):
#         self.name = name
#         self.species = species
#         self.age = age
#         # print(name)
#         # print(self.species)
#         # print(self.age)
#
# # an1 = animal('Dog','Mammal')
# # print(an1.name)
# # print(an1.species)
#
# an1 = animal('Dog','Mammal',15)
# # print(an1)
# print(an1.age)
# print(an1.species)
# print(an1.name)




# class animal:
#     def __init__(self,*args):
#         if len(args) == 1:
#             self.name = args[0]
#         elif len(args) == 2:
#             self.name = args[0]
#             self.species = args[1]
#         elif len(args) == 3:
#             self.name = args[0]
#             self.species = args[1]
#             self.age = args[2]
# an1 = animal('Dog','Mammal',15)
# print(an1.name)
# print(an1.species)
# print(an1.age)



## Operator Overloading:
# class bob:
#     def __init__(self,bal):
#         self.balance = bal
#     def __mul__(self,other):
#         print('Self  :',self.balance)
#         print('Other :',other.balance)
#         print(self.balance,'*',other.balance,'=',self.balance * other.balance)
# srt = bob(1000)
# smd = bob(2000)
# amd = bob(3000)
# n = srt * smd
# m = srt * amd



# class base:
#     def base(self,x):
#         print(self,'->',x.der1)
#
# class derived(base):
#     def __init__(self):
#         self.der1 = 10
#     def show1(self):
#         print(self.der1)
#
# d1 = derived()
# d1.show1()
# d1.base(d1)



# class arith:
#     def cal(self,x,y):
#         print('Plus:            ',x.der1 + y.der2)
#         print('Minus:           ',x.der1 - y.der2)
#         print('Multiplication:  ',x.der1 * y.der2)
#         if y.der2 != 0:
#             print('Division:        ',x.der1 / y.der2)
#         else:
#             print('Division:         Not Defined')
# class maths(arith):
#     def __init__(self):
#         self.der1 = number1
#         self.der2 = number2
#     def show1(self):
#         print('Number_1: ',self.der1,'\nNumber_2: ',self.der2)
#
# number1 = float(input('Enter Number.1: '))
# number2 = float(input('Enter number.2: '))
#
# m1 = m2 = maths()
# m1.show1()
# # m2.show1()
# m1.cal(m1,m2)



# class Student:
#     def __init__(self, name, contact, fees):
#         print("Student Catalogue:")
#         self.name = name
#         self.contact = contact
#         self.fees = fees
#     def showData1(self):
#         print("Name        :", self.name)
#         print("Contact     :", self.contact)
#     def showTotalFees(self):
#         print("Total Fees  :", self.fees)
# class Course(Student):
#     emi = 0
#     def __init__(self, name, contact, fees, course, duration):
#         super().__init__(name, contact, fees)
#         self.course = course
#         self.duration = duration
#     def calcEmi(self):
#         self.emi = self.fees / 10
#     def showData(self):
#         super().showData1()
#         print("Course      :", self.course)
#         print("Duration    :", self.duration)
#         print("Emi         :", self.emi)

# ds = Course("Mayank", 9512691345, 65000, "Data-Science", "8 Months")
# ds.calcEmi()
# ds.showData()
# ds.showTotalFees()




# class Student:
#     def __init__(self, name, contact, fees):
#         print("Student Catalogue:")
#         self.name = name
#         self.contact = contact
#         self.fees = fees
#     def showData1(self):
#         print("Name        :", self.name)
#         print("Contact     :", self.contact)
#     def showTotalFees(self):
#         print("Total Fees  :", self.fees)
# class Course(Student):
#     emi = 0
#     def __init__(self, name, contact, fees, course, duration,score):
#         super().__init__(name, contact, fees)
#         self.course = course
#         self.duration = duration
#         self.score = score
#     def calcEmi(self):
#         self.emi = self.fees / 10
#     def scholer(self):
#         if self.score > 85:
#             self.fees = (self.fees)*0.8
#     def showData(self):
#         super().showData1()
#         print("Course      :", self.course)
#         print("Duration    :", self.duration)
#         print("Emi         :", self.emi)
#         print('Score       :', self.score)
#
# ds = Course("Mayank", 9512691345, 65000, "Data-Science", "8 Months",90)
# ds.calcEmi()
# ds.showData()
# ds.scholer()
# ds.showTotalFees()




# class employee:
#     raised = 1.05
#     def __init__(self,first,last,pay):
#         self.f =first
#         self.l = last
#         self.email = first.lower() + 'dts' + last.lower() + '@gmail.com'
#         self.pay = pay
#     def fullname(self):
#         return f'{self.f} {self.l}'
#     def appliedraise(self):
#         self.pay = int(self.pay * self.raised)
# class developer(employee):
#     # pass
#     raised = 1.1
#
# e1 = employee('Mayank','Solanki',65000)
# e2 = employee('Melech','McAuley',60000)
#
# d1 = developer('Mayank','Solanki',65000)
# # print('Employee :',e1.email)
# # print('Employee :',e2.fullname())
# # print('Developer:',d1.email)
# # print(help(developer))
# print(e1.pay)
# e1.appliedraise()
# print(e1.pay)




# class Student:
#     def __init__(self, name, contact, address):
#         print('Student Details:')
#         self.name = name
#         self.contact = contact
#         self.address = address
#
#     def show_student(self):
#         print('Name         :', self.name)
#         print('Contact      :', self.contact)
#         print('Address      :', self.address)
#
#
# class Job(Student):
#     def __init__(self, name, contact, job_role, address, job_location):
#         super().__init__(name, contact, address)
#         self.job_role = job_role
#         self.job_location = job_location
#
#     def show_job(self):
#         print('Name         :', self.name)
#         print('Contact      :', self.contact)
#         print('Address      :', self.address)
#         print('Job Role     :', self.job_role)
#         print('Job Location :', self.job_location)
#
#
# class Course(Student):
#     def __init__(self, name, contact, address, course_name, fees, duration):
#         super().__init__(name, contact, address)
#         self.course_name = course_name
#         self.fees = fees
#         self.duration = duration
#
#     def show_course(self):
#         print('Name         :', self.name)
#         print('Contact      :', self.contact)
#         print('Address      :', self.address)
#         print('Course Name  :', self.course_name)
#         print('Fees         :', self.fees)
#         print('Duration     :', self.duration)
#
#
# class Study(Course):
#     def __init__(self, name, contact, address, course_name, fees, duration, subjects):
#         super().__init__(name, contact, address, course_name, fees, duration)
#         self.subjects = subjects
#
#     def show_study(self):
#         print('Name         :', self.name)
#         print('Contact      :', self.contact)
#         print('Address      :', self.address)
#         print('Course Name  :', self.course_name)
#         print('Fees         :', self.fees)
#         print('Duration     :', self.duration)
#         print('Subjects     :', self.subjects)
#
# # Example usage:
# st1 = Study('Mayank', 9512691345, 'Surat', 'Data Science', 65000, '8 Months', ['Python', 'SQL'])
# st1.show_study()


# class Employee:
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.email = first.lower() + last.lower() + '@gmail.com'
#         self.pay = pay
#     def fullname(self):
#         return f'{self.first} {self.last}'
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
# class Developer(Employee):
#     raise_amt = 1.1
#     def __init__(self,first,last,pay,prog_lang):
#         super().__init__(first,last,pay)
#         self.prog_lang = prog_lang
# class Manager(Employee):
#     def __init__(self,first,last,pay,employees = None):
#         super().__init__(first,last,pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#     def add_emp(self,emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#     def remove_emp(self,emp):
#         if emp not in self.employees:
#             self.employees.remove(emp)
#     def print_emps(self):
#         for emp in self.employees:
#             print('---->',emp.fullname())
#
#
# dev1 = Developer('Mayank','Solanki',40000,'Python')
# # print(dev1.email)
# # # print(dev1.first)
# # print(dev1.prog_lang)
# dev2 = Developer('Melech','McAuley',35000,'Java')
# # print(dev2.pay)
#
# man1 = Manager('Aston','Martin',60000,[dev1])
# # print(man1.email)
# man1.add_emp(dev2)
# man1.print_emps()




# from tkinter import *
# def calculate():
#     temp = int(entry.get())
#     temp = 1.8 * temp + 32
#     output_label.configure(text = 'Converted: {:.1f}'.format(temp))
#     entry.delete(0,END)
# root = Tk()
# message_label = Label(text='Enter a temperature',
#                       font=('Verdana', 16))
# output_label = Label(font=('Verdana', 16))
# entry = Entry(font=('Verdana', 16), width=4)
# calc_button = Button(text='Ok', font=('Verdana', 16),
#                      command=calculate)
# message_label.grid(row=0, column=0)
# entry.grid(row=0, column=1)
# calc_button.grid(row=0, column=2)
# output_label.grid(row=1, column=0, columnspan=3)
# mainloop()




# Define a function named string_length that takes one argument, str1.
# def string_length(str1):
#     # Initialize a variable called count to 0 to keep track of the string's length.
#     count = 0
#
#     # Iterate through each character in the input string str1.
#     for char in str1:
#         # For each character encountered, increment the count by 1.
#         count += 1
#
#     # Return the final count, which represents the length of the input string.
#     return count
#
# # Call the string_length function with the argument 'w3resource.com' and print the result.
# print(string_length('Mayank'))


# for i in range(5):
#     for j in range(5):
#         print(i,end=' ')
#     print()
# print()
# for i in range(5):
#     for j in range(5):
#         print(j,end=' ')
#     print()
# print()
# for i in range(5):
#     for j in range(5):
#         print(chr(65+j+32),end=' ')
#     print()

# print(chr(97))



# for i in range(5,0,-1):
#     for j in range(1,5+1):
#         print(j,end = '  ')
#     print()

# for i in range(5,0,-1):
    # for j in range(5,0,-1):
    #     print(i,j,end = '  ')
    # print()

# m = 1
# for i in range(1,6):
#     for j in range(1,6):
#         print('{:3d}'.format(m),end=' ')
#         m+=1
#     print()


# m = 1
# for i in range(5):
#     for j in range(5):
#         print('{:3d}'.format(m),end = ' ')
#         m += 2
#     print()


# m=2
# for i in range(5):
#     for j in range(5):
#         print('{:2d}'.format(m),end='  ')
#         m += 2
#     print()



# for i in range(1,6):
#     for j in range(1,6):
#         print('{:2d}'.format(i*j),end='  ')
#     print()



# for i in range(1,6):
#     for j in range(1,4):
#         print(j,i,end=' ')
#     print()



# for i in range(1,6):
    # for j in range(1,4):
    #     print('{} {}'.format(i,j),end=' ')
    # print()




# for i in range(1,6):
#     p = i
#     for j in range(1,6):
#         print('{:2d}'.format(p),end= ' ')
#         p += 5
#     print()

# for i in range(1, 6):
#     for j in range(1, 6):
#         print('{:2d}'.format(i + 5 * (j - 1)), end=' ')
#     print()


# for i in range(5,0,-1):
#     for j in range(6,i,-1):
#         print(i,end = ' ')
#     print()



# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end = ' ')
#     print()



# for i in range(1,6):
#     for j in range(1,i+1):
#         print('{:3d}'.format(j*2),end = '')
#     print()



# x = y = 5,10
# res = x == y
# print(res)


# def func(x,y):
#     return x if y > 0 else y
#
# x = func(5,0) + func(0,-5) + func(2,-3) + func(5,3) + func(5,-2)
# print(x)
# x = none, y = 0



# import numpy as np
# ar1 = np.identity(3)
# print(ar1)
# ar2 = np.eye(2,3)
# print(ar2)



# l = [1,2,3,4,5,6,1,2,3,5,998,6,54]
# lis = []
# for i in l:
#     if i not in lis:
#         lis.append(i)
# print(lis)


# l = [1, 2, 3, 4, 5, 6, 1, 2, 3, 5, 998, 6, 54]
# n = {}
# for num in l:
#     if num in n:
#         n[num] += 1
#     else:
#         n[num] = 1
# print(n)
'''
+-------------------------------+
|                               |
|  Start: Given list            |
|  l = [1, 2, 3, 4, 5, 6, 1,    |
|       2, 3, 5, 998, 6, 54]    |
|                               |
+---------------+---------------+
                |
                v
+-------------------------------+
|                               |
|  Create an empty dictionary:  |
|  count_dict = {}              |
|                               |
+---------------+---------------+
                |
                v
+-------------------------------+
|                               |
|  Iterate through each number  |
|  in the list                  |
|                               |
+---------------+---------------+
                |
                v
+-------------------------------+
|                               |
|  Check if the number is       |
|  already in the dictionary    |
|                               |
+---------------+---------------+
                |
                v
+-------------------------------+
|    +----------------------+   |
|    | Yes                  |   |
|    |                      |   |
|    v                      |   |
|  +------------------------+   |
|  | Increment the count    |   |
|  +------------------------+   |
|                               |
+-------------------------------+
                |
                v
+-------------------------------+
|    +----------------------+   |
|    | No                   |   |
|    |                      |   |
|    v                      |   |
|  +------------------------+   |
|  | Initialize count to 1  |   |
|  +------------------------+   |
|                               |
+---------------+---------------+
                |
                v
+-------------------------------+
|                               |
|  Repeat for each number in    |
|  the list                     |
|                               |
+---------------+---------------+
                |
                v
+-------------------------------+
|                               |
|  Print the final count        |
|  dictionary                   |
|                               |
+---------------+---------------+
                |
                v
+-------------------------------+
|                               |
|  End                          |
|                               |
+-------------------------------+
'''




# numbers = [10, 5, 8, 20, 15, 25]
# n = sorted(numbers)
# print(f'Max = {n[-1]} \nMin = {n[-2]}')


# lst = [1,2,4,5,6.6,9,8,55,1.2,2,4.4,6,2,35,'a','f','h','u']
# lst1 = []
# for number in lst:
#     if isinstance(number,(float,int)):
#         lst1.append(number)
# print(lst1,'\n')
# lst2 = sorted(lst1)
# print(lst2,'\n')
# x = f'1st_Max = {lst2[-1]} \n2nd_Max = {lst2[-2]}'
# print(x)


# lst = [1, 2, 4, 5, 6.6, 9, 8, 55, 1.2, 2, 4.4, 6, 2, 35, 'akl', 'f', 'h', 'ou']
# integers = [number for number in lst if isinstance(number, int)]
# floats = [number for number in lst if isinstance(number, float)]
# characters = [char for char in lst if isinstance(char, str) and len(char) == 1]
#
# print("Integers:", integers)
# print("Floats:", floats)
# print("Characters:", characters)
# ls1 = sorted(integers) + sorted(floats) + sorted(characters,key = lambda x: ord(x))
# ls1 = ls1[-1:0:-1]
# print(set(ls1))



# lst = [1, 2, 4, 5, 6.6, 9, 8, 55, 1.2, 2, 4.4, 6, 2, 35, 'akl', 'f', 'h', 'ou']
# integers = [number for number in lst if isinstance(number, int)]
# floats = [number for number in lst if isinstance(number, float)]
# characters = [char for char in lst if isinstance(char, str) and 1 <= len(char) <= 19]
#
# print("Integers:", integers)
# print("Floats:", floats)
# print("Characters:", characters)
#
# # Concatenate lists, sort, and reverse
# ls1 = sorted(integers) + sorted(floats) + sorted(characters, key=lambda x: ord(x[0]), reverse=True)
#
# # Convert to a set to remove duplicates
# unique_sorted_ls1 = set(ls1)
#
# print("Sorted and Unique List:", unique_sorted_ls1)





# class dog:
#     def bark(self):
#         print('Woff!')
#
# snowy = dog()
# snowy.bark()
# snowy.a = 100
# print(snowy.a)
# snowy.bark()


'''
class dataset:
    def __init__(self):
        self.data = None
    def store_data(self,raw_data):
        self.data = raw_data



class Dataset(object):
    def __init__(self, data=None):
        self.data = data
class MRIDataset(Dataset):
    def __init__(self, data=None, parameters=None):
# here has the same effect as calling
# Dataset.__init__(self)
        super(MRIDataset, self).__init__(data)
        self.parameters = parameters
mri = MRIDataset(data=[1,2,3])
print(mri.parameters)
ds = Dataset(23)
print(ds.data)



class My2Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return My2Vector(self.x+other.x, self.y+other.y)
v1 = My2Vector(1, 2)
v2 = My2Vector(30, 2)
v3 = v1 + v2
print(v3.x , v3.y)

'''




'''

class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,others):
        print(vector(self.x + others.x,self.y + others.y))
vc = vector
v1 = vc(1,2)
v2 = vc(100,200)
v3 = v1 + v2
v2.vc()



class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        result = vector(self.x + other.x, self.y + other.y)
        print(f"x: {result.x}, y: {result.y}")
        # If you don't want to return a new instance, you can return None or any other value
        # return None

# Create instances of the vector class
v1 = vector(88, 66)
v2 = vector(12, 34)
# Add two vectors using the overridden __add__ method



class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adding(self, other):
        result = vector(self.x + other.x, self.y + other.y)
        print(f"x: {result.x}, y: {result.y}")
        # If you don't want to return a new instance, you can return None or any other value
        # return None

# Create instances of the vector class
v1 = vector(88, 66)
v2 = vector(12, 34)
# Add two vectors using the overridden __add__ method
v1.adding(v2)

'''




'''
import pandas as pd

# Mock response structure
mock_response = {
    'MRData': {
        'RaceTable': {
            'Races': [
                {
                    'round': '1',
                    'Circuit': {
                        'circuitId': 'albert_park',
                        'Location': {
                            'country': 'Australia'
                        }
                    },
                    'date': '2020-03-15',
                    'url': 'https://example.com/race1'
                },
                {
                    'round': '2',
                    'Circuit': {
                        'circuitId': 'sepang',
                        'Location': {
                            'country': 'Malaysia'
                        }
                    },
                    'date': '2020-03-22',
                    'url': 'https://example.com/race2'
                },
                {
                    'round': '3',
                    'Circuit': {
                        'circuitId': 'shanghai',
                        'Location': {
                            'country': 'China'
                        }
                    },
                    'date': '2020-04-05',
                    'url': 'https://example.com/race3'
                },
                {
                    'round': '4',
                    'Circuit': {
                        'circuitId': 'barcelona',
                        'Location': {
                            'country': 'Spain'
                        }
                    },
                    'date': '2020-04-19',
                    'url': 'https://example.com/race4'
                },
                {
                    'round': '5',
                    'Circuit': {
                        'circuitId': 'monaco',
                        'Location': {
                            'country': 'Monaco'
                        }
                    },
                    'date': '2020-05-03',
                    'url': 'https://example.com/race5'
                },
                {
                    'round': '6',
                    'Circuit': {
                        'circuitId': 'montreal',
                        'Location': {
                            'country': 'Canada'
                        }
                    },
                    'date': '2020-05-17',
                    'url': 'https://example.com/race6'
                },
                {
                    'round': '7',
                    'Circuit': {
                        'circuitId': 'silverstone',
                        'Location': {
                            'country': 'United Kingdom'
                        }
                    },
                    'date': '2020-05-31',
                    'url': 'https://example.com/race7'
                },
                {
                    'round': '8',
                    'Circuit': {
                        'circuitId': 'hockenheim',
                        'Location': {
                            'country': 'Germany'
                        }
                    },
                    'date': '2020-06-14',
                    'url': 'https://example.com/race8'
                },
                {
                    'round': '9',
                    'Circuit': {
                        'circuitId': 'hungaroring',
                        'Location': {
                            'country': 'Hungary'
                        }
                    },
                    'date': '2020-06-28',
                    'url': 'https://example.com/race9'
                },
                {
                    'round': '10',
                    'Circuit': {
                        'circuitId': 'spa',
                        'Location': {
                            'country': 'Belgium'
                        }
                    },
                    'date': '2020-08-30',
                    'url': 'https://example.com/race10'
                },
                # Add more races as needed
            ]
        }
    }
}

# Process the mock response
races = {'round': [],
         'circuit_id': [],
         'country': [],
         'date': [],
         'url': []}

try:
    for item in mock_response['MRData']['RaceTable']['Races']:
        races['round'].append(int(item.get('round', None)))
        races['circuit_id'].append(item['Circuit'].get('circuitId', None))
        races['country'].append(item['Circuit']['Location'].get('country', None))
        races['date'].append(item.get('date', None))
        races['url'].append(item.get('url', None))

except Exception as e:
    print(f"Error processing mock response: {e}")

# Create DataFrame
races_df = pd.DataFrame(races)
print(races_df)
'''



# import COVID19Py
# covid19 = COVID19Py.COVID19()
# data = covid19.getAll(timelines=True)
# virusdata = dict(data['latest'])
# names = list(virusdata.keys())
# values = list(virusdata.values())
# print(virusdata)



# simple interest
'''
simple interest(quarterly) = (p*(r/4)*t)/100
'''
# def si(p,r,t):
#     interest = (p*(r/4)*t)/100
#     # print(interest)
#     total_amt = p + interest
#     return f'\nInterest     : ₹{interest}\nTotal Amount :₹{total_amt} '
#
# p = float(input('Enter Principal   : '))
# r = float(input('Enter Rate in %.  : '))
# t = float(input('Enter time in yrs.: '))
#
# x = si(p,r,t)
# print(x)




# FD interest
'''
FDI = p*(1 + r*0.01/n)**(n*t)
'''
# def fdi(p,r,n,t):
#     amount = p*(1 + r*0.01/n)**(n*t)
#     interest = amount - p
#     return f'\nFD Interest : ₹{interest:.2f}'
#
# p = float(input('Enter Principal    : '))
# r = float(input('Enter Rate in %.   : '))
# n   = int(input('Enter n (duration) : '))
# t = float(input('Enter time in yrs. : '))
#
# f1 = fdi(p,r,n,t)
# print(f1)




# Recurring interest
'''
M = R x {(1 + n) x n – 1} / 1- (1 + i) (-1/3)
'''
# def recur(r,n,i,t):
#     # amt = r*((1+n)*n-1)/(1-(1+i)*(-1/3))
#     interest = r * (((1 + (n * i))**(4 * t)) - 1) / (i * (1 + (n * i))**(4 * t))
#     return f'Interest = {interest}\nAMT = ₹{r + interest}'
#
# r = float(input('Enter Principal    : '))
# n = float(input('Quarters   : '))
# i = float(input('Rate: '))
# t = float(input('Enter time in yrs. : '))

# r1 = recur(p,r,n,t)
# r1 = recur(r,i/400,n,t)
# print(r1)




# EMI
'''
EMI = p*(r*(1+r)**n)/((1+r)**n-1)
monthly rate = r/0.12
total payments = t*12
'''
# def emi(p,r,t):
#     mrate = r/(12*100)
#     totalpay = t*12
#     EMI = p*(mrate*(1+mrate)**totalpay)/((1+mrate)**totalpay-1)
#     return f'\nEMI : ₹{EMI:.2f}'
#
# p = float(input('Enter Principal   : '))
# r = float(input('Enter Rate in %.  : '))
# t = float(input('Enter time in yrs.: '))
#
# e1 = emi(p,r,t)
# print(e1)




# for i in range(1,108+1):
#     print(i,'Jai Shree Ram')


# class icici:
#     def __init__(self,name,age,contact,accbal,saving_acc_number):
#         self.name = name
#         self.age = age
#         self.contact = contact
#         self.saving_acc_bal = accbal
#         self.saving_acc_number = saving_acc_number
#     def accdetails(self):
#         print('\nHERE\'S YOUR CURRENT STATUS')
#         print(f'Name: {self.name}\nAge: {self.age}\n'
#               f'Contact No.: {self.contact}\nPrevious Balance: {self.saving_acc_bal}/- ₹\n'
#               f'Current Balance: {self.saving_acc_bal}/- ₹')
#     def get_saving_acc_balance(self):
#         return self.saving_acc_bal
#     def set_saving_acc_balance(self,bal):
#         self.saving_acc_bal = bal
# class saving(icici):
#     def __init__(self,name,age,contact,accbal,saving_acc_number):
#         super().__init__(name,age,contact,accbal,saving_acc_number)
#     def withdraw(self,withamt):
#         self.withamt = withamt
#         self.accBal = super().get_saving_acc_balance()
#         if self.accBal >= self.withamt:
#             self.accBal -= self.withamt
#             super().set_saving_acc_balance(self.accBal)
#         else:
#             print('No Enough Money')
#     def deposit(self,depoamt):
#         self.accBal += depoamt
#         print('Depoamt:',self.accBal)
# class customer(saving):
#     def __init__(self,name,age,contact,accbal,saving_acc_number,address):
#         super().__init__(name,age,contact,accbal,saving_acc_number)
#         self.address = address
#     def withdraw_amt(self,bal):
#         super().withdwar(bal)
#     def deposit_amt(self,bal):
#         super().deposit(bal)
#
# cus2 = customer('Melech',23,6979298428,100000,'Israel','is1234')
# cus2.accdetails()
# cus2.set_saving_acc_balance(20000)
# cs = cus2.get_saving_acc_balance()
# cus2.accdetails()
# print(cs)



# import numpy as np
# a = np.full((3,5,4),7)
# print(a)

# b = np.zeros((3,3))
# print(b)

# c = np.ones((2,3,4,2))
# print(c)

# a = np.empty((4,4))
# print(a)

# b = np.random.random((2,3))
# print(b)


# c = np.linspace(0,100,11)
# print(c)



# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d
# ax = plt.axes( projection = '3d' )
# a1 = plt.show()
# print(a1)
# z = np.linspace( 0 , 20 , 100 )
# x = np.sin(z)
# y = np.cos(z)
# ax1 = plt.axes( projection = '3d' )
# ax1.plot3D(x,y,z)
# plt.show()


# ax = plt.axes( projection = '3d' )
# def z_function(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2 ))
# x = np.linspace(- 5 , 5 , 50 )
# y = np.linspace(- 5 , 5 , 50 )
#
# X, Y = np.meshgrid(x,y)
# Z = z_function(X,Y)
# ax.plot_surface(X,Y,Z)
# plt.show()


# import pandas as pd
# series = pd.Series([ 10 , 20 , 30 , 40 ],
#                    [ 'A' , 'B' , 'C' , 'D' ])
# print(series)
# print (series[ 'C' ])
# print (series[ 1 ])




# class icici:
#     loan_amt = 0
#
#     def __init__(self, name, age, contact, accbal, saving_acc_number):
#         self.name = name
#         self.age = age
#         self.contact = contact
#         self.saving_acc_bal = accbal
#         self.saving_acc_number = saving_acc_number
#
#     def accdetails(self):
#         print('\nHERE\'S YOUR CURRENT STATUS')
#         print(f'Name: {self.name}\nAge: {self.age}\n'
#               f'Contact No.: {self.contact}\nPrevious Balance: {self.saving_acc_bal}/- ₹\n'
#               f'Current Balance: {self.saving_acc_bal}/- ₹')
#
#     def get_saving_acc_balance(self):
#         return self.saving_acc_bal
#
#     def set_saving_acc_balance(self, bal):
#         self.saving_acc_bal = bal
#
#     def get_loan_acc_balance(self):
#         return self.loan_amt
#
#     def set_loan_acc_balance(self, bal):
#         self.loan_amt = bal
#
# class saving(icici):
#     def __init__(self, name, age, contact, accbal, saving_acc_number):
#         super().__init__(name, age, contact, accbal, saving_acc_number)
#
#     def withdraw(self, withamt):
#         acc_bal = super().get_saving_acc_balance()
#         if acc_bal >= withamt:
#             acc_bal -= withamt
#             super().set_saving_acc_balance(acc_bal)
#             print(f'Withdrawal successful. Updated balance: {super().get_saving_acc_balance()}/- ₹')
#         else:
#             print('Insufficient Balance')
#
#     def deposit(self, depoamt):
#         acc_bal = super().get_saving_acc_balance()
#         acc_bal += depoamt
#         super().set_saving_acc_balance(acc_bal)
#         print(f'Deposit successful. Updated balance: {acc_bal}/- ₹')
#
#     def showbalance(self):
#         print(f'Saving Acc Balance: {super().get_saving_acc_balance()}/- ₹')
#
# class loan(icici):
#     def approved_loan(self, loan_amt):
#         current_loan = super().get_loan_acc_balance()
#         new_loan = current_loan + loan_amt
#         super().set_loan_acc_balance(new_loan)
#         print(f'Loan approved. Updated loan balance: {super().get_loan_acc_balance()}/- ₹')
#
#     def pay_loan(self, payment_amt):
#         current_loan = super().get_loan_acc_balance()
#         if current_loan > 0 and payment_amt <= current_loan:
#             new_loan = current_loan - payment_amt
#             super().set_loan_acc_balance(new_loan)
#             print(f'Loan payment successful. Updated loan balance: {super().get_loan_acc_balance()}/- ₹')
#         elif current_loan == 0:
#             print('No outstanding loan.')
#         else:
#             print('Invalid payment amount. Cannot exceed the outstanding loan balance.')
#
#     def showloanbalance(self):
#         print(f'Loan Balance: {super().get_loan_acc_balance()}/- ₹')
#
# class customer(saving, loan):
#     def __init__(self, name, age, contact, accbal, address, saving_acc_number):
#         super().__init__(name, age, contact, accbal, saving_acc_number)
#         self.address = address
#
#     def withdraw_amt(self, bal):
#         super().withdraw(bal)
#
#     def deposit_amt(self, bal):
#         super().deposit(bal)
#
#     def apply_for_loan(self, loan_amt):
#         super().approved_loan(loan_amt)
#
#     def pay_loan_amt(self, payment_amt):
#         super().pay_loan(payment_amt)
#
#
# # Creating a customer with initial details
# customer1 = customer(name="John Doe", age=30, contact="1234567890",
# accbal=5000, address="123 Main Street", saving_acc_number="S12345")
#
# # Displaying initial account details
# customer1.accdetails()
#
# # Applying for a loan of 2000
# customer1.apply_for_loan(2000)
#
# # Displaying loan balance after loan approval
# customer1.showloanbalance()
#
# # Making a loan payment of 1000
# customer1.pay_loan_amt(1000)
#
# # Displaying loan balance after payment
# customer1.showloanbalance()




# import math
# x = math.factorial(5)
# print(x)
# x = math.lcm(4,5,7,8,55)
# print(x)




# import turtle as trt
# a = trt.Screen()
# a.setup(500,500)


# # print('Enter 1st Number: ')
# x = int(input('Enter 1st Number: '))
# # print('Enter 2nd Number: ')
# # print(end='     ')
# y = int(input('Enter 2nd Number: '))
# # print(x,y,sep = ' hehehehe ')
# print(x+y)




# pi = 3.14
#
# while True:
#     r = float(input('Enter Radius (or type "exit" to end): '))
#
#     if r == 'exit':
#         break
#
#     area = pi * r**2
#     print('Area Of Circle is:', area)
#



# r = float(input('Enter Radius: '))
# pi = 3.14
# print('Area Of Circle is:',pi*r**2)




# x = '123456789'
# print(type(x))
# for i in x:
#     print(i,'hello')
# print(len(x))




# variable = 'Hello World'
# print(variable)
# print(variable.capitalize())
# print(variable.lower())
# print(variable.upper())
# print(variable.center(20,'*'))
# print(variable.count('l'))
# print(variable.index('e'))
# print(variable.replace('o','x'))
# print(variable.find('o'))
# print('31/01/2022'.replace('/','-'))

# var = '31/01/2022'.split('/')
# print(var,'\n')
# print(type(var))

# numbers = 'ab123456789'
# print(numbers.isalnum())
# print(numbers.isnumeric())
# print(numbers.islower())
# print(numbers.isupper())




# set1 = {5,'Hello',3.2}
# print(type(set1))
# print(set1)
# set1.add(2)
# set1.discard(3.2)
# set1.remove(2)
# set1.pop()
# set1.add(1)
# print(set1)
# x = set1.intersection({2,5})
# print(x)
# x = set1.difference({2,5})
# print(x)
# x = set1.issubset({2,5,3,4,5,6,8,'Hello',3.2,1})
# print(x)
# x = set1.issuperset({2,5})
# print(x)
# x = set1.isdisjoint({12,15})
# print(x)
# x = set1.union({211,511})




# # Create a list of friends
# friends_list = ["Alice", "Bob", "Charlie", "David", "Emma"]
#
# # Get user input
# user_choice = input("Do you want to print names in ALL CAPS? (yes/no): ").lower()
#
# # Check user choice and print names accordingly
# if user_choice == "yes":
#     for friend in friends_list:
#         print(friend.upper() + "!")
# else:
#     for friend in friends_list:
#         print(friend.lower())




# stuff = list()
# stuff.append('python')
# stuff.append('chuck')
# stuff.sort()
# print (stuff[0])
# print (stuff.__getitem__(0))
# print (list.__getitem__(stuff,0))
#
# print (stuff.__getitem__(0))




# x = 5
# while x>0:
#     print(x,'Hello')
#     x -= 1



# x = 1
# while x<=10:
#     print(x)
#     x += 1



# x = int(input('Enter 1st Number: '))
# y = int(input('Enter 2nd Number: '))
# z = int(input('Enter 3rd number: '))
#
# if x>y and x>z:
#     print(x,'is greater')
# elif y>x and y>z:
#     print(y,'is greater')
# else :
#     print(z,'is greater')



# x = 'mayank'
# print(x[::-1])



# t = (2,4,5,1,3,6,8,55)
# print(t[1])
# print(len(t))
# x = len(t) - 1          # len(t) = 8
# print(t[::-1])
# while x >= 0:
#     print(t[x])
#     x -= 1
# y = 0
# while y < len(t):
#     print(t[y])
#     y += 1




# numbers = [10, 25, 7, 15, 30, 5]
# # print(len(numbers))
# # print(sum(numbers))
# numbers.append(20)
# # print(numbers)
# numbers.remove(7)
# print(numbers)
# x = int(input('Enter NUmber to check: '))
# if x in numbers:
#     print('Present')
# else:
#     print('Not Present')
# double_numbers = [num * 2 for num in numbers]
# print(double_numbers)
# doubled_numbers = []
# for num in numbers:
#     x = num*2
#     doubled_numbers.append(x)
# print(doubled_numbers)



# list_comprehension
'''
new_list = [expression for element in iterable if condition]
'''

# original_numbers = [1, 2, 3, 4, 5]
# on = [x**2 for x in original_numbers]
# print(on)


# numbers = [10, 15, 20, 25, 30]
# even = [x for x in numbers if x % 2 == 0]
# print(even)


# words = ["apple", "banana", "cherry", "date"]
# uc = [word.upper() for word in words ]
# print(uc)


# words = ["cat", "elephant", "dog", "giraffe"]
# length = [len(word) for word in words]
# print(length)


# newlist = [ x for x in range(0,20+1) if x % 3 == 0]
# print(newlist)


# numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
# num = [ nums**2 for nums in numbers if nums > 0 and nums % 2 == 0 ]
# print(num)


# words = ["hello", "world", "python", "exercise"]
# prnt = [ sum( 1 for char in word if char.lower() in 'aeiou') for word in words ]
# print(prnt)



# def temp(temp_cel):
#     k = temp_cel + 273.15
#     f = (9/5) * temp_cel + 32
#     return f'''\nCelsius to Kelvin  : {k} K
# Celsius to Fahrenheit : {f} °F'''
#
# temp_cel = float(input('Enter Temperature in Celsius: '))
# print(temp(temp_cel))



'''
To convert from kPa to psi: Pressure in psi = Pressure in kPa × 0.14503773773
To convert from kPa to mmHg: Pressure in mmHg = Pressure in kPa × 7.50062
To convert from kPa to atm: Pressure in atm = Pressure in kPa × 0.00986923
'''
# def pressure(kpa):
#     psi = round(kpa * 0.14503773773,3)
#     mmhg = round(kpa * 7.50062,3)
#     atm = round(kpa * 0.00986923,3)
#     return psi,mmhg,atm
#
# kpa = float(input('Enter Pressure in kPa: '))
#
# psi,mmhg,atm = pressure(kpa)
#
# print(f'\nEquivalent Pressure:\n'
#       f'In pounds per square inch (psi)..: {psi:.3f}\n'
#       f'In millimeters of mercury (mmHg).: {mmhg:.3f}\n'
#       f'In atmospheres (atm).............: {atm:.3f}')



'''
Sum of the Digits in an Integer
'''
# number = int(input('Enter a four-digit integer: '))
# digit_sum = sum(int(digit) for digit in str(number))
# print(f'Sum of digits in {number}: {digit_sum}')

# x = '444'
# y = int(x)
# print(sum(int(digit) for digit in x))


# number = int(input('Enter Number: '))
# revnum = int(str(number)[::-1])
# print(revnum)
# print(int(str(number)[::-1]))


# number = int(input('Enter NUmber: '))
# ispali = str(number) == str(number)[::-1]
# print(ispali)



# number = int(input('Enter NUmber: '))
# avg = sum(int(digit) for digit in str(number))/len(str(number))
# print(avg)



# number = int(input('Enter Positive Number: '))
# evens = sum(1 for digit in str(number) if int(digit) % 2 == 0)
# odds = len(str(number)) - evens
# print(f'Number of even digits: {evens}\nNumber of odd digits: {odds}')



# p = 1234
# c = 0
# while c!= 3:
#     c += 1
#     pin = int(input('Enter Pin: '))
#     if pin == p:
#         print('Transaction Successful')
#         break
#     else:
#         print('Incorrect Pin')
# else:
#     print('Card Blocked')



# p = 1234
# max = 3
# for i in range(max):
#     pin = int(input('Enter Pin: '))
#     if pin == p:
#         print('Correct Pin')
#         break
#     else:
#         print('Incorrect Pin')
# else:
#     print('Card Blocked')






# d1  = {41:'Amit', 81:'Ajay','age':18,'Weight':50}
# for i in d1:
    # print(i)                  # Prints Keys only
    # print(d1[i])              # Prints Values only
    # print(i,d1[i],sep = ':')  # Prints both keys and values
    # print(f'{i:<7}:{d1[i]}')  # Prints both keys and values with formation




# def fun1():
#     print('Hello Bharat')
#     print('Hello Gujarat')
# fun1()            # prints fun1
# print(fun1())     # prints fun1 + None




# def fun1():
#     print('Mayank Solanki')
#     print('Melech McAuley')
# print('Pehle Bahar Wala Print Hoga')
# fun1()




# def add():
#     x = eval(input('Enter 1st Number: '))
#     y = eval(input('Enter 2nd Number: '))
#     print(type(x))
#     print(type(y))
#     return f'Addition of {x},{y} is {x + y}'
# print(add())




# def add(a,b):                   # Arguments(parameters)_passing or Formal_parameter
#     z = a + b                   # z_can_only_be_used_within_this_function_until_you_return_it
#     # print(f'{a} + {b} = {z}')
#     return f'{a} + {b} = {z}'   # To_get_z_use(print(add(a,b))
# x = eval(input('Enter 1st Number: '))
# y = eval(input('Enter 2nd Number: '))
# # add(x,y)                        # Actual_parameter      # Functional Calling
# print(add(x,y))                 # Only_use_when_you_do_return




# def fun2(*m):
#     # print(*m)   # prints numbers
#     print(m)    # prints in the form of tuple
#     h = sum(m)
#     length = len(m)
#     print('Sum of all Numbers   : ',h)
#     print('Count of all Numbers : ',length)
#     print('Average :',h/length)
#
# fun2(*(eval(input('Enter Numbers :'))))




# for i in range(1,5+1):          # A = 1,2,3,4,5
#     print('\n',i,'A')
#     for j in range(6,8+1):      # B = 6,7,8
#         print(i,j,'B')
# print('\nDone')




# for i in range(1,6):
#     print('A',end = ' ')
#     for j in range(1,4):
#         print('B',end = '')
#     print(' ')




# for i in range(5):
#     for j in range(5):
#         print(i,'*',j,end = '   ')
#     print()




# m = 1
# for i in range(1,6):
#     for j in range(m):
#         print('*',end = ' ')
#     m += 1
#     print()




# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print('*',end = ' ')
#         else :
#             pass
#     print()




# for i in range(1,6):
#     for j in range(1,6):
#         if j + 1 <= i:
#             print(' ',end = ' ')
#         else:
#             print('*',end = ' ')
#     print()




# for i in range(1,5):
#     for j in range(1,i+4):
#         if (j >= 5 - i) and (j <= 3 + i):
#             print(i,end = ' ')
#         else :
#             print(' ',end = ' ')
#     print()




# x = eval(input('Enter Number: '))
# for i in range(2,x):
#     if x % i == 0:
#         print('Not Prime')
#         break
# else :
#     print('Prime')



# x = eval(input('Enter Number: '))
# result = 'Not Prime' if any(x % i == 0 for i in range(2,x)) else 'Prime'
# print(result)


# x = eval(input('Enter Number: '))
# result = 'Prime' if all(x % i != 0 for i in range(2, x)) else 'Not Prime'
# print(result)



# x = eval(input('Enter Number: '))
# def check_prime_all(x):
#     return 'Prime' if all(x % i != 0 for i in range(2, x)) else 'Not Prime'
#
# def check_prime_any(x):
#     return 'Prime' if any(x % i == 0 for i in range(2, x)) else 'Not Prime'
#
# print("| Number | all() Result | any() Result |")
# print("| ------ | ------------ | ------------ |")
#
# for num in range(2, x + 1):
#     result_all = check_prime_all(num)
#     result_any = check_prime_any(num)
#     print(f"| {num:6} | {result_all:12} | {result_any:12} |")





# import threading
# print(threading.current_thread())
# print(threading.current_thread().name)
# print(threading.current_thread().ident)
# print(threading.current_thread().is_alive())




# from threading import Thread,current_thread
# def display(n,msg):
#     print(current_thread())
#     for i in range(n):
#         print(msg)
# t1 = Thread(target = display,kwargs ={'n':4 , 'msg' : 'Hello!'})
# t1.start()
# for i in range(4):
#     print('Welcome!')
# print(current_thread())




# s1 = eval(input('Start : '))
# s2 = eval(input('End : '))
# y = []
# for x in range(s1,s2):
#     for i in range(2,x):
#         if x % i == 0:
#             break
#     else:
#         y.append(x)
# print(y)
# print(len(y))
# a1 = (y[len(y)//2-1:len(y)//2:])
# a2 = (y[len(y)//2:len(y)//2-1:-1])
# a = sum(a1 + a2)
# print(a)




# l = list('1234')
# l[0] = l[1] = 5
# print(l)



# number = int(input('Enter a four-digit integer: '))
# digit_sum = sum(int(digit) for digit in str(number))
# print(f'Sum of digits in {number}: {digit_sum}')

# x = '444'
# y = int(x)
# print(sum(int(digit) for digit in x))



# number = int(input('Enter Number: '))
# digitsum = sum(int(digit) for digit in str(number))
# print(digitsum)




'''Sort 3 Integers'''
# n1 = eval(input('Enter 1st Number: '))
# n2 = eval(input('Enter 2nd Number: '))
# n3 = eval(input('Enter 3rd Number: '))
# l1 = [n1,n2,n3]
# lmax = max(l1)
# lmin = min(l1)
# lnn = sum(l1) - lmax - lmin
# print(f'\nMaximum : {lmax}\nMiddle  : {lnn}\nMinimum : {lmin}' )




# n1 = eval(input('Enter 1st Number: '))
# even_odd = 'Even' if n1 % 2 == 0 else 'Odd'
# print(even_odd)




'''Sound Levels'''
# def noise(ns):
#     if ns == 130:
#         print('It\'s Jackhammer')
#     elif 130 < ns:
#         print('Higher than Jackhammer')
#     elif ns == 106:
#         print('It\'s Gas Lawnmower')
#     elif 106 < ns < 130:
#         print('Between Gas Lawnmower and Jackhammer')
#     elif ns == 70:
#         print('It\'s Alarm Clock')
#     elif 70 < ns < 106:
#         print('Between Alarm clock and Gas Lawnmower')
#     elif ns == 40:
#         print('It\'s Quiet room')
#     elif 40 < ns < 70:
#         print('Between Quiet room and Alarm clock')
#     elif ns < 40:
#         print('Less than Quiet room')
#
# ns = eval(input('Enter Decibel Level(db): '))
# noise(ns)




# from time import sleep
# # from threading import Thread
# class A():
#     def run(self):
#         for i in range(5):
#             print('Mayank')
#             sleep(1)
# class B():
#     def run(self):
#         for i in range(5):
#             print('Solanki')
#             sleep(1)
# t1 = A()
# t2 = B()
# t1.run()
# t2.run()




# from time import sleep
# from threading import Thread
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print('Mayank')
#             sleep(1)
# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print('Solanki')
#             sleep(1)
# class C(Thread):
#     def run(self):
#         for i in range(5):
#             print('House')
#             sleep(1)
# t1 = A()
# t2 = B()
# t3 = C()
# t1.start()
# t2.start()
# t3.start()




# # from time import sleep
# from threading import Thread
# class c1(Thread):
#     def run(self):
#         for i in range(5):
#             print('Mayank',i)
#             # sleep(1)
# class c2(Thread):
#     def run(self):
#         for i in range(5):
#             print('Solanki',chr(65 + i))
#             # sleep(1)
# class c3(Thread):
#     def run(self):
#         for i in range(5):
#             print('House',chr(97 + i))
#             # sleep(1)
# t1 = c1()
# t2 = c2()
# t3 = c3()
# print('-1)---------- Project_-1 ----------(-1)')
# t1.start()  # Mayank
# t2.start()  # Solanki
# t3.start()  # House
# print('0---------- Project_0 ----------0')         # Zero
# t1.join()   # Mayank (0-4)
# print('1---------- Project_1 ----------1')         # One
# t2.join()   # Solanki (A-E)
# print('2---------- Project_2 ----------2')         # Two
# t3.join()   # House (a-e)
# print('3---------- Project_3 ----------3')         # Three





# from threading import Thread, active_count, current_thread
# from time import sleep
#
# def square(number):
#     for i in range(1, number + 1):
#         print(f"Square: {i,i*i}")
#         sleep(1)
#
# def cube(number):
#     for i in range(1, number + 1):
#         print(f"Cube: {i,i*i*i}")
#         sleep(1)
#
# def sqrt(number):
#     for i in range(1,number + 1):
#         print(f'Square Root: {i,i**(1/2)}')
#         sleep(1)
#
# # startTime = time.time()
#
# sq = Thread(target=square, args=(5,))
# cu = Thread(target=cube, args=(5,))
# sr = Thread(target=sqrt, args=(5,))
#
# sq.start()
# cu.start()
# sr.start()
#
# print(f"----Current Active Thread: {active_count()}----upar vaalu")
# # print(f"----Thread identity: {current_thread().ident}----upar vaalu")
# # print(f"----Thread identity sq: {sq.ident}----")
# # print(f"----Thread identity cu: {cu.ident}----")
# # print(f"----Thread identity sqrt: {sr.ident}----")
#
# sq.join()
# cu.join()
# sr.join()
#
# # print(f"----Thread identity: {current_thread().ident}----niche vaalu")
# # print(f"----Thread identity sq: {sq.ident}----")
# # print(f"----Thread identity cu: {cu.ident}----")
# # print(f"----Thread identity sqrt: {sr.ident}----")
# print(f"----Current Active Thread: {active_count()}----niche vaalu")




# p = eval(input('Enter Start: '))
# q = eval(input('Enter End: '))
# lst = []
# for i in range(p,q+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else :
#         print(i,end = ' ')
#         lst.append(i)
# print()

# length = len(lst)
# mid = length//2
# print(lst[mid] + lst[mid - 1])



# import calendar
# print(calendar.calendar(2024))



# num = int(input('Enter Number: '))
# num = str(num)
# if num == num[::-1]:
#     print('Palindrom')
# else:
#     print('Not Palindrom')



# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.cm as cm
#
# # Make an array with ones in the shape of an 'X'
# a = np.eye(10,10)
# a += a[::-1,:]
#
# fig = plt.figure()
# ax1 = fig.add_subplot(121)
# # Bilinear interpolation - this will look blurry
# ax1.imshow(a, interpolation='bilinear', cmap=cm.Greys_r)
#
# ax2 = fig.add_subplot(122)
# # 'nearest' interpolation - faithful but blocky
# ax2.imshow(a, interpolation='nearest', cmap=cm.Greys_r)
#
# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 10)
#
# fig = plt.figure()
# plt.plot(x, np.sin(x), '-')
# plt.plot(x, np.cos(x), '--')
# plt.show()



# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Generate sample data
# np.random.seed(42)
# n_points = 100
# x = np.linspace(0, 10, n_points)
# y = np.linspace(0, 10, n_points)
# x, y = np.meshgrid(x, y)
# z = np.sin(np.sqrt(x**2 + y**2))
#
# # Create a pandas DataFrame
# df = pd.DataFrame({'X': x.flatten(), 'Y': y.flatten(), 'Z': z.flatten()})
#
# # Create a 3D plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(df['X'], df['Y'], df['Z'], c='r', marker='o')
#
# # Customize plot
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('3D Scatter Plot')
#
# plt.show()




# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Generate sample data for a surface plot
# np.random.seed(42)
# n_points = 100
# x = np.linspace(-5, 5, n_points)
# y = np.linspace(-5, 5, n_points)
# x, y = np.meshgrid(x, y)
# z = np.sin(np.sqrt(x**2 + y**2))
#
# # Create a pandas DataFrame
# df = pd.DataFrame({'X': x.flatten(), 'Y': y.flatten(), 'Z': z.flatten()})
#
# # Reshape data for surface plot
# x = df['X'].values.reshape((n_points, n_points))
# y = df['Y'].values.reshape((n_points, n_points))
# z = df['Z'].values.reshape((n_points, n_points))
#
# # Create a 3D surface plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, cmap='viridis')
#
# # Customize plot
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('3D Surface Plot')
#
# plt.show()




# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Generate sample data for a parametric surface plot
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, np.pi, 50)
# u, v = np.meshgrid(u, v)
#
# # Parametric equations for the surface
# x = u * np.cos(v)
# y = u * np.sin(v)
# z = u**2
#
# # Create a pandas DataFrame
# df = pd.DataFrame({'U': u.flatten(), 'V': v.flatten(), 'X': x.flatten(), 'Y': y.flatten(), 'Z': z.flatten()})
#
# # Reshape data for surface plot
# u = df['U'].values.reshape((50, 100))
# v = df['V'].values.reshape((50, 100))
# x = df['X'].values.reshape((50, 100))
# y = df['Y'].values.reshape((50, 100))
# z = df['Z'].values.reshape((50, 100))
#
# # Create a 3D surface plot
# fig = plt.figure(figsize=(12, 10))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k')
#
# # Customize plot
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('3D Parametric Surface Plot')
#
# plt.show()





# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from scipy.integrate import solve_ivp
#
# # Define the Lorenz system of differential equations
# def lorenz(t, y, sigma, rho, beta):
#     dydt = np.zeros_like(y)
#     dydt[0] = sigma * (y[1] - y[0])
#     dydt[1] = y[0] * (rho - y[2]) - y[1]
#     dydt[2] = y[0] * y[1] - beta * y[2]
#     return dydt
#
# # Set parameters for the Lorenz system
# sigma = 10
# rho = 28
# beta = 8 / 3
#
# # Solve the Lorenz system using scipy's solve_ivp
# initial_conditions = [1, 0, 20]
# sol = solve_ivp(lorenz, (0, 25), initial_conditions, args=(sigma, rho, beta), dense_output=True)
#
# # Generate data from the solution
# t = np.linspace(0, 25, 10000)
# y = sol.sol(t)
#
# # Create a pandas DataFrame
# df = pd.DataFrame({'T': t, 'X': y[0], 'Y': y[1], 'Z': y[2]})
#
# # Create a 3D plot of the Lorenz attractor
# fig = plt.figure(figsize=(12, 10))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(df['X'], df['Y'], df['Z'], lw=0.5)
#
# # Customize plot
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('Lorenz Attractor')
#
# plt.show()



##----------------------------- 4D Flower -----------------------------##
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Generate sample data for a nebula-like shape
# theta = np.linspace(0, 4 * np.pi, 1000)
# phi = np.linspace(0, 2 * np.pi, 100)
# theta, phi = np.meshgrid(theta, phi)
#
# # Parametric equations for the nebula-like shape
# r = 5 + 3 * np.sin(7 * theta) * np.cos(5 * phi)
# x = r * np.sin(theta) * np.cos(phi)
# y = r * np.sin(theta) * np.sin(phi)
# z = r * np.cos(theta)
#
# # Create a pandas DataFrame
# df = pd.DataFrame({'Theta': theta.flatten(), 'Phi': phi.flatten(), 'X': x.flatten(), 'Y': y.flatten(), 'Z': z.flatten()})
#
# # Reshape data for surface plot
# theta = df['Theta'].values.reshape((100, 1000))
# phi = df['Phi'].values.reshape((100, 1000))
# x = df['X'].values.reshape((100, 1000))
# y = df['Y'].values.reshape((100, 1000))
# z = df['Z'].values.reshape((100, 1000))
#
# # Create a 3D surface plot of the nebula-like shape
# fig = plt.figure(figsize=(12, 10))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none', alpha=0.8)
#
# # Customize plot
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('Nebula-Like 3D Surface Plot')
#
# plt.show()





# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
#
# def menger_sponge(iterations, size=1.0):
#     vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
#                          [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
#
#     for _ in range(iterations):
#         new_vertices = []
#
#         for v0, v1 in zip(vertices[:-1], vertices[1:]):
#             mid_point = (v0 + v1) / 3.0
#             new_vertices.extend([v0, mid_point, mid_point, v1])
#
#         new_vertices.append(vertices[-1])
#         vertices = np.array(new_vertices)
#
#     return size * vertices
#
# # Generate Menger sponge coordinates
# iterations = 3  # Adjust the number of iterations for more or less detail
# sponge_vertices = menger_sponge(iterations)
#
# # Create a pandas DataFrame
# df = pd.DataFrame({'X': sponge_vertices[:, 0], 'Y': sponge_vertices[:, 1], 'Z': sponge_vertices[:, 2]})
#
# # Create a 3D plot of the Menger sponge
# fig = plt.figure(figsize=(10, 10))
# ax = fig.add_subplot(111, projection='3d')
#
# # Create Poly3DCollection from vertices
# ax.add_collection3d(Poly3DCollection([sponge_vertices], facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
#
# # Customize plot
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('Menger Sponge in 3D')
#
# plt.show()





# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# def torus(R, r, phi, theta):
#     x = (R + r * np.cos(theta)) * np.cos(phi)
#     y = (R + r * np.cos(theta)) * np.sin(phi)
#     z = r * np.sin(theta)
#
#     return x, y, z
#
# # Generate torus coordinates
# R, r = 3, 1
# phi = np.linspace(0, 2 * np.pi, 100)
# theta = np.linspace(0, 2 * np.pi, 100)
# phi, theta = np.meshgrid(phi, theta)
# x, y, z = torus(R, r, phi, theta)
#
# # Create a pandas DataFrame
# df = pd.DataFrame({'X': x.flatten(), 'Y': y.flatten(), 'Z': z.flatten()})
#
# # Create a 3D plot of the torus
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none', alpha=0.8)
#
# # Customize plot
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('Torus in 3D')
#
# plt.show()




# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# def spiral_galaxy(theta, phi, r0, a, b, c):
#     x = r0 * np.sin(a * theta) * np.cos(b * phi)
#     y = r0 * np.sin(a * theta) * np.sin(b * phi)
#     z = r0 * np.cos(a * theta) * np.exp(-c * theta)
#
#     return x, y, z
#
# # Generate spiral galaxy coordinates
# theta = np.linspace(0, 5 * np.pi, 1000)
# phi = np.linspace(0, 2 * np.pi, 100)
# theta, phi = np.meshgrid(theta, phi)
# r0, a, b, c = 1, 0.3, 3, 0.1
# x, y, z = spiral_galaxy(theta, phi, r0, a, b, c)
#
# # Create a pandas DataFrame
# df = pd.DataFrame({'X': x.flatten(), 'Y': y.flatten(), 'Z': z.flatten()})
#
# # Create a 3D plot of the spiral galaxy in blue
# fig = plt.figure(figsize=(10, 10))
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, cmap='Blues', edgecolor='none', alpha=0.8)
#
# # Customize plot
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('Spiral Galaxy in Blue')
#
# plt.show()





# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# def ghost_face(theta, phi, r_eyes, r_mouth):
#     x_eyes = r_eyes * np.sin(theta) * np.cos(phi - np.pi / 4)
#     y_eyes = r_eyes * np.sin(theta) * np.sin(phi - np.pi / 4)
#     z_eyes = r_eyes * np.cos(theta) + 3  # Adjust the height of the eyes
#
#     x_mouth = r_mouth * np.sin(theta) * np.cos(phi)
#     y_mouth = r_mouth * np.sin(theta) * np.sin(phi)
#     z_mouth = -r_mouth * np.cos(theta) - 1  # Adjust the depth of the mouth
#
#     return x_eyes, y_eyes, z_eyes, x_mouth, y_mouth, z_mouth
#
# # Generate ghost face coordinates
# theta = np.linspace(0, np.pi, 100)
# phi = np.linspace(0, 2 * np.pi, 100)
# theta, phi = np.meshgrid(theta, phi)
# r_eyes, r_mouth = 0.2, 0.5
# x_eyes, y_eyes, z_eyes, x_mouth, y_mouth, z_mouth = ghost_face(theta, phi, r_eyes, r_mouth)
#
# # Create a pandas DataFrame
# df_eyes = pd.DataFrame({'X': x_eyes.flatten(), 'Y': y_eyes.flatten(), 'Z': z_eyes.flatten()})
# df_mouth = pd.DataFrame({'X': x_mouth.flatten(), 'Y': y_mouth.flatten(), 'Z': z_mouth.flatten()})
#
# # Create a 3D plot of the ghost face
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(df_eyes['X'], df_eyes['Y'], df_eyes['Z'], color='black', label='Eyes')
# ax.scatter(df_mouth['X'], df_mouth['Y'], df_mouth['Z'], color='red', label='Mouth')
#
# # Customize plot
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('Ghost Face in 3D')
# ax.legend()
#
# plt.show()




# import time
# start = time.perf_counter()
# def do_something():
#     print('Sleeping 1 sec...')
#     time.sleep(1.9)
#     print('Done sleeping...')
# do_something()
# finish = time.perf_counter()
# print(f'Finish in {round(finish-start)} second(s)')




# import turtle
# import random
# import time
#
# delay = 0.1
# sc = 0      # score card
# hs = 0      # highest score
# bodies = []
# # creatiing of screen
# s = turtle.Screen()
# s.title('Snake Game')
# s.bgcolor('light blue')
# s.setup(width=600,height=600)
#
# # head of turtle
# head = turtle.Turtle()
# head.speed(0)
# head.shape('circle')
# head.color('blue')
# head.fillcolor('red')
# head.penup()
# head.goto(0,0)
# head.direction = 'stop'
#
# # food for snake
# food = turtle.Turtle()
# food.speed(0)
# food.shape('square')
# food.color('red')
# food.fillcolor('blue')
# food.penup()
# food.ht()       # for hiding turtle
# food.goto(200,150)
# food.direction = 'stop'
# food.st()       # for showing turtle
#
# # score board
# sb = turtle.Turtle()
# sb.penup()
# sb.ht()
# sb.goto(-250,250)
# sb.write('Score: 0   |   Highet Score: 0')
#
# # functions for moving in all direction
# def moveUp():
#     if head.direction != 'down':
#         head.direction = 'up'
# def moveDown():
#     if head.direction != 'up':
#         head.direction = 'down'
# def moveLeft():
#     if head.direction != 'right':
#         head.direction = 'left'
# def moveRight():
#     if head.direction != 'left':
#         head.direction = 'right'
# def moveStop():
#     head.direction = 'stop'
# def move():
#     if head.direction == 'up':
#         y = head.ycor()
#         head.sety(y + 20)
#     if head.direction == 'left':
#         x = head.xcor()
#         head.setx(x - 20)
#     if head.direction == 'down':
#         y = head.ycor()
#         head.sety(y - 20)
#     if head.direction == 'right':
#         x = head.xcor()
#         head.setx(x + 20)
#
# # event handling
# s.listen()
# s.onkey(moveUp,'Up')
# s.onkey(moveDown,'Down')
# s.onkey(moveRight,'Right')
# s.onkey(moveLeft,'Left')
# s.onkey(moveStop,'space')
#
# # main loop
# while True:
#     s.update()      # to update the screen
#     # check collision with border
#     if head.xcor() > 290:
#         head.setx(-290)
#     if head.xcor() < -290:
#         head.setx(+290)
#     if head.ycor() > 290:
#         head.sety(-290)
#     if head.ycor() < -290:
#         head.sety(+290)
#
#     # check collision with food
#     if head.distance(food) < 20:
#         x = random.randint(-290,290)
#         y = random.randint(-290,290)
#         food.goto(x,y)
#         # increase the body of the snake
#         body = turtle.Turtle()
#         body.speed(0)
#         body.penup()
#         body.shape('square')
#         body.color('red')
#         body.fillcolor('blue')
#         bodies.append(body)         # append new body in the list
#         sc += 100           # increase the score
#         delay -= 0.001      # increase the speed
#
#         if sc > hs:
#             hs = sc     # update highest score
#         sb.clear()
#         sb.write(f'Score:{sc}  |Highest Score{hs}')
#     # move snake bodies
#     for i in range(len(bodies) - 1,0,-1):
#         x = bodies[i - 1].xcor()
#         y = bodies[i - 1].ycor()
#         bodies[i].goto(x,y)
#     if len(bodies) > 0:
#         x = head.xcor()
#         y = head.ycor()
#         bodies[0].goto(x,y)
#     move()
# # check collision with snake body
#     for body in bodies:
#         if body.distance(head) < 20:
#             time.sleep(1)
#             head.goto(0,0)
#             head.direction = 'stop'
#             # head bodies
#             for body in bodies:
#                 body.ht()
#             bodies.clear()
#             delay = 0.1
#             sb.clear()
#             sb.write(f'Score:{sc}  |Highest Score:{hs}')
#     time.sleep(delay)
# s.mainloop()




# n = int(input('Enter Number: '))
# prn = []
# for num in range(2, n+1):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prn.append(num)
# print(len(prn))
# print(prn)







# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Generate data for the 3D plot
# theta = np.linspace(0, 2*np.pi, 100)
# phi = np.linspace(0, np.pi, 100)
# theta, phi = np.meshgrid(theta, phi)
# r = 2  # radius of the 3D shape
# x = r * np.sin(phi) * np.cos(theta)
# y = r * np.sin(phi) * np.sin(theta)
# z = r * np.cos(phi)
#
# # Create a 3D plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# # Plot the 3D surface
# ax.plot_surface(x, y, z, color='c', alpha=0.8, edgecolor='k')
#
# # Add labels and title
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('Incredible 3D Shape')
#
# # Display the plot
# plt.show()





# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Generate data for the 3D plot
# theta = np.linspace(0, 2*np.pi, 100)
# phi = np.linspace(0, 2*np.pi, 100)
# theta, phi = np.meshgrid(theta, phi)
# a, c = 1, 0.5  # parameters for torus
# x = (c + a * np.cos(theta)) * np.cos(phi)
# y = (c + a * np.cos(theta)) * np.sin(phi)
# z = a * np.sin(theta)
#
# # Create a twisted surface
# twist_factor = 2
# x_t = x * np.cos(twist_factor * phi) - y * np.sin(twist_factor * phi)
# y_t = x * np.sin(twist_factor * phi) + y * np.cos(twist_factor * phi)
# z_t = z
#
# # Create a 3D plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# # Plot the torus
# ax.plot_surface(x, y, z, color='lightcoral', alpha=0.8, edgecolor='k')
#
# # Plot the twisted surface
# ax.plot_surface(x_t, y_t, z_t, color='mediumaquamarine', alpha=0.8, edgecolor='k')
#
# # Add labels and title
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('Combined 3D Shape')
#
# # Display the plot
# plt.show()



'''
numbers = [
    [1],
    [2, 9],
    [3, 8, 10],
    [4, 7, 11, 14],
    [5, 6, 12, 13, 15]
]
for row in numbers:
    for num in row:
        print(num, end=" ")
    print()
'''




# n = 5
# m = 1
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(m,end = ' ')
#         m += 4
#     print()




# word = 'apple'
# rw = ' '
# for i in word:
#     rw = i + rw
# print(rw)




# n = int(input('Enter Year: '))
# if n % 100 == 0:
#     if n % 400 == 0:
#         print('Leap  Year')
#     else :
#         print('Not Leap Year')
# elif n % 4 == 0:
#     print('Leap Year')
# elif ((n % 4)) != 0:
#     print('Not Leap Year')




# n1 = int(input('Enter 1st Number: '))
# n2 = int(input('Enter 2nd Number: '))
# n3 = int(input('Enter 3rd Number: '))
#
# if n1 == n2 == n3:
#     print('All numbers are the same')
# elif n1 == n2 or n1 == n3 or n2 == n3:
#     print('Two numbers are the same')
#     if n1 > n2 and n1 > n3:
#         print(n1, 'Is greater')
#         if n2 < n3:
#             print(n2, 'Is smaller')
#         else:
#             print(n3, 'Is smaller')
#     elif n2 > n3:
#         print(n2, 'Is greater')
#         if n1 < n3:
#             print(n1, 'Is smaller')
#         else:
#             print(n3, 'Is smaller')
#     else:
#         print(n3, 'Is greater')
#         if n1 < n2:
#             print(n1, 'Is smaller')
#         else:
#             print(n2, 'Is smaller')
# elif n1 > n2 and n1 > n3:
#     print(n1, 'Is greater')
#     if n2 < n3:
#         print(n2, 'Is smaller')
#     else:
#         print(n3, 'Is smaller')
# elif n2 > n3:
#     print(n2, 'Is greater')
#     if n1 < n3:
#         print(n1, 'Is smaller')
#     else:
#         print(n3, 'Is smaller')
# else:
#     print(n3, 'Is greater')
#     if n1 < n2:
#         print(n1, 'Is smaller')
#     else:
#         print(n2, 'Is smaller')




# n1 = int(input('Enter 1st Number: '))
# n2 = int(input('Enter 2nd Number: '))
# n3 = int(input('Enter 3rd Number: '))
# if n1 == n2 == n3:
#     print('All numbers are same')
# elif n1 == n2 or n1 == n3 or n2 == n3:
#     print('Two numbers are same')
#     maxn = max(n1,n2,n3)
#     minn = min(n1,n2,n3)
#     print(f'Max: {maxn}\nMin: {minn}')
# else:
#     maxn = max(n1,n2,n3)
#     minn = min(n1,n2,n3)
#     print(f'Max: {maxn}\nMin: {minn}')




# prime or not
# n = int(input('Enter Number: '))
# if n == 1:
#     print('It\'s not a prime number')
# for i in range(2,n):
#     if n % i != 0:
#         print('Prime')
#         break
# 	else:
#     	print("Not Prime")
#         break





# import random
# while True:
#     n = random.randint(0, 2)
#     user_input = input('Enter Number or "1" to quit: ')
#     if user_input == '1':
#         print('Closing the game. Goodbye!')
#         break
#     try:
#         m = int(user_input)
#     except ValueError:
#         print('Invalid input. Please enter a number or "1" to quit.')
#         continue
#     if n == m:
#         print('You Won!')
#     else:
#         print(f'You Lose. The correct number was {n}')





# import random
# while True:
#     n = random.randint(0, 5)
#     # Ask the user to enter 'q' to quit or any other number to continue
#     quit1 = input('Enter "q" to quit or Press Enter: ')
#     # Check if the user wants to quit
#     if quit1.lower() == 'q':
#         print('Exiting the game. Goodbye!')
#         break
#     try:
#         m = int(input('Enter Number: '))
#     except ValueError:
#         print('Invalid Input. Please enter a valid number.')
#         continue
#     if m == n:
#         print('You Won!')
#     else:
#         print(f'You Lose. The correct number was {n}')





'''
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Generate random dataset
np.random.seed(123)
num_samples = 100
x1 = np.random.normal(10, 2, num_samples) # Independent variable 1 (age)
x2 = np.random.normal(5, 1, num_samples) # Independent variable 2 (income)
y = 2*x1 + 3*x2 + np.random.normal(0, 1, num_samples) # Dependent variable (savings)

# Reshape independent variables
X = np.column_stack((x1, x2))

# Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model on training data
model.fit(X_train, y_train)

# Predict the savings using the test set
y_pred = model.predict(X_test)

# Print model coefficients and intercept
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)

# Print model performance metrics
from sklearn.metrics import mean_squared_error, r2_score
print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))
print('R2 score: %.2f' % r2_score(y_test, y_pred))
'''





'''
# Step 1 : import library
import pandas as pd
# Step 2 : import data
salary = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/Salary%20Data.csv')
# Step 3 : define target (y) and features (X)
salary.columns
y = salary['Salary']
X = salary[['Experience Years']]
# Step 4 : train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=2529)
# check shape of train and test sample
X_train.shape, X_test.shape, y_train.shape, y_test.shape
# Step 5 : select model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
# Step 6 : train or fit model
model.fit(X_train,y_train)
model.intercept_
model.coef_
# Step 7 : predict model
y_pred = model.predict(X_test)
y_pred
# Step 8 : model accuracy
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
mean_absolute_error(y_test,y_pred)
mean_absolute_percentage_error(y_test,y_pred)
mean_squared_error(y_test,y_pred)
'''




# numbers = [3,6,2,4, 3, 6, 8,9,1,1]
#
# for i in range(len(numbers)) :
#     for j in range(i+1, len(numbers) ):
#         if numbers[i] == numbers[j]:
#             print(numbers[i] , " is a duplicate")
#             break




# list1 = [1,3,5,7]
# list2 = [2,4,6,8]
# pair = [(x,y) for x in list1 for y in list2 if x != y]
# print(pair)





# def maxnum(n1,n2,n3):
#     if n1 > n2 and n1 > n3:
#         maxval = n1
#     elif n2 > n3:
#         maxval = n2
#     else :
#         maxval = n3
#     return f'{maxval} is the largest'
# m1 = maxnum(31,14,15)
# print(m1)





# def square_num():
#     lst = []
#     for i in range(1,30+1):
#         lst.append(i**2)
#     return lst
# print(square_num())



# import math
# def square_roots():
#     lst = []
#     for i in range(1, 50+1):
#         square_root = math.sqrt(i)
#         if square_root.is_integer():
#             lst.append(int(square_root))
#     return lst
# print(square_roots())



# def square_roots():
#     lst = []
#     for i in range(1, 50+1):
#         square_root = i**0.5
#         if square_root.is_integer():
#             lst.append(int(square_root))
#     return lst
# print(square_roots())





# def primnum(x):
# 	if x < 2:
# 		print('Enter Valid Number')
# 	elif x > 2:
# 		for i in range(2,x):
# 			if x % i == 0 :
# 				print(x,'isn\'t prime number')
# 				break
# 		else:
# 			print(x,'is prime number')
# x = int(input('Enter Number: '))
# p1 = primnum(x)




# x = True + True		# 2
# x = True - False	# 1
# x = False - True	# -1
# x = False - False	# 0
# print(x)




# data = [10,20,30,40,50,'Mayank']
# print(data)
# data[4] = data[5]
# data[5] = 'Solanki'
# d1 = [i for i in range(5)]
# print(d1)
# data.append(d1)
# print(data)




# print('Positive' if (num := float(input('Enter Number: '))) > 0 else 'Negative' if num < 0 else 'Zero')

# print('Even' if (num := float(input('Enter Number: '))) % 2 == 0 and num != 0 else 'Odd' if num % 2 != 0 else 'Zero' if num == 0 else 'Invalid Input')

# print(all([]))		# True
# print(any([]))		# False



# st = 'Mayank Solanki'
# m = len(st)				# 14
# for i in range(m):		# 0 to 13
# 	print(i,'=',st[i])


# rg = (2,3,4,5)
# for i in range(10):
# 	if i in(rg):
# 		# continue		# Skips elements
# 		# pass			# Keeps the code running
# 		# break			# Stops at the condition and proceed further
# 	print(i)
# print('Hehehehe')




# # # Linear Search:
# m = [ 1, 2, 3, 4, 5, 65, 11 ]
# def linearsearch(x):
# 	for i in m:
# 		if x == i:
# 			return f'It Exists, {x}'
# 	else:
# 		return f'Does not exist'
# ls = linearsearch(65)
# print(ls)





# # list1 = list(range(11,21))
# list1 = [ 11, 21, 45, 38, 75, 22 ]
# position = -1
# def linearSearch ( item ):
# 	for i in range( len( list1 ) ):
# 		if list1[ i ] == item:
# 			position = i
# 			break
# 	if position != -1:
# 		return "yes item is present at ", i + 1, "index"
# 	else:
# 		return "NO"
# # item = int(input("enter item"))
# item = 11
# ls = linearSearch( item )
# print( ls )




# for i in range(5):
#     print(i)
# else:
#     print("Mayank")




# def linear(array,target):
# 	for i in range(len(array))
# 		if array[i] == target:
# 			return i
# 		return -1




# def linearsearch(alist,num):
# 	for i in range(len(alist)):
# 		if alist[i] == num :
# 			return True
# 	return linearsearch
#
# alist = [1,2,5,4,55,69,52,366,4,55]
# num = linearsearch(alist,55)
# print(num)




# def linearsearch(alist, nums):
#     found_indices = {}
#     for num in nums:
#         for i in range(len(alist)):
#             if alist[i] == num:
#                 found_indices[num] = i
#                 break
#     return found_indices
#
# alist = [1, 2, 5, 4, 55, 69, 52, 366, 4]
# nums_to_search = [55, 5, 4]
#
# found_indices = linearsearch(alist, nums_to_search)
#
# for num in nums_to_search:
#     if num in found_indices:
#         print(f"Element {num} found at index {found_indices[num]}")
#     else:
#         print(f"Element {num} not found in the list")



# # triangle progammme
# for i in range(5):
# 	for j in range(5):
# 		print('*',end = '  ')
# 	print()




# # Bubble Sort:
# lst = [9,5,7,8,6,4,1,2,3]
# print(lst)
# def sortnum(lst):
# 	lgt = len( lst )
# 	for i in range( lgt - 1 ):
# 		for j in range( lgt - 1 - i ):
# 			if lst[ j ] > lst[ j + 1 ]:
# 				lst[ j ], lst[ j + 1 ] = lst[ j + 1 ], lst[ j ]
# 	return lst
# print(sortnum(lst))





# def bubble_sort ( arr ):
# 	for i in range( len( arr ) - 1 ):
# 		flag = 0
# 		for j in range( len( arr ) - 1 - i ):
# 			if arr[ j ] > arr[ j + 1 ]:
# 				arr[ j ], arr[ j + 1 ] = arr[ j + 1 ], arr[ j ]
# 				flag = 1
# 		if flag == 0:
# 			break
# 	return arr
# arr = [23,12,34,11,100,56,78]
# print(arr)
# print(bubble_sort(arr))





# # Selection Sort:
# lst = [7,8,4,5,6,1,2,3]
# def selectionsort(lst):
# 	for i in range( len( lst ) - 1 ):
# 		for j in range( i + 1, len( lst ) ):
# 			if lst[i] > lst[j]:
# 				lst[i],lst[j] = lst[j],lst[i]
# 	return lst
# ss = selectionsort(lst)
# print(ss)





# # Binarysearch with recursion:
# def birec(lst, num, low, high,count = 0):
#     if low <= high:
#         count += 1
#         mid = (low + high) // 2
#         if lst[mid] == num:
#             print(mid)
#             # return f'Your {num} is at index {mid} with iterations {count}'
#         elif lst[mid] < num:
#             birec(lst, num, mid + 1, high,count)
#         elif lst[mid] > num:
#             birec(lst, num, low, mid - 1,count)
#     else:
#         return -1
# lst = [11, 12, 13, 45, 55, 56, 66, 67, 68, 70]
# print(lst)
# print(len(lst))
# low = 0
# high = len(lst) - 1
# num = eval(input('Enter Desired Number: '))
# br = birec(lst, num, low, high)
# # print(br)






# def recursion(i = 0,dpt = 1000000000): 		# if dpt >= 999 it'll alway give 999 iterations
# 	if i >= dpt:
# 		return
# 	i += 1
# 	print('Hello',i)
# 	recursion(i,dpt)
# recursion()




# # Prime Number:
# def prime(num):
# 	if num >= 2 :
# 		for i in range( 2, num ):
# 			if num % i == 0:
# 				print( 'Not Prime' )
# 				break
# 		else:
# 			print( 'Prime' )
# 	else:
# 		print('Invalid Number')
# x = eval(input('Enter Number: '))
# p1 = prime(x)
# # # p1()




# # Prime Number using Recursion:
# def prime(n,i):
# 	if i == 1:
# 		return 1
# 	if n % i == 0:
# 		return 0
# 	return prime(n,i-1)
#
# n = int(input('Enter Number: '))
# ind = prime(n,n-1)
#
# if ind == 1:
# 	print('Prime')
# if ind == 0:
# 	print('Not Prime')




# # Print your name 10 times without using loop
# count = 1
# def printer(name):
# 	global count
# 	if count <= 10:
# 		print(count,name)
# 		count += 1
# 		printer(name)
#
# printer('Mayank')




# # Factorial
# def fact(num):
# 	if num > 0:
# 		num = num * fact(num - 1)
# 		return num
# 	return 1
#
# x = eval(input('Enter Number: '))
# pt = fact(x)
#
# if x == 0:
# 	print(1)
# if x < 0:
# 	print('Zero se kam kaa factorial nahi hota hei bhai')
# else :
# 	print(pt)




# # 2 raised to 5:
# def raisedto(num,power):
# 	if power == 0:
# 		return 1
# 	return num * raisedto(num,power-1)
#
# x,y = map(int,input('Enter Number and power: ').split())
# rt = raisedto(x,y)
# print(rt)




# # Prime or Not
# def prime(n,i):
# 	if n >= 2:
# 		if i == 1:
# 			return 1
# 		if n % i == 0:
# 			return 0
# 		return prime( n, i - 1 )
# 	else:
# 		return 123
# n = int(input('Enter Number: '))
# pm = prime(n,n-1)
# if pm == 1:
# 	print('Prime')
# if pm == 0:
# 	print('Not Prime')
# if pm == 123:
# 	print('Invalid Number')





# # Binary Search using recursion:
# lst = [11,12,13,14,15,16,17,18,19,20]
# print(lst)
# print(len(lst))
# def bsearch(num,mn,mx):
# 	if mn <= mx:
# 		mid = (mn + mx) // 2
# 		if num < lst[mid]:
# 			return bsearch(num,mn,mid - 1)
# 		if num > lst[mid]:
# 			return bsearch(num,mid + 1,mx)
# 		else:
# 			return f'Desired number: {num}\nIndex: {mid}'
# 	else:
# 		return 'Element Not Found'
#
# num = int(input('Enter NUmber To Find: '))
# mn = 0
# mx = len(lst) - 1
# bs = bsearch(num,mn,mx)
# print(bs)




# # Sort and Search:
# def bsort(lst):
# 	for i in range(len(lst)):
# 		for j in range(len(lst) - i - 1):
# 			if lst[j] > lst[j + 1]:
# 				lst[j],lst[j + 1] = lst[j + 1],lst[j]
# 	return lst
#
# lst = [645123,1254,12,3,123,12385]
# bs = bsort(lst)
# print(bs)



# # Linear Search:
# lst = [22,54,89,7455,326,697929842886,9512691345,123456789]
# print(lst)
# def lnsearch(num):
# 	for i in range(len(lst)):
# 		if num == lst[i]:
# 			return f'Yes It exists at place {i + 1}'
# 	return 'Does not exist'
#
# n = eval(input('Enter Value: '))
# lns = lnsearch(n)
# print(lns)




# # Sort + Search:

# lst = [1, 17, 41, 81, 65, 33, 89, 73, 49, 9, 97, 57, 25]
# def sort_search():
#
# 	def sort1( lst ):
# 		for i in range( len( lst ) ):
# 			for j in range( len( lst ) - i - 1 ):
# 				if lst[ j ] > lst[ j + 1 ]:
# 					lst[ j ], lst[ j + 1 ] = lst[ j + 1 ], lst[ j ]
# 		return lst
#
# 	def search1( num, low = 0, high = len( lst ) - 1 ):
# 		if low < high:
# 			mid = (low + high) // 2
# 			if num == lst[ mid ]:
# 				return lst[ mid ]
# 			if num < lst[ mid ]:
# 				search1( num, low, mid - 1 )
# 			if num > lst[ mid ]:
# 				search1( num, mid + 1, high )
# 		else:
# 			'Number Does not exists'
# 	sort1(lst)
# 	num = 65
# 	s1 = search1(num)
# 	return s1
#
# print(sort_search())



# # stack fake sample:
# lst =[]
# top =-1
#
# def Push(n):
#     lst.append(n)
#     return lst
#
# def Pop():
#     lst.pop()
#     return lst
#
# a=Push(3)
# a=Push(10)
# # Pop()
# a=Push(40)
# a=Push(25)
# print(a)



# import array as arr
# a1 = arr.array('i', [1, 2, 3, 5, 60])
# print(a1)




# def push(arr, n):
#     max_size = 5
#     if len(arr) < max_size:
#         arr.append(n)
#         # print(arr)
#         return arr
#     else:
#         print("Stack is full. Cannot push more elements.")
#
# def pop(arr):
#     if len(arr) > 0:
#         return arr.pop()
#     else:
#         print("Stack is empty.")
#
# myList = []
# print(push(myList, 1))
# print(push(myList, 2))
# print(push(myList, 3))
# print(push(myList, 4))
# print(push(myList, 5))
# print(push(myList, 6))  # This will print "Stack is full. Cannot push more elements."
# print(pop(myList))  # This will pop and print the last element (5)
# print(pop(myList))  # This will pop and print the next-to-last element (4)




# def push(stack, n):
#     max_size = 5
#     if len(stack) < max_size:
#         stack.append(n)
#         # print(stack)
#         return stack
#     else:
#         print("Stack is full. Cannot push more elements.")
#
# def pop(stack):
#     if len(stack) > 0:
#         return stack.pop(0)
#     else:
#         print("Stack is empty.")
#
# myStack = []
# print(push(myStack, 1))
# print(push(myStack, 2))
# print(push(myStack, 3))
# print(push(myStack, 4))
# print(push(myStack, 5))
# print(push(myStack, 6))  # This will print "Stack is full. Cannot push more elements."
# print(pop(myStack))  # This will pop and print the last element (5)
# print(pop(myStack))  # This will pop and print the next-to-last element (4)
# print(pop(myStack))
# print(pop(myStack))
# print(pop(myStack))
# print(pop(myStack))




# # How to find average of N numbers in Python
# sum1 = 0
# count = 0
# def avg(start,end):
# 	global sum1,count
# 	for i in range( start, end + 1 ):
# 		sum1 += i
# 		count += 1
# 	average = sum1 / count
# 	return average
# x = eval(input('Enter Start: '))
# y = eval(input('Enter End: '))
# a1 = avg(x,y)
# print(a1)




# # How to Sum of the First N Positive Integers in Python

# method 1:
# addkar = 0
# def sums1(num):
# 	global addkar
# 	for i in range(num + 1):
# 		addkar += i
# 	return addkar
# x = eval(input('Enter Number: '))
# print(sums1(x))

# method 2:
# def sums2(num):
# 	return (num * (num + 1)) / 2
# x = eval(input('Enter Number: '))
# print(sums2(x))




# # How to find Area of a Circle in Python
# import math
# # print(math.pi)
# pi = math.pi
# def area_of_circle(r,pi):
# 	# global pi
# 	return f'Area of the Circle is {pi * r ** 2} with Radius {rad}'
# rad = eval(input("Enter Radius: "))
# ac = area_of_circle(rad,pi)
# print(ac)




# # How to Reverse a String in Python
#
# # Method 1:
# st1 = input('Enter Strings: ')
# def rev_str(st1):
# 	return st1[::-1]
# rs = rev_str(st1)
# print(rs)

# # 2
# os = input('Enter String: ')
# rs = os[::-1]
# print(rs)
#
# # 3
# os = input('Enter String: ')
# wrd = os.split()
# rs = ' '.join(wrd[::-1]for wrd in os.split())
# print(rs)




# # Reverse the number
# num = int(input('Enter Number: '))
# rn = int(str(num)[::-1])
# print(rn)



'''
Read a temperature in Celsius, and print it converted in Kelvin. The conversion
formula is K = C + 273.15, where C is Celsius temperature, and K is Kelvin temperature.
'''
# cel = float(input('Enter temp. in Celcius: '))
# kel = cel + 273.15
# print(f'{cel}_celcius converted to Kelvin is {kel}_kelvin')


'''
Read a velocity in km/h (kilometers per hour) and print it converted to m/s (meters
per second). Conversion formula is M = K / 3.6, where K is the velocity in km/h and M in
m/s.
'''

# k = int(input('Enter Velocity in Km/h: '))
# m = k / 3.6
# print(f'{k}_kmph convert in m/s is {round(m, 2)}')


'''
Read  a velocity in m/s (meters per second) and print it converted to km/h
(kilometers per hour). Conversion formula is K = M * 3.6, where K is the velocity in km/h
and M in m/s.
'''

# m = float(input('Enter m/s: '))
# k = m * 3.6
# print(f'{m}_mps in kmph is {round(k,2)}')




# # Arithmetic series:
#
# def arithseries(num):
# 	a = 1
# 	for i in range( 1, num + 1 ):
# 		print( ' ' + str( a ), end = ' ' )
# 		a += 3
# 	return a
# num = int( input( 'Enter Number: ' ) )
# art = arithseries(num)
# print(art)




# # Geometric series:
# num = int(input('Enter Number: '))
# x = 5
# for i in range(1,num + 1):
# 	print(x,end = ' ')
# 	x *= 2




# # Odd no. series
# num = int(input('Enter Number: '))
# for i in range(1,num + 1):
# 	if i % 2 != 0:
# 		print(i,end = ' ')




# # Even no. series
# odd = []
# even = []
# num = int(input('Enter Number: '))
# for i in range(1,num + 1):
# 	if i % 2 != 0:
# 		odd.append(i)
#
# 	else:
# 		even.append(i)
# print( 'Odd Numbers  : ', len(odd),odd )
# print( 'Even Numbers : ', len(even),even )




# # Square Number Series:
# num = int(input('Enter Size: '))
# for i in range(1,num + 1):
# 	print(i*i,end = ' ')




# val = input('Enter Values: ')
# lst = val.split(',')
# tup = tuple(lst)
# print('List  :',lst)
# print('Tuple :',tup)



# # How to extract extension from filename in python
# filename = input('Write File Name: ')
# file_ext = filename.split('.')
# print('The Extension is ' + repr(file_ext[-1]))



# # Display the first and last colors from a given list in Python
# colors = ['Blue','Black','Red','Green','White']
# print('%s,%s'%(colors[0],colors[-1]))



# # Display a sample examination schedule in Python
# examdate  =(10,2,2024)
# print('Exam\'ll start %i-%i-%i' %examdate)




# # How to Read a number n and compute n+nn+nnn in python
# # Num 1:
# a = int(input('Enter Number: '))
# n1 = int('%s' %a)
# n2 = int('%s%s'%(a,a))
# n3 = int('%s%s%s'%(a,a,a))
# print(n1 + n2 + n3)
# # Num 2:
# num = int(input('Enter Number: '))
# x = num*(1 + 11 + 111)
# print(x)




# import calendar as cld
#
# x = int(input('Enter Month: '))
# y = int(input('Enter Year: '))
#
# cal = cld.TextCalendar()
# cal.prmonth(y, x)





# print('''
# This
# is
# Mayank \nSolanki
# ''')




# from datetime import date
# fdate = date(2000,3,18)
# sdate = date(2024,3,10)
# dlt = sdate - fdate
# print(dlt.days)


# # How to find the difference between two numbers in Python
# n1 = float(input('Enter 1st Number : '))
# n2 = float(input('Enter 2nd Number : '))
# if n1 > n2:
# 	print(f'{n1} is {n1 - n2} numbers greater than {n2}')
# if n1 < n2:
# 	print(f'{n2} is {n2 - n1} numbers greater than {n1}')
# else :
# 	print("Both Numbers are same")




'''
Calculate sum of three numbers if the values are equal then
return thrice of their sum in Python
'''

# def threenumbers(n1,n2,n3,qt = 1):
# 	while True:
# 		if n1 == n2 == n3:
# 			return f'Thrice : {n1 * 3}'
# 		else:
# 			return f'Sum : {n1 + n2 + n3}'
# n1 = float(input('Enter 1st Number : '))
# n2 = float(input('Enter 2nd Number : '))
# n3 = float(input('Enter 3rd Number : '))
# tn = threenumbers(n1,n2,n3)
# print(tn)




# # How to reverse a number using slice operations in python
# num = int(input('Enter Number : '))
# rev = str(num)[::-1]
# print(int(rev))




# class employee:
# 	def __init__(self,empid = None,name = None ,salary = None):
# 		self.id = empid
# 		self.name = name
# 		self.salary = salary
#
# 	def setEmpid( self,empid ):
# 		self.id = empid
#
# 	def setName( self,name ):
# 		self.name = name
#
# 	def setSalary( self,salary ):
# 		self.salary = salary
#
# 	def getEmpid( self ):
# 		return self.id
#
# 	def getName( self ):
# 		return self.name
#
# 	def getSalary( self ):
# 		return self.salary
#
# 	def showall( self ):
# 		return self.id,self.name,self.salary
#
# e1 = employee(1,'Melech',56000)
# e1.setName('Mayank')
# print(e1.showall())




# lst1 = [11,12,13,14,15]
# lst2 = [21,22,23,24,25]
# print('lst1:',lst1)
# print('lst2:',lst2)
#
# def len_vagar(farvu):
#     count = 0
#     for i in farvu:
#         count += 1
#     return count
# print(len_vagar)


# print('lst3')
# lst3 = []
# for i in range(len_vagar(lst1)):
# 	lst3.append(lst1[i])
# 	if lst1[i] == lst1[-1]:
# 		for i in range( len_vagar( lst2 ) ):
# 			lst3.append( lst2[ i ] )
# print(lst3)

# print('lst3')
# lst3 = []
# for i in range(len_vagar(lst1)):
#     lst3[len_vagar(lst3):] = [lst1[i]]
# if lst3[-1] == lst1[-1]:
#     for i in range(len_vagar(lst2)):
#         lst3[len_vagar(lst3):] = [lst2[i]]
# print(lst3)
#
#
# print('lst4')
# lst4 = []
# for i in range(len_vagar(lst2)):
#     lst4[len_vagar(lst4):] = [lst2[i]]
# if lst4[-1] == lst2[-1]:
#     for i in range(len_vagar(lst1)):
#         lst4[len_vagar(lst4):] = [lst1[i]]
# print(lst4)


# # M1
# print('lst5')
# lst5 = []
# for i in range(len_vagar(lst1)):
#     lst5[len_vagar(lst5):] = [lst1[i]]
#     if i < len_vagar(lst2):
#         lst5[len_vagar(lst5):] = [lst2[i]]
# print(lst5)

# # M2
# print('lst5')
# lst5 = []
# lambai = max(len_vagar(lst1), len_vagar(lst2))
# for i in range(lambai):
#     if i < len_vagar(lst1):
#         lst5[len_vagar(lst5):] = [lst1[i]]
#     if i < len_vagar(lst2):
#         lst5[len_vagar(lst5):] = [lst2[i]]
# print(lst5)

# # M3
# def ravi_varu(*laakhide_badhu):
#     lst_result = []
#     max_length = max(len_vagar(lst) for lst in laakhide_badhu)
#     for i in range(max_length):
#         for lst in laakhide_badhu:
#             if i < len_vagar(lst):
#                 lst_result[len_vagar(lst_result):] = [lst[i]]
#     return lst_result
# print('lst5')
# lst3 = [11111,22222,33333,44444,55555,66666,77777,88888]
# lst_result = ravi_varu(lst3,lst1,lst2)
# print(lst_result)



# x = y = 5,10
# res = x == y
# print(res)






# # First In
# def fi(lst, x):
#     lst.insert(0, x)
#     return lst
# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst)
# addnum = int(input('Enter Number to Add: '))
# f1 = fi(lst, addnum)
# print(f1)

# # First Out
# def fo(lst):
# 	ot = lst.pop(0)
# 	return f'{ot} is out from {lst}'
# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst)
# f2 = fo(lst)
# print(f2)

# # Last In
# def li(lst,num):
# 	lst.append(num)
# 	return lst
# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst)
# addnum = int(input('Enter Number to Add: '))
# l1 = li(lst, addnum)
# print(l1)

# # Last Out
# def lo(lst):
# 	ot = lst.pop()
# 	return f'{ot} is out from {lst}'
# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst)
# l2 = lo(lst)
# print(l2)



# # dque with class
# class dque:
# 	global lst
# 	def firstin ( self,lst, x ):
# 		lst.insert( 0, x )
# 		return lst
# 	def firstout ( self,lst ):
# 		ot = lst.pop( 0 )
# 		return f'{ot} is out from \n{lst}'
# 	def lastin ( self,lst, num ):
# 		lst.append( num )
# 		return lst
# 	def lastout ( self,lst ):
# 		ot = lst.pop()
# 		return f'{ot} is out from \n{lst}'
# lst1 = [1, 2, 3, 4, 5, 6, 7]
# print('List1:\n',lst1)
# d1 = dque()
# d2 = dque()
# dextra = dque()
# x = int(input('Enter Number:'))
# print(d1.firstin(lst1,x))
# print(d1.firstout(lst1))
# print(d1.lastin(lst1,x))
# print(d1.lastout(lst1))






# def recursiveSum(lst):
#     if len(lst) == 1:
#         return lst[0]
#     return lst[0] + recursiveSum(lst[1:])
#
# numbers = [1, 2, 3]
# result = recursiveSum(numbers)
# print(result)




# class MyIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.end:
#             result = self.current
#             self.current += 1
#             return result
#         else:
#             raise StopIteration  # StopIteration signals the end of iteration
#
# # Example usage:
# my_iterator = MyIterator(1, 5)
#
# for value in my_iterator:
#     print(value)



'''
class Node:
	def __init__( self,item=None,next=None ):
		self.item = item
		self.next = next

class SLL:
	def __init__( self,start = None ):
		self.start = start
	def is_empty( self ):
		return self.start == None
	def insert_at_start( self,data ):
		n = Node(data,self.start)
		self.start = n
	def insert_at_last( self,data ):
		n = Node(data)
		if not self.is_empty():
			temp = self.start
			while temp.next is not None:
				temp = temp.next
			temp.next = n
		else:
			self.start = n
	def delete_item( self,data ):
		if self.start.next is None:
			pass
		elif self.start.next is None:
			if self.start.item == data:
				self.start = temp.next
			else:
				while temp.next is not None:
					if temp.next.item == data:
						temp.next = temp.next.next
						break
					temp = temp.next
	def __iter__( self ):
		return SLLIterator(self.start)
class SLLIterator:
	def __init__( self,start ):
		self.current = start
	def __iter__( self ):
		return self
	def __next__( self ):
		if not self.current:
			raise StopIteration
		data = self.current.item
		self.current = self.current.next
		return data



# driver code
mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
mylist.delete_item(30)
print()

for x in mylist:
    print(x,end=' ')

print()
'''




'''
# This is the CircularQueue class
class CircularQueue:
	
	# constructor for the class
	# taking input for the size of the Circular queue
	# from user
	def __init__ ( self, maxSize ):
		self.queue = list()
		# user input value for maxSize
		self.maxSize = maxSize
		self.head = 0
		self.tail = 0
	
	# add element to the queue
	def enqueue ( self, data ):
		# if queue is full
		if self.size() == (self.maxSize - 1):
			return ("Queue is full!")
		else:
			# add element to the queue
			self.queue.append( data )
			# increment the tail pointer
			self.tail = (self.tail + 1) % self.maxSize
			return True
	
	# remove element from the queue
	def dequeue ( self ):
		# if queue is empty
		if self.size() == 0:
			return ("Queue is empty!")
		else:
			# fetch data
			data = self.queue[ self.head ]
			# increment head
			self.head = (self.head + 1) % self.maxSize
			return data
	
	# find the size of the queue
	def size ( self ):
		if self.tail >= self.head:
			qSize = self.tail - self.head
		else:
			qSize = self.maxSize - (self.head - self.tail)
		# return the size of the queue
		return qSize


# input 7 for the size or anything else
size = input( "Enter the size of the Circular Queue" )
q = CircularQueue( int( size ) )

# change the enqueue and dequeue statements as you want
print( q.enqueue( 10 ) )
print( q.enqueue( 20 ) )
print( q.enqueue( 30 ) )
print( q.enqueue( 40 ) )
print( q.enqueue( 50 ) )
print( q.enqueue( 'Studytonight' ) )
print( q.enqueue( 70 ) )
print( q.enqueue( 80 ) )
print( q.dequeue() )
print( q.dequeue() )
print( q.dequeue() )
print( q.dequeue() )
print( q.dequeue() )
print( q.dequeue() )
print( q.dequeue() )
print( q.dequeue() )
print( q.dequeue() )
'''




# colors = {'Black','Blue','Green'}
# colors.add('Red')
# colors.add('Blue')
# print(colors)



# # Which number is greater (Without comparison operator)
# n1 = eval(input('Enter Number_1: '))
# n2 = eval(input('Enter Number_2: '))
# if n1 // n2 != 0:
# 	if n1 / n2 == 1:
# 		print('Both are same')
# 	else:
# 		print(f'{n1} is greater')
# elif n1 // n2 == 0:
# 	print(n2,'is greater')




# x = 5
# def add():
# 	global x
# 	x = 3
# 	x = x + 5
# 	print(x)
# add()
# print(x)


# my_list = [5,7,2,1,4,3,6,5,5,5,5,5,5,8]
# my_list.sort(reverse = 0)
# print(my_list)



# class employee:

# # print(e1.name)
# # print(e1.age)
# # e1.display()
# print(e1.__dict__)
# e1.age = 23
# print('\nage 23 set krya pachhi\n')
# print(e1.__dict__,'\n')
# print('\ngettattr:')
# print(getattr(e1, 'name')) 			# can fetch only one attribute at instant
# print('\nsetattr:')
# setattr(e1,'name','Ferrari') 			# can change only one attribute at instant
# print(e1.__dict__)
# print('\ndelattr:')
# delattr(e1,"age")						# Removes the attribute itself
# print(e1.__dict__)
# print('\nhasattr:')
# print(hasattr(e1,'age'))
# print(hasattr(e2,'age'))
# print(isinstance(e1,employee))




# class student:
# 	def __init__( self,nm,m ):
# 		self.name = nm
# 		self.marks = m
# 	def display( self ):
# 		print(self.name,self.marks)
# 	def change_data( self ):
# 		self.name = input('Enter Name: ')
# 		self.marks = int(input('Enter Marks: '))
# s1 = student('Mayank',99)
# s1.display()
# s1.change_data()
# s1.display()
# print(s1.name,s1.marks)



# class employee:
# 	company_name = 'Infosys'
# 	def __init__( self,nm,sal ):
# 		self.name = nm
# 		self.salary = sal
#
# 	@classmethod
#
# 	def get_comp_name( cls ):
# 		return f'Company name is: {cls.company_name}'
#
# e1 = employee('Mayank',1200000)
# print(e1.name,e1.salary,e1.company_name,e1.get_comp_name())
# # e1.get_comp_name()



# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# def say_hello():
#     print("Hello!")
#
# say_hello = my_decorator(say_hello)
#
# say_hello()



# class employee:
#     def set_name( self,nm ):
#         self.name = nm
#     def get_name( self ):
#         print('Name is: ',self.name)
#
# e1 = employee()
# e2 = employee()
# e1.set_name(input('Enter Name:'))
# e2.set_name(input('Enter Name:'))
#
# e1.get_name()
# e2.get_name()



# class employee:
# 	bonus1 = 2000
# 	def display( self ):
# 		print('Hello Employee')
#
# class manager(employee):
# 	bonus2 = 5000
# 	def show( self ):
# 		print('Hello Manager')
#
# e1 = employee()
# m1 = manager()
#
# m1.display()
# # e1.show()
# print(e1.bonus1)
# print(m1.bonus2)
# print(m1.bonus1)





# # Define the maximum size of the stack
# stack_size = 5
#
# # Initialize the stack with 'None' values
# stack = [None] * stack_size
#
# # Initialize the top index to -1 since the stack is empty
# top = -1
#
# # Function to push a new element onto the stack
# def push(value):
#     global top, stack_size
#
#     # Check if the stack is full (overflow)
#     if top >= stack_size - 1:
#         print("Stack is full (Overflow)")
#     else:
#         # Increment the top index and add the new value to the stack
#         top += 1
#         stack[top] = value
#
# # Function to print the current state of the stack
# def print_stack():
#     global top, stack_size
#     print("Stack:", stack[:top + 1])  # Display elements in the stack
#     print("Stack Size:", stack_size)  # Display the maximum size of the stack
#     print("Top Index:", top)  # Display the index of the top element in the stack
#
# # Function to pop the top element from the stack
# def pop_stack():
#     global top
#
#     # Check if the stack is empty
#     if top < 0:
#         return "Stack is empty"
#     else:
#         # Remove the top element from the stack and return it
#         popped = stack[top]
#         stack[top] = None
#         top -= 1
#         return popped

# push(10)
# push(20)
# push(30)
# print_stack()  # Output: Stack: [10, 20, 30], Stack Size: 5, Top Index: 2
# print(pop_stack())  # Output: 30
# print_stack()  # Output: Stack: [10, 20, None], Stack Size: 5, Top Index: 1




# stack = []
# top = -1
#
# def pushing(stack,*num):
#     if len(stack) == 0:
#         stack.insert(0,num)
#     else:
#         stack.append(num)
#     print(stack)
#
# def popping(stack):
#     stack.pop()
#
# pushing(stack,12)
# pushing(stack,13,14,15,16,17)






# class stackcl:
#     def isempty ( self,my_stack ):
#         if len( my_stack ) == 0:
#             return True
#         else:
#             return False
#
#     def top ( self,my_stack ):
#         if self.is_empty( my_stack ):
#             print( 'Stack is Empty' )
#             return None
#         else:
#             return my_stack[ -1 ]
#
#     def pushing (self, my_stack, num ):
#         if len(my_stack) != 0:
#             my_stack.append( num )
#         else :
#             my_stack.insert(0,num)
#         return my_stack
#
#     def popping ( self,my_stack ):
#         if self.isempty( my_stack ):
#             print( 'Stack is Empty' )
#             print( 'Can\'t Delete' )
#         else:
#             return print(f'{my_stack.pop()} is deleted')
#
#     def display ( self,my_stack ):
#         for i in range( len( my_stack ) - 1, -1, -1 ):
#             print( my_stack[ i ] )
#
#     def length ( self,my_stack ):
#         return print(len( my_stack ))
#
# stack1 = []
# s1 = stackcl()
# s1.pushing(stack1,11)
# s1.pushing(stack1,22)
# s1.pushing(stack1,33)
# s1.pushing(stack1,44)
# s1.pushing(stack1,55)
# s1.display(stack1)
# s1.length(stack1)
# s1.popping(stack1)
# s1.display(stack1)
# s1.length(stack1)






# class quecl:
# 	def isempty ( self,que1 ):
# 		if len( que1 ) == 0:
# 			return True
# 		else:
# 			return False
#
# 	def first ( self,que1 ):
# 		if self.isempty( que1 ):
# 			print( '\nQueue is Empty' )
# 			return None
# 		else:
# 			return que1[ 0 ]
#
# 	def pushing ( self,que1, num ):
# 		que1.append( num )
# 		return print( f'\n{num} is added in Queue: {que1}' )
#
# 	def popping ( self,que1 ):
# 		if self.isempty( que1 ):
# 			print( '\nQueue is empty' )
# 			print( 'Can\'t Delete' )
# 		else:
# 			return print( f'\n{que1.pop( 0 )} is out from Queue: {que1}' )
#
# 	def display ( self,que1 ):
# 		if self.isempty(que1):
# 			for i in range( 0, len( que1 ) ):
# 				print( que1[ i ] )
# 			if len(que1) == 0:
# 				return print( f'\nNothing to display' )
#
# 	def length (self,que1):
# 		if len(que1) >= 1:
# 			return print(f'\nThere\'re {len(que1)} elements in Queue')
# 		else:
# 			return print( f'\nThere\'s {len( que1 )} element in Queue' )
#
# que = []
# # print(isempty(que))
# # first(que)
# # pushing(que,11)
# # pushing(que,22)
# # pushing(que,33)
# # pushing(que,44)
# # pushing(que,55)
# # display(que)
# # popping(que)
# # display(que)
# q1 = quecl()
# # print(q1.isempty(que))
# q1.pushing(que,11)
# q1.pushing(que,22)
# q1.pushing(que,33)
# q1.pushing(que,44)
# q1.pushing(que,55)
# q1.display(que)
# q1.length(que)
# q1.popping(que)
# q1.popping(que)
# q1.popping(que)
# q1.popping(que)
# q1.popping(que)
# q1.popping(que)
# q1.display(que)
# q1.length(que)






# class CircularDeque:
#     def __init__(self, capacity):
#         # Initialize the CircularDeque with a specified capacity
#         self.capacity = capacity
#         # Create a list to represent the circular deque
#         self.queue = [None] * capacity
#         # Initialize front and rear indices to -1 to indicate an empty deque
#         self.front = self.rear = -1
#
#     def is_empty(self):
#         # Check if the deque is empty
#         return self.front == -1
#
#     def is_full(self):
#         # Check if the deque is full
#         return (self.rear + 1) % self.capacity == self.front
#
#     def enqueue_front(self, item):
#         # Enqueue an item at the front of the deque
#         if self.is_full():
#             print("\nDeque is full. Cannot enqueue at the front.")
#         else:
#             # If deque is empty, set front and rear to 0
#             if self.is_empty():
#                 self.front = self.rear = 0
#             else:
#                 # Update front index in a circular manner
#                 self.front = (self.front - 1) % self.capacity
#             # Add the item to the front
#             self.queue[self.front] = item
#             print(f"\n{item} enqueued at the front of the Deque: {self.queue}")
#
#     def enqueue_rear(self, item):
#         # Enqueue an item at the rear of the deque
#         if self.is_full():
#             print("\nDeque is full. Cannot enqueue at the rear.")
#         else:
#             # If deque is empty, set front and rear to 0
#             if self.is_empty():
#                 self.front = self.rear = 0
#             else:
#                 # Update rear index in a circular manner
#                 self.rear = (self.rear + 1) % self.capacity
#             # Add the item to the rear
#             self.queue[self.rear] = item
#             print(f"\n{item} enqueued at the rear of the Deque: {self.queue}")
#
#     def dequeue_front(self):
#         # Dequeue an item from the front of the deque
#         if self.is_empty():
#             print("\nDeque is empty. Cannot dequeue from the front.")
#         else:
#             # Retrieve the item at the front
#             removed_item = self.queue[self.front]
#             # If deque has only one item, reset front and rear to -1
#             if self.front == self.rear:
#                 self.front = self.rear = -1
#             else:
#                 # Update front index in a circular manner
#                 self.front = (self.front + 1) % self.capacity
#             print(f"\n{removed_item} dequeued from the front of the Deque: {self.queue}")
#
#     def dequeue_rear(self):
#         # Dequeue an item from the rear of the deque
#         if self.is_empty():
#             print("\nDeque is empty. Cannot dequeue from the rear.")
#         else:
#             # Retrieve the item at the rear
#             removed_item = self.queue[self.rear]
#             # If deque has only one item, reset front and rear to -1
#             if self.front == self.rear:
#                 self.front = self.rear = -1
#             else:
#                 # Update rear index in a circular manner
#                 self.rear = (self.rear - 1) % self.capacity
#             print(f"\n{removed_item} dequeued from the rear of the Deque: {self.queue}")
#
#     def display(self):
#         # Display the contents of the deque
#         if self.is_empty():
#             print("\nDeque is empty.")
#         else:
#             print("\nDeque:", end=" ")
#             i = self.front
#             while True:
#                 # Print each element in the circular manner
#                 print(self.queue[i], end=" ")
#                 if i == self.rear:
#                     break
#                 i = (i + 1) % self.capacity
#             print()
#
#
# # Example usage:
#
# # Create a CircularDeque with a capacity of 5
# cd = CircularDeque(5)
#
# # Enqueue and dequeue operations from both ends
# cd.enqueue_front(1)
# cd.enqueue_rear(2)
# cd.display()
# cd.dequeue_front()
# cd.dequeue_rear()
# cd.display()





# def init_deque(capacity):
#     # Initialize the circular deque with a specified capacity
#     queue = [None] * capacity
#     front = rear = -1
#     return queue, front, rear
#
# def is_empty(front):
#     # Check if the deque is empty
#     return front == -1
#
# def is_full(rear, front, capacity):
#     # Check if the deque is full
#     return (rear + 1) % capacity == front
#
# def enqueue_front(queue, front, rear, item, capacity):
#     # Enqueue an item at the front of the deque
#     if is_full(rear, front, capacity):
#         print("\nDeque is full. Cannot enqueue at the front.")
#     else:
#         # If deque is empty, set front and rear to 0
#         if is_empty(front):
#             front = rear = 0
#         else:
#             # Update front index in a circular manner
#             front = (front - 1) % capacity
#         # Add the item to the front
#         queue[front] = item
#         print(f"\n{item} enqueued at the front of the Deque: {queue}")
#     return queue, front, rear
#
# def enqueue_rear(queue, front, rear, item, capacity):
#     # Enqueue an item at the rear of the deque
#     if is_full(rear, front, capacity):
#         print("\nDeque is full. Cannot enqueue at the rear.")
#     else:
#         # If deque is empty, set front and rear to 0
#         if is_empty(front):
#             front = rear = 0
#         else:
#             # Update rear index in a circular manner
#             rear = (rear + 1) % capacity
#         # Add the item to the rear
#         queue[rear] = item
#         print(f"\n{item} enqueued at the rear of the Deque: {queue}")
#     return queue, front, rear
#
# def dequeue_front(queue, front, rear, capacity):
#     # Dequeue an item from the front of the deque
#     if is_empty(front):
#         print("\nDeque is empty. Cannot dequeue from the front.")
#     else:
#         # Retrieve the item at the front
#         removed_item = queue[front]
#         # If deque has only one item, reset front and rear to -1
#         if front == rear:
#             front = rear = -1
#         else:
#             # Update front index in a circular manner
#             front = (front + 1) % capacity
#         print(f"\n{removed_item} dequeued from the front of the Deque: {queue}")
#     return queue, front, rear
#
# def dequeue_rear(queue, front, rear, capacity):
#     # Dequeue an item from the rear of the deque
#     if is_empty(front):
#         print("\nDeque is empty. Cannot dequeue from the rear.")
#     else:
#         # Retrieve the item at the rear
#         removed_item = queue[rear]
#         # If deque has only one item, reset front and rear to -1
#         if front == rear:
#             front = rear = -1
#         else:
#             # Update rear index in a circular manner
#             rear = (rear - 1) % capacity
#         print(f"\n{removed_item} dequeued from the rear of the Deque: {queue}")
#     return queue, front, rear
#
# def display(queue, front, rear, capacity):
#     # Display the contents of the deque
#     if is_empty(front):
#         print("\nDeque is empty.")
#     else:
#         print("\nDeque:", end=" ")
#         i = front
#         while True:
#             # Print each element in the circular manner
#             print(queue[i], end=" ")
#             if i == rear:
#                 break
#             i = (i + 1) % capacity
#         print()
#
# # Example usage:
#
# # Initialize CircularDeque with a capacity of 5
# deque_capacity = 5
# deque, front_index, rear_index = init_deque(deque_capacity)
#
# # Enqueue and dequeue operations from both ends
# deque, front_index, rear_index = enqueue_front(deque, front_index, rear_index, 1, deque_capacity)
# deque, front_index, rear_index = enqueue_rear(deque, front_index, rear_index, 2, deque_capacity)
# display(deque, front_index, rear_index, deque_capacity)
# deque, front_index, rear_index = dequeue_front(deque, front_index, rear_index, deque_capacity)
# deque, front_index, rear_index = dequeue_rear(deque, front_index, rear_index, deque_capacity)
# display(deque, front_index, rear_index, deque_capacity)






# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.stack = [None] * size
#         self.top = -1
#
#     def is_empty(self):
#         return self.top == -1
#
#     def is_full(self):
#         return self.top == self.size - 1
#
#     def push(self, val):
#         if self.is_full():
#             print("Stack is overflow")
#         else:
#             self.top += 1
#             self.stack[self.top] = val
#
#     def pop(self):
#         if self.is_empty():
#             return "Stack is empty"
#         else:
#             popped = self.stack[self.top]
#             self.stack[self.top] = None
#             self.top -= 1
#             return popped
#
#     def print_stack(self):
#         print(self.stack[: self.top + 1])
#
# # Example usage:
# stack_size = 5
# stack = Stack(stack_size)
#
# # Pushing elements onto the stack
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# # Printing the current stack
# stack.print_stack()
#
# # Popping an element from the stack
# popped_value = stack.pop()
# print("Popped:", popped_value)
#
# # Printing the updated stack
# stack.print_stack()





# list1 = [None] * 5
# print(list1)
#
# lstlen = 5
# stack = [None] * lstlen
# top =-1
# class cc:
#     def push ( val ):
#         global lstlen
#         global top
#         if (top >= lstlen - 1):
#             print( "listlen :", lstlen )
#             print( "Stack is overflow" )
#         else:
#             top += 1
#             stack[ top ] = val
#
#     def print_stack ():
#         global top
#         global lstlen
#         print( stack )
#         print( lstlen, " - ", top )
#
#     def pop_stack ():
#         global top
#         global lstlen
#         if top < 0:
#             return "List is empty"
#         else:
#             popped = stack[ top ]
#             stack[ top ] = None
#             top = top - 1
#             return popped
#
# push(11)
# push(12)
# push(13)
# push(14)
# push(15)
# # push(16)
# print(pop_stack())
# print(pop_stack())
# print(pop_stack())
# print(pop_stack())
# print(pop_stack())
# print(pop_stack())
# print_stack()




# lst = [1, 2, 3, 4, 5]
# front = rear = -1
# cap = 5
# l1 = [None] * cap
#
# def emptyq():
#     global front, rear
#     return front == rear == -1
#
# def qfull():
#     global front, rear, cap
#     return (front == 0 and rear == cap - 1) or (front == rear + 1)
#
# def ipfront(num):
#     global front, rear, cap, lst
#     if not qfull():
#         if front == -1:
#             front = rear = 0
#         elif front == 0:
#             front = cap - 1
#         else:
#             front -= 1
#         lst[front] = num
#     else:
#         print('Queue is full.Cannot insert at front.')
#
# def iprear(num):
#     global front, rear, cap, lst
#     if not qfull():
#         if front == -1:
#             front = rear = 0
#         elif rear == cap - 1:
#             rear = 0
#         else:
#             rear += 1
#         lst[rear] = num
#     else:
#         print('Queue is full.Cannot insert at rear.')
#
# def dqfront():
#     global front, rear, cap, lst
#     if not emptyq():
#         if front == rear:
#             front = rear = -1
#         elif front == cap - 1:
#             front = 0
#         else:
#             front += 1
#     else:
#         print('Queue is empty.Cannot delete from front.')
#
# def dqrear():
#     global front, rear, cap, lst
#     if not emptyq():
#         if front == rear:
#             front = rear = -1
#         elif rear == 0:
#             rear = cap - 1
#         else:
#             rear -= 1
#     else:
#         print('Queue is empty.Cannot delete from rear.')
#
# def displayq():
#     global front, rear, cap, lst
#     if not emptyq():
#         i = front
#         while True:
#             print(lst[i], end=" ")
#             if i == rear:
#                 break
#             i = (i + 1) % cap
#         print()
#     else:
#         print('Queue is empty.')
#
#
# iprear(6)
# ipfront(12)
# ipfront(0)
# iprear(55)
# displayq()
#
# dqfront()
# dqrear()
# displayq()
#
# # ipfront(lst,66)
# print(lst)
# print(emptyq(lst))



# class Stack:
# 	def __init__( self ):
# 		self.list1 = list1
# 	def is_empty( self,list1 ):
# 		if len(self.list1) < 1:
# 			print('Stack is Empty')
# 			return True
# 		else:
# 			return print(list1)
# 	def pushing( self,num ):
# 		self.list1.append(num)
# 		return print(self.list1)
# 	def popping( self ):
# 		if len(self.list1) <= 0:
# 			print('No more elements to delete')
# 		else:
# 			self.list1.pop()
# 			return print( self.list1 )
# 	def peek( self ):
# 		if not is_empty():
# 			return print(self.list1[-1])
# 		else:
# 			print('Koi peek pr nahi hai bhai')
# 	def size( self ):
# 		return print(len(self.list1))
#
#
# l1 = [11,22,33,44,55]
# l2 = []
# s2 = Stack(l2)
# s2.is_empty(l2)
# s2.peek()
# s1 = Stack(l1)
# s1.is_empty(l1)
# s1.pushing(99)
# s1.popping()
# s1.peek()
# s1.size()
# s1.popping()
# s1.popping()
# s1.popping()
# s1.popping()
# s1.popping()
# s1.popping()






# class Stack:
#     def __init__(self):
#         # Initialize an empty list for the stack
#         self.list1 = []
#
#     def is_empty(self):
#         # Check if the stack is empty by leveraging the truthiness of an empty list
#         return not bool(self.list1)
#
#     def pushing(self, num):
#         # Append the given number to the stack and print the updated stack
#         self.list1.append(num)
#         print(f"Pushed {num}, Stack: {self.list1}")
#
#     def popping(self):
#         # Use list.pop() with a default value to avoid IndexError if the stack is empty
#         popped_element = self.list1.pop() if self.list1 else None
#         print(f"Popped {popped_element}, Stack: {self.list1}")
#
#     def peek(self):
#         # Use list[-1:] to get the last element without popping, and handle an empty stack
#         last_element = self.list1[-1] if self.list1 else None
#         print(f"Peeked: {last_element}")
#
#     def size(self):
#         # Use len() directly and print the size of the stack
#         print(f"Size of Stack: {len(self.list1)}")
#
# # Example of usage:
# stack_instance = Stack()
# stack_instance.pushing(11)
# stack_instance.pushing(22)
# stack_instance.pushing(33)
# stack_instance.pushing(44)
# stack_instance.pushing(55)
# stack_instance.popping()
# stack_instance.popping()
# stack_instance.popping()
# stack_instance.popping()
# stack_instance.peek()
# stack_instance.size()



'''

####### 
# Stack 
#######  
|------| <-- Top 
|------| 
|------| 
|------| 
|------| 
|------| 
|------|  

########### 
# If we pop: 
########### 

|------| <-- Pop 

|------| <-- New top 
|------| 
|------| 
|------| 
|------| 
|------| 


###############
# If we push 
# a new element: 
############### 

|------| <-- Push new 
|------| element 
|------| (new top) 
|------| 
|------| 
|------| 
|------| 
|------|

'''


# class Queue:
# 	def __init__( self ):
# 		self.q = []
# 	def enqueue( self,elem ):
# 		self.q.append(elem)
# 		return self.q
# 	def dequeue( self ):
# 		if len(self.q) != 0:
# 			return self.q.pop(0)
# 		else:
# 			print('Queue is Empty')
# 	def isEmpty( self ):
# 		if len(self.q) > 0:
# 			return False
# 		return True
#
# # q1 = Queue()
# # for i in range(1,10+1):
# # 	q1.enqueue(i*11)
# #
# # print(q1.q)
# q1 = Queue()
# [q1.enqueue(i * 11) for i in range(1, 10)]
# print(q1.q)
#
# q2 = Queue()
# [q2.enqueue(i*10) for i in range(10,100+1,10)]
# print(q2.q)
#
# # [q1.dequeue() for i in range(len(q1.q) // 2)]
# # print(q1.q)
#
# # print([Queue().enqueue(i * 11) for i in range(1,10)].q)
# # print(q1.isEmpty())





'''
Mini Project 1:

You are to design an RPN calculator. RPN stands for Reverse Polish Notation.
An RPN calculator is also known as a postfix calculator. We as humans do
math as follows, for example, 4 + 7 or we must use BEMDAS rules: 8 + ((10 *
3) / 2). In RPN, we would represent these as: 4 7 + and the last expression we
represent as 8 10 3 2 / * +. Whats happening here is the operator (+ is in the
prefix position rather than infix position as we are used to). This might look a
little confusing but its actually quite simple and we can use a stack to solve
this problem.
'''

# class RPNCalculator:
#     def __init__(self):
#         self.stack = []
#
#     def calculate_rpn(self, expression):
#         operators = {'+', '-', '*', '/'}
#
#         for token in expression.split():
#             if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
#                 # If the token is a number, push it onto the stack
#                 self.stack.append(float(token))
#             elif token in operators:
#                 # If the token is an operator, pop two operands, perform the operation, and push the result
#                 operand2 = self.stack.pop()
#                 operand1 = self.stack.pop()
#
#                 if token == '+':
#                     result = operand1 + operand2
#                 elif token == '-':
#                     result = operand1 - operand2
#                 elif token == '*':
#                     result = operand1 * operand2
#                 elif token == '/':
#                     if operand2 == 0:
#                         raise ValueError("Cannot divide by zero")
#                     result = operand1 / operand2
#
#                 self.stack.append(result)
#             else:
#                 raise ValueError(f"Invalid token: {token}")
#
#         if len(self.stack) != 1:
#             raise ValueError("Invalid expression")
#
#         return self.stack[0]
#
# # Example usage:
# calculator = RPNCalculator()
# result = calculator.calculate_rpn("8 10 3 2 / * +")
# print("Result:", result)



# def f(x,*y,z = 0):
# 	return x,y,z
# print(f(1,2,3,4))


# # Stack using list:
# class Stack:
# 	def __init__( self ):
# 		self.list1 = []
# 	def is_empty( self ):
# 		if len(self.list1) < 1:
# 			return print('Stack is empty')
# 		return True
# 	def pushing( self,num ):
# 		self.list1.append(num)
# 		return self.list1
# 	def popping( self ):
# 		if self.is_empty():
# 			self.list1.pop()
# 			return self.list1
# 		else :
# 			return print('Stack is empty already')
# 	def display ( self ):
# 		stack_number = len( self.list1 )
# 		for i in range( len( self.list1 ) - 1, -1, -1 ):
# 			print( f"{self.list1[ i ]:<4} Stack: {stack_number}")
# 			stack_number -= 1
# 		print()
# 	# print(self.list1)
# 	def peek( self ):
# 		return self.list1[-1]
# 	def size( self ):
# 		return len(self.list1)
#
# s1 = Stack()
# # s1.pushing(11)
# for i in range(1 ,11):
# 	s1.pushing(i*10)
# s1.display()
# s1.popping()
# s1.popping()
# s1.display()



# # Stack extending list
# class Stack(list):
# 	def is_empty( self ):
# 		return len(self) == 0
# 	def push( self,data ):
# 		self.append(data)
# 	def pop( self ):
# 		if not self.is_empty():
# 			return super().pop()
# 		else:
# 			raise IndexError('Stack is Empty')
# 	def peek( self ):
# 		if not self.is_empty():
# 			return self[-1]
# 		else:
# 			raise IndexError('Stack is Empty')
# 	def size( self ):
# 		return len(self)
# 	def insert( self,index,data ):
# 		raise AttributeError('No attribute Insert in Sgtack')
# s1 = Stack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# print(s1.peek())
# # s1.insert(0,10)




# n1 = eval(input('Enter Number_1: '))
# n2 = eval(input('Enter Number_2: '))
# print('*  ',n1 * n2)
# print('/  ',n1 / n2)
# print('// ',n1 // n2)
# print('%  ',n1 % n2)
# print('** ',n1 ** n2)



# print(True > 0.9999999999999999)		# 16 X 9 -----> True
# print(True > 0.99999999999999999)		# 17 X 9 -----> False


# print(True and True)
# print(1 & True)
# print(True & 1)
# print(False & 1)
# print(1 & False)
# print(False or True & 0 or 1)


# x = 0.0
# print(type(x))
# print(int(x))
# print(str(x))
# print(bool(x))


# y = 0
# print(type(y))
# print(float(y))
# print(str(y))
# print(bool(y))


# z = False
# print(type(z))
# print(int(z))
# print(float(z))
# print(str(z))


# a = '0'
# print(type(a))
# print(int(a))
# print(float(a))
# print(bool(a))
# b = eval(a)
# print(type(b))
# print(bool(b))


# x = '3.14'
# print(type(x))
# x = eval(x)
# print(type(x))
# print(int(x))


# print('Mayank Solanki'[0])		# Gives M as output
# print('Mayank Solanki'[0:])		# Gives all string from given number
# print('Mayank Solanki'[::-1])		# Gives all string in return order
# print('Mayank Solanki'[:])		# Gives all string



# print('Mayank Solanki')
# print('			Mayank Solanki		'.strip())		# Removes blank spaces except in between strings
# print('		Mayank		Solanki		'.strip())


# # Replace works only for strings
# print('Mayank Solanki'.replace(' ','- - -'))		# Mayank- - -Solanki
# print('Mayank Solanki'.replace('M',True))			# Can't replace string with int or float or bool
# print("mayank".replace(['m','a'],'X'))			# Can't replace more than one element
# print('Mayank Solanki'.replace('Solanki','81'))		# You can only replace elment with same type of characters
# print('Mayank Solanki'.lower().replace('s','X'))
# print('Mayank Solanki'.upper().replace('M','X'))

# print('Mayank Solanki'.count('a'))
# print('Melech McAuley'.lower().count('a'))		# o|p: 1.first it'll convert the string in lowercase then counts the element
# print('Melech McAuley'.upper().count('E'))		# o|p: 3.first it'll convert the string in uppercase then counts the element


# print('Mayank'.isalpha())			# True. Only letters
# print('123'.isdigit())				# True. Only integers
# print('mayank @ 12'.islower())			# True. Any thing as a string but letters must be in lower case
# print('MAYANK 12'.isupper())			# True. Any thing as a string but letters must be in UPPER case


# print('mayank solanki'.capitalize())			# Mayank solanki
# print('mayank solanki'.title())				# Mayank Solanki


# print('Mayank Solanki'.startswith('May'))		# True
# print('Mayank Solanki'.endswith('nki'))			# True


# print('Mayank Solanki'.center(20,'-'))		# ---Mayank Solanki---
# print('Mayank Solanki'.ljust(20,'-'))		# Mayank Solanki------
# print('Mayank Solanki'.rjust(20,'-'))		# ------Mayank Solanki
# print('Mayank Solanki'.center(2,'-'))		# Mayank Solanki


# print('Mayank'.swapcase())			# o|p: mAYANK. Convert upper to lower,lower to upper
# print('Mayank Solanki'.zfill(20))	# o|p: 000000Mayank Solanki. Feels zero at the starting to meet the condition of length


# x = y = z = 4
# print(x,y,z,sep = '-')

'''
Unpacking:

a,x,y = z = 11,22,33
print(a,x,y,z)					# 11 22 33 (11, 22, 33)

a,x,(y,z) = 11,22,((22.5,33),44)	# 11 22 (22.5, 33) 44
print(a,x,y,z)

data = [1,2,3,4]
a,b,c,d = data
print(a,b,c,d)				# 1 2 3 4
'''


# String = "Python is powerful!"
# length = len(String)
# print(length)



# list1 = []
# for i in range(11, 26):
#     list1.append(i)
# print(len(list1))
# print(list1)
#
# lx = []
# ly = []
# num = int(input('Enter Split: '))
#
# def halfing(list1,num):
# 	for i in range( 0, num ):
# 		lx.append( list1[ i ] )
# 	print( "lx:", lx )
#
# 	for i in range( num, len( list1 ) ):
# 		ly.append( list1[ i ] )
# 	print( "ly:", ly )
#
# halfing(list1,num)




# def halfing_rec(lst, num, idx=0, lx=None, ly=None):
#     if lx is None:
#         lx = []
#     if ly is None:
#         ly = []
#
#     if idx < len(lst):
#         (lx if idx < num else ly).append(lst[idx])
#         halfing_rec(lst, num, idx + 1, lx, ly)
#     else:
#         return lx, ly
#
# lst = list(range(11, 21))
# print(len(lst))
# print(lst)
#
# n = int(input('Enter Split: '))
#
# l1 = halfing_rec(lst, n)
# print(l1)
# # print("lx:", lx)
# # print("ly:", ly)




# def half_rec(list1, idx=0, op=None):
# 	if op is None:
# 	    op = []
#
# 	if idx < len(list1):
# 	    op.append([list1[idx]])
# 	    half_rec(list1, idx + 1, op)
# 	return op
#
# list1 = []
# for i in range(11, 25 + 1):
# 	list1.append(i)
# print(list1)				# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
#
# op = half_rec(list1)
# for list2nd in op:
# 	print(list2nd)




# class Node:
#     def __init__(self, elem):
#         self.elem = elem
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def add(self, elem):
#         if self.head is None:
#             self.head = Node(elem)
#         else:
#             temp = self.head
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = Node(elem)
#
# ll1 = LinkedList()
# ll1.add(5)
# ll1.add(6)
# ll1.add(7)
#
# temp = ll1.head
# while temp is not None:
#     print(temp.elem)
#     temp = temp.next





# class Node:
# 	def __init__( self,elem ):
# 		self.elem = elem
# 		self.next = None
#
# class linkedlist:
# 	def __init__( self ):
# 		self.head = None
#
# 	def add( self,elem ):
# 		if self.head is None:
# 			self.head = Node(elem)
# 		else:
# 			temp = self.head
# 			while temp.next is not None:
# 				temp = temp.next
# 			temp.next = Node(elem)
#
# ll1 = linkedlist()
# [ll1.add(i) for i in range(11,21)]
#
# temp = ll1.head
# while temp is not None:
# 	print(temp.elem)
# 	temp = temp.next



'''
.strip()
.replace()
.count()
.lower().count()
.upper().count()
.isalpha()
.isdigit()
.islower()
.isupper()
.startswth()
.endswith()
.capitalize()
.title()
.center()
.ljust()
.rjust()
'''


'''
# Default order
String1 = "{} {} {}".format('Begineer', 'in', 'Python')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Begineer', 'in', 'Python')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Begineer', f='in', l='Python')
print("\nPrint String in order of Keywords: ")
print(String1)
'''



# from collections import Counter
# import re
#
# def analyze_text_data(text_data):
#     combined_text = ' '.join(text_data)
#
#     # Convert to lowercase to make the analysis case-insensitive
#     combined_text = combined_text.lower()
#
#     words = re.findall(r'\b\w+\b', combined_text)
#
#     keywords = ['frequency', 'User', 'analysis']
#
#     # Count the frequency of each keyword in the text
#     keyword_counts = Counter(words)
#
#     # Display the frequency of each keyword
#     for keyword in keywords:
#         print(f'The keyword "{keyword}" appears {keyword_counts[keyword]} times.')
#
# # Example usage:
# text_data = [
#     "User - generated text data for keyword frequency analysis.",
#     "Analyzing text data helps to understand user preferences.",
#     "This is an example of analyzing keyword frequency in Python."
# ]
#
# analyze_text_data(text_data)



# n1 = eval(input('Enter Number: '))
# if n1 < 0:
# 	print('{} is Negative'.format(n1))
# if n1 > 0:
# 	print('{} is Positive'.format(n1))
# if n1 == 0:
# 	print("It's a Zero")
# if not (n1 < 0 or n1 > 0 or n1 == 0):
# 	print("enter Valid Number.")




# for i in range(1, 10+1):
#     print(f"{2} * {i:2} = {2*i:2}")

# x = 0
# for i in range(1,7 + 1):
# 	for j in range(1,7 + 1):
# 		for k in range(1,7 + 1):
# 			x += 1
# 			print(i,j,k,sep = '-')
# 		print(f'{j} '*5)
# 	print(f'{i} '*10)
# print('-'*20)
# print(x)




# xx = 0
# for i in range(1,70):
# 	for j in range(1,70):
# 		if (i + j == 12):
# 			xx += 1
# 			print(f"{i:2} + {j:2} = 12")
# print('-'*13)
# print(xx)



# for i in range(1,12+1):
# 	num = 0
# 	for j in range(1,6+1):
# 		for k in range(1,6+1):
# 			if (k + j == i):
# 				num += 1
#
# 	print(i,round((num/36)*100,2))




# for i in range(1,36 + 1):
# 	num = 0
# 	for j in range(1,6 + 1):
# 		for k in range(1,6 + 1):
# 			for l in range(1,6 + 1):
# 				for m in range(1,6 + 1):
# 					for n in range(1,6 + 1):
# 						for o in range(1,6 + 1):
# 							if (j + k + l + m + n + o == i):
# 								num += 1
# 	print(i,'=',round((num/(6**6))*100,3))




# l = ["Data", "Science", "Python"]
# for i in l:
# 	print(i,end = ' ')
#
# rslt = '-'.join(l)
# print(rslt)



# print("Dictionary Iteration")
# d = dict()
# d['key1'] = "val1"
# d['key2'] = 345
# for i in d:
# 	print(i,':-',d[i])



# word = "Python"
# for i in word:
# 	print(i,end=' ')

# rl = '-'.join(word)
# print(rl)



# for i in range(1, 4):
# 	for j in range(ord('A'), ord('C') + 1):
# 		print('i',i,' j', chr(j))
# 	print()



# list1 = ["Data-Science", "Power BI", "Python"]
# for index,sub in enumerate(list1):
# 	print(f"Index: {index + 1}, Subj: {sub}")



# sq = [x**2 for x in range(5+1)]
# print(sq)
# for i in sq:
# 	print(i,end = ' ')



'''
Problem Statement - 

Write a program checking whether a number is 
an Armstrong number. An Armstrong number (also known as a 
narcissistic number, pluperfect digital invariant, or 
pluperfect number) is a number that is the sum of its own 
digits each raised to the power of the number of digits.
'''

# def is_armstrong_number(number):
#     num_str = str(number)
#     num_digits = len(num_str)
#     sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
#     return sum_of_digits == number
#
# # User input
# num = int(input("Enter a number: "))
#
# # Check and display the result
# if is_armstrong_number(num):
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")



# def armstrongnumbner(num):
# 	numstr = str( num )
# 	numlen = len( numstr )
# 	numsum = sum( int( i ) ** numlen for i in numstr )
# 	print( numsum == num )
#
# num = int(input("Enter Number: "))
# armstrongnumbner(num)



# num = int(input('Enter Number to check whether it\'s ARMSTRONG Number or NOT: '))
# anc = 0
# for i in str(num):
# 	anc += int(i)**len(str(num))
# if anc == num:
# 	print('Yes')
# else:
# 	print('No')




# def arm(number):
# 	sums = 0
# 	for i in str( number ):
# 		sums += int( i ) ** len( str( number ) )
# 	if sums == number:
# 		return True
# 	else:
# 		return False
# number = int(input('Enter Number: '))
# print(arm(number))




# count = 2
# while count <= 9:
# 	count += 2
# 	print('hehehe')
# 	print(count)


# count = 1
# while count <= 10:
# 	print(count,end = ' ')
# 	count += 1



# outer = 1
# cnt = 0
# while outer <= 3 + 1:
# 	inner1 = 1
# 	while inner1 <= 2 + 2:
# 		inner2 = 1
# 		while inner2 <= 2 + 2:
# 			cnt += 1
# 			print(outer,'X',inner1,'X',inner2)
# 			inner2 += 1
# 		print('-'*10)
# 		inner1 += 1
# 	print('='*10,'\n')
# 	outer += 1
# print(cnt)




# count = 1
# n = 0
# while count <= 20:
# 	if count in [2,3,7,11,13,17,19]:
# 		count += 1
# 		print('\n')
# 		continue
# 	n += 1
# 	print(count,end = ' ')
# 	count += 1
# print('\n')
# print('Total Loops: ',n)




# l1 = [1,2,3,4,5]
# l2 = l1.copy()
# l3 = l1[::-1]
# l2[1] = 88
# l3[1] = 11
# print(l1)
# print(l2)
# print(l3)



# count = 1
# while count <=5:
# 	if count == 4:
# 		# print(count)
# 		break
# 	print(count)
# 	count += 1



# while True:
# 	age = int(input('Enter Age: '))
# 	if age >= 0 and age <= 110:
# 		break
# 	else:
# 		print('Please enter valid Age')


# game_over = False
# while not game_over:
# 	user_input = input( 'Continue Playing? (yes/no): ' ).lower()
# 	if user_input == 'no':
# 		print('OK, See you later.....Bye!')
# 		game_over = True
# 	elif user_input == 'yes':
# 		print( 'Game is still ongoing...' )
# 	else:
# 		print( 'Invalid input. Please enter either "yes" or "no".' )



# # Method 1:
# over = True
# while over:
# 	user = input('Play Further or not? (yes/no): ')
# 	uselow = user.lower()
# 	if uselow == 'yes':
# 		print('Playing...........')
# 	if uselow == 'no':
# 		print('OK! BYE.')
# 		over = False



# # Method 2:
# over = True
# while over:
# 	user = input('Play Further or not? (yes/no): ')
# 	uselow = user.lower()
# 	if uselow == 'yes':
# 		print('Playing...........')
# 	if uselow == 'no':
# 		print('OK! BYE.')
# 		break




'''
Problem Statement - 

Create a Python program that prompts the user to enter positive numbers continuously. 
The program should use a while loop to collect input data until the user enters a non-positive number. 
Implement simple data validation to ensure entered values are valid positive numbers. Finally, 
output the list of positive numbers entered by the user. The objective is to create an interactive 
and error-tolerant program for collecting and handling user input.
'''

# # Meethod 1:
# positive = True
# l1 = []
# while positive:
# 	user_enter = int(input("Enter Positive Number: "))
# 	if user_enter >= 0:
# 		l1.append(user_enter)
# 	if user_enter < 0:
# 		print('Number is not positive')
# 		positive = False
# print( l1 )


# # Method 2
# l1 = []
# while True:
# 	user = input('Enter Positive Number: ')
# 	try:
# 		ue = float(user)
# 	except ValueError:
# 		print('Enter Valid Data')
# 	if ue >= 0:
# 		l1.append(ue)
# 	if ue < 0:
# 		print('It\'s Negative number.')
# 		break
# print('Your List:\n',l1)





# numbers = []
# while True:
#     user_input = input("Enter a positive number (enter a non-positive number to stop): ")
#     if user_input.replace('.', '', 1).isdigit() and float(user_input) > 0:
#         numbers.append(float(user_input))
#     elif user_input.replace('-', '', 1).isdigit() and float(user_input) <= 0:
#         break
#     else:
#         print("Invalid input. Please enter a valid positive number.")
# if numbers:
#     print(f"You entered the following positive numbers: {numbers}")
# else:
#     print("No positive numbers were entered.")


# -------------------------------------------------------
# def deleting( self,val ):
# 	temp = self.head
# 	while temp.next != None and temp.next.elem != val:
# 		temp = temp.next
# 	if temp.next == None:
# 		return
# 	else:
# 		temp.next = temp.next.next
# 		return val
# -------------------------------------------------------




# class Node:
# 	def __init__(self,val,next = None):
# 		self.val = val
# 		self.next = next
#
# class LinkedList(Node):
# 	def __init__( self ):
# 		self.head = None
# 	def printing( self ):
# 		temp = self.head
# 		while (temp):
# 			print(temp.val,end = ' ')
# 			temp = temp.next
# 	def inserting( self ,val):
# 		newnode = Node(val)
# 		temp = self.head
# 		while (temp.next != None):
# 			temp = temp.next
# 		temp.next = newnode
#
#
# # n1 = Node(5)
# # ll1 = LinkedList
# # ll1.inserting(5)





'''
Linked List:
'''

# class Node:
#     def __init__(self, elem):
#         self.elem = elem
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def is_empty(self):
#         return self.head is None
#
#     def insert_first(self, elem):
#         temp = self.head
#         new_Node = Node(elem)
#         self.head = new_Node
#         self.head.next = temp
#
#     def add(self, elem):
#         new_node = Node(elem)
#         if self.is_empty():
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = new_node
#
#     def remove_last(self):
#         if self.is_empty():
#             print("Cannot remove from an empty list.")
#             return
#         temp = self.head
#         if temp.next is None:
#             removed_elem = temp.elem
#             self.head = None
#             print('Removed', removed_elem)
#         else:
#             while temp.next.next is not None:
#                 temp = temp.next
#             removed_elem = temp.next.elem
#             temp.next = None
#             print('Removed', removed_elem)
#
#     def middle_insert(self, val, new_elem):
#         temp = self.head
#         while temp is not None and temp.elem != val:
#             temp = temp.next
#         if temp is None:
#             print(f"Value {val} not found in the list.")
#             return
#         new_node = Node(new_elem)
#         new_node.next = temp.next
#         temp.next = new_node
#         return new_elem
#
#     def delete_first(self):
#         if self.is_empty():
#             print("Cannot delete from empty list.")
#             return
#         removed_elem = self.head.elem
#         self.head = self.head.next
#         print('Deleted first element', removed_elem)
#         return removed_elem
#
#     def delete(self, val):
#         if self.is_empty():
#             print("Cannot delete from an empty list.")
#             return
#         if self.head.elem == val:
#             removed_elem = self.head.elem
#             self.head = self.head.next
#             print('Deleted', removed_elem)
#             return removed_elem
#         temp = self.head
#         while temp.next is not None and temp.next.elem != val:
#             temp = temp.next
#         if temp.next is None:
#             print(f"Value {val} not found in the list.")
#             return
#         removed_elem = temp.next.elem
#         temp.next = temp.next.next
#         print('Deleted', removed_elem)
#         return removed_elem
#
#     def search(self, elem):
#         temp = self.head
#         while temp is not None:
#             if temp.elem == elem:
#                 return True
#             temp = temp.next
#         return False
#
#     def ascending_sort(self):
#         c = self.count()
#         while c > 0:
#             temp = self.head
#             while temp.next is not None:
#                 if temp.elem > temp.next.elem:
#                     temp.elem, temp.next.elem = temp.next.elem, temp.elem
#                 temp = temp.next
#             c -= 1
#
#     def descending_sort(self):
#         c = self.count()
#         while c > 0:
#             temp = self.head
#             while temp.next is not None:
#                 if temp.elem < temp.next.elem:
#                     temp.elem, temp.next.elem = temp.next.elem, temp.elem
#                 temp = temp.next
#             c -= 1
#
#     def count ( self ):
#         temp = self.head
#         count = 0
#         while (temp.next != None):
#             count += 1
#             temp = temp.next
#         return count
#
#     def print_list ( self ):
#         temp = self.head
#         while temp is not None:
#             if temp.next is not None:
#                 print( temp.elem, end = ' ---> ' )
#             else:
#                 print( temp.elem, end = ' ' )
#             temp = temp.next
#         print()
#
#
#
# ll1 = LinkedList()
#
# print('Original List:')
# [ll1.add( i * 10 ) for i in range(11,21)]
# ll1.print_list()
#
# print('\nInserting 88 at First(HEAD).')
# ll1.insert_first(88)
# ll1.print_list()
#
# print(f'\nRemoving Last element.')
# ll1.remove_last()
# ll1.print_list()
#
# print('\nInserting element at the middle(after 130 adding 800).')
# ll1.middle_insert(130,800)
# ll1.print_list()
#
# print('\nDeleting element(deleting 130).')
# ll1.delete(130)
# ll1.print_list()
#
# print('\nDeleting first element')
# ll1.delete_first()
# ll1.print_list()
#
# print('\nAdding some elements in the Original list to performe other operations.')
# [ll1.add( i * 5 ) for i in range(21,36)]
#
# ll1.print_list()
# print('Searching for element(120).')
# print(ll1.search(120))
# print('Searching for element(1000).')
# print(ll1.search(1000))
#
# print('\nSorting elements in ascending form.')
# ll1.ascending_sort()
# ll1.print_list()
#
# print('\nSorting elements in descending form.')
# ll1.descending_sort()
# ll1.print_list()
#
# print('\nCounting total elements.')
# print(ll1.count())




'''
Circular Linked List:
'''
# class Node:
#     def __init__(self, elem):
#         self.elem = elem
#         self.next = None
#
# class CircularLinkedList:
#     def __init__(self, head=None, tail=None):
#         self.head = head
#         self.tail = tail
#
#     def traverse(self):
#         if not self.head:
#             return
#         temp = self.head
#         while True:
#             print(temp.elem, end=' ')
#             temp = temp.next
#             if temp == self.head:
#                 break
#         print()
#
#     def insert_at_first(self, elem):
#         new_node = Node(elem)
#         if not self.head:
#             self.head = new_node
#             self.head.next = self.head
#             self.tail = self.head
#         else:
#             new_node.next = self.head
#             self.head = new_node
#             self.tail.next = self.head
#
#     def insert_at_last(self, elem):
#         new_node = Node(elem)
#         if not self.head:
#             self.head = new_node
#             self.head.next = self.head
#             self.tail = self.head
#         else:
#             new_node.next = self.head
#             self.tail.next = new_node
#             self.tail = new_node
#
#     def delete(self, val):
#         if not self.head:
#             return False
#         if self.head.elem == val:
#             if self.head.next == self.head:
#                 self.head = None
#             else:
#                 self.head = self.head.next
#                 self.tail.next = self.head
#             return val
#         temp = self.head
#         while temp.next != self.head and temp.next.elem != val:
#             temp = temp.next
#         if temp.next == self.head:
#             return False
#         temp.next = temp.next.next
#         return val
#
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             if temp.next is not None:
#                 print(temp.elem, end=' ----> ')
#             else:
#                 print(temp.nelem,end = ' ')
#             temp = temp.next
#             if temp == self.head:
#                 break
#         print()
#
#
# cl1 = CircularLinkedList()
#
# [cl1.insert_at_first(i*10) for i in range(1,11)]
# cl1.print_list()
#
# cl1.delete(30)
# cl1.print_list()
#
# cl1.delete(20)
# cl1.print_list()
#
# cl1.insert_at_last(9000)
# cl1.print_list()
#
# cl1.insert_at_first(6000)
# cl1.print_list()




# lst = [1,2,3,4,5,6]
# print(lst)
# lst = [i**2 for i in lst]
# print(lst)
# lst = [i**2 for i in lst]
# print(lst)


# lst = []
# [lst.append(i) for i in range(1,16)]
# print(lst)
# lst = []
# [lst.append(i) for i in range(1,16) if i % 2 == 0]
# print(lst)
# lst = []
# [lst.append(i**2) for i in range(1,16) if i % 2 == 0]
# print(lst)

# lst = [[1,2,3],[4,5,6],[7,8,9]]
# for i in lst:
# 	print(i)

# for i in lst:
# 	for j in i:
# 		print(j,end = ' ')

# print([[j for i in range(2)]for j in lst])					# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([j for i in lst for j in i])				# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print( [ [ j for i in range( 2 ) ] for j in lst ] )			 # [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]


# print([[j*10 for j in range(1,2 + 1)]for i in range(1,3 + 1)])			# [[10, 20], [10, 20], [10, 20]]
#		 |-----------[ROWS]-----------|-------[COLUMNS]-------|


# print([[j for i in range(5)]for j in range(3)])			# 2nd loop, j = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2]]
# print([[i for i in range(5)]for j in range(3)])			# 1st loop, i = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]




'''
Problem Statement - Count Occurrences of each unique word in a Sentence
'''

# def count_word_occurrences(sentence):
#     word_list = sentence.split()
#     unique_words = []
#     word_counts = []
#
#     for word in word_list:
#         # Check if the word is already in the unique_words list
#         if word in unique_words:
#             index = unique_words.index(word)
#             word_counts[index] += 1
#         else:
#             # Add the word to the unique_words list and initialize its count to 1
#             unique_words.append(word)
#             word_counts.append(1)
#
#     return unique_words, word_counts
#
# # User input
# user_sentence = input("Enter a sentence: ")
#
# unique_words, word_counts = count_word_occurrences(user_sentence)
# print("Word occurrences in the sentence:")
# for word, count in zip(unique_words, word_counts):
#     print(f"{word}: {count}")




'''Dictionary'''
# dct = {1 : 'Mayank',2:'Miral',3:'Martin',4:'Melech'}
# print(dct)
# print(type(dct))

# print('Changing Martin to Aston-Martin')
# dct[3] = 'Aston' + '-' + dct[3]
# print(dct)
#
# print('Adding last element')
# dct[len(dct) + 1] = 'Last_element'
# print(dct)

# # Accesing Dictionary:
# dct = {1 : 'Mayank',2:'Miral',3:'Martin',4:'Melech'}
# print(dct)
# print('\nAccesing Dictionary:')
# print(dct)

# print(dct[1])

# print(dct[2])

# for i in dct:
# 	print(dct[i])

# print(dct['Mayank'])			# !!!!!ERROR = We cant access the key by value

# print(dct[1])				# Mayank
# print(dct.get(1))			# Mayank


# # Adding and updating the key-value pairs:
# dct = {1 : 'Mayank',2:'Miral',3:'Martin',4:'Melech'}
# print(dct)

# dct[600] = 'Yuval'		# {1: 'Mayank', 2: 'Miral', 3: 'Martin', 4: 'Melech', 600: 'Yuval'}
# print(dct)

# dct[0] = 'Morkal'			# {1: 'Mayank', 2: 'Miral', 3: 'Martin', 4: 'Melech', 0: 'Morkal'}
# print(dct)

# del dct[1]					# {2: 'Miral', 3: 'Martin', 4: 'Melech'}
# print(dct)


# # Cleaning the dictionary:
# dct = {1 : 'Mayank',2:'Miral',3:'Martin',4:'Melech'}
# print(dct)

# print(dct.clear())			# None
# print(dct)					# {}

# print(dct.keys())				# dict_keys([1, 2, 3, 4])

# print(dct.values())				# dict_values(['Mayank', 'Miral', 'Martin', 'Melech'])

# for k in dct.keys():
# 	print(k,dct[k])

# print(dct.items())				# dict_items([(1, 'Mayank'), (2, 'Miral'), (3, 'Martin'), (4, 'Melech')])
# for i in dct.items():
# 	print(i[0],i[1])

# for i in dct.items():				# (1, 'Mayank').......
# 	print(i)
#
# for i,j in dct.items():				# 1 Mayank........
# 	print(i,j)

# # Checking if key is present:
# print('Checking if key is present:')
# dct = {1 : 'Mayank',2:'Miral',3:'Martin',4:'Melech'}
# print(dct)
#
# # print(1 in dct)						# True
# # print(0 in dct)						# False

# # Some other operations:
# dict_1.update(dict_2)
# dict_1 + dict_2 						# Error


# A = "geeksforgeeks"
# B = "geeksquiz"
# print(A.split())
# print(len(A))
# la = []
# for i in A.split():
# 	for j in B.split():
# 		if j not in A.split():
# 			print(la.append(j))



# A = "efghijkl"
# B = "abcdefgh"
#
# set_A = set(A)
# set_B = set(B)
#
# result_set = (set_A - set_B) | (set_B - set_A)
# result = ''.join(sorted(result_set))
#
# print(result)
#
#
#
# # dct = {1 : {'Name':'Mayank','Phone': 9512691345},
# #         2 : {'Name':'Melech','Phone': 69792984288},
# #         3 : {'Name':'Miral','Phone': 9913328982},
# #         4 : {'Name':'Miral','Phone': 9879705541}}
# # print(dct)
# # print('-'*50*2)
# # print(dct.items())              # dict_items([(1, {'Name': 'Mayank', 'Phone': 9512691345}),......
# # print(dct.values())             # dict_values([{'Name': 'Mayank', 'Phone': 9512691345},......
# # print(dct.keys())               # dict_keys([1, 2, 3, 4])
#
# # # Accessing Elements
# # print(dct[1])               # {'Name': 'Mayank', 'Phone': 9512691345}
# # print(dct[1]['Name'])       # Mayank
# #
# # print(len(dct))             # 4
#
# # # Updating
# # print(dct[3])               # {'Name': 'Miral', 'Phone': 9913328982}
# # dct[3]['Name'] = 'Aston'
# # print(dct[3])               # {'Name': 'Aston', 'Phone': 9913328982}
#
# # # Adding
# # dct[5] = {'Name':'Viral','Phone':9876543210}
# # print(dct)                    # This will added in the last of the dictionary
# # # print(len(dct))               # 5
#
# # # Deleting
# # print(dct[4])                  # {'Name': 'Miral', 'Phone': 9879705541}
# # del dct[4]
# # print(dct[4])                  # Error
#
# # # Going through the Data
# # for i in dct.keys():
# #     print(i,dct[i]['Name'],end = ' ')                 # 1 Mayank 2 Melech 3 Miral 4 Miral
# #
# # for i in dct.keys():
# #     print(i,dct[i]['Phone'],end = ' ')                # 1 Mayank 2 Melech 3 Miral 4 Miral 1 9512691345 2 69792984288 3 9913328982 4 9879705541
# # for i in dct.keys():
# #     print(i,dct[i]['Name'],dct[i]['Phone'],end = ' ')   # 1 Mayank 9512691345 2 Melech 69792984288 3 Miral 9913328982 4 Miral 9879705541
# # print(1 in dct)                     # True
# # print(66 in dct)                    # False
#
# # # Going to level Upper with marks
# # # Taking new dct:
# # data = {1 : {'Name':'Mayank','Phone': 9512691345,'Marks':{'Hindi':45,'Math':46,'Science':48}},
# #         2 : {'Name':'Melech','Phone': 69792984288,'Marks':{'Hindi':40,'Math':30,'Science':31}},
# #         3 : {'Name':'Miral','Phone': 9913328982,'Marks':{'Hindi':39,'Math':40,'Science':41}},
# #         4 : {'Name':'Miral','Phone': 9879705541,'Marks':{'Hindi':12,'Math':41,'Science':37}},}
# # print(data)
# # print('-'*50*2)
#
# # for i in data.keys():
# #     print(i,data[i]['Name'],data[i]['Marks'])
#
# # for key, value in data.items():
# #     print(key, value.get('Name', 'Name not available'))
# #     if 'Marks' in value:
# #         for subject, marks in value['Marks'].items():
# #             print(f"   {subject}: {marks}")
#
#
#
# '''Circular Linked List'''
# class Node:
# 	def __init__( self,data ):
# 		self.data = data
# 		self.next = None
#
# class CLL:
# 	def __init__( self ):
# 		self.head = None
# 		self.tail = None
# 	def display( self ):
# 		if self.head is None:
# 			print("Empty CLL")
# 		else:
# 			temp = self.head
# 			print(temp.data,'--->',end = ' ')
# 			while temp.next != self.head:
# 				temp = temp.next
# 				print(temp.data,'--->',end = ' ')
# 			print(temp.next.data)
#
# l = CLL()
#
#
# n1 = Node(10)
# l.head = n1
# l.tail = n1
# l.tail.next = l.head
# l.display()
# print()
#
# n2 = Node(20)
# l.tail.next = n2
# l.tail = n2
# l.tail.next = l.head
# l.display()
#
# n3 = Node(30)
# l.tail.next = n3
# l.tail = n3
# l.tail.next = l.head
# l.display()


'''Dictionary Comprehension'''
# dct = {i:i**2 for i in range(1,6)}					# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(dct)

# print('-'*30)


# dct1 = {i:i**2 for i in range(1,11) if i % 2 == 0}
# print(dct1)											# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# lst1 = ['apple','banana','mango','orange']
# print(lst1)

# for i in range(len(lst1)):
# 	print(lst1[i],{i:lst1[i]})

# dct1 = {item: len(item) for item in lst1}				# {'apple': 5, 'banana': 6, 'mango': 5, 'orange': 6}
# print(dct1)
#
# print({len(i) : i for i in lst1})

# print({i[::-1] : i for i in lst1})					# {'elppa': 'apple', 'ananab': 'banana', 'ognam': 'mango', 'egnaro': 'orange'}

# lst2 = lst1[::-1]
# print(lst2)											# ['orange', 'mango', 'banana', 'apple']
# print({i[::-1]:i for i in lst2})						# {'egnaro': 'orange', 'ognam': 'mango', 'ananab': 'banana', 'elppa': 'apple'}

# dct2 = {'Num_'+str(i) : i for i in range(1,100 + 1)}
# print(dct2)

# dct2 = {'Num_'+str(i) : i for i in range(1,100 + 1) if i % 7 == 0}
# print(dct2)
# print(len(dct2))


# l1 = ['a','b','c','d','e']
# l2 = [1,2,3,4,5]
#
# dctl12 = { l2[ i ] : l1[ i ] for i in range( len(l1) ) }
# print(dctl12)


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# final_dct = {(i+1,j+1) : matrix[i][j] for i in range(3) for j in range(3)}
# print(final_dct)
'''
{(1, 1): 1, (1, 2): 2, (1, 3): 3,
 (2, 1): 4, (2, 2): 5, (2, 3): 6,
 (3, 1): 7, (3, 2): 8, (3, 3): 9}
'''


# matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
# final_dct1 = { matrix1[i][j] : (i+1,j+1) for i in range(3) for j in range(3)}
# print(final_dct1)
'''
{1: (1, 1), 2: (1, 2), 3: (1, 3),
 4: (2, 1), 5: (2, 2), 6: (2, 3),
 7: (3, 1), 8: (3, 2), 9: (3, 3)}
'''



'''
SETS:

{values_(Empty curly brackets is by default dictionary)}:set()
Mutable
Unordered
Unique Values
'''
# set1 = {1,2,3,4,5,'a','b','c','d','e'}			# len = 10
# print(set1)
# # print(type(set1))
# print('-'*30)

# # Adding
# set1.add(6)
# print(set1)

# # Pop
# popped_s1 = set1.pop()			# For pop() use another variable
# print(popped_s1)
# print(set1)

# # Remove
# set1.discard('b')
# print(set1)

# # Iterating
# for i in set1:
# 	print(i)

# # Checking Values in set1:
# print(2 in set1)				# True
# print('b' in set1)				# True
# print('xx' in set1)				# False

# # # Set operations:
# seta = {1,2,3,4,5,'a','b','c'}				# len = 8
# setb = {4,5,6,7,8,'aa','bb','cc'}			# len = 8
#
# # # Union
# print('\nUnion')
# print(seta | setb)					# All elements of 'seta' and 'setb'
#
# # # Intersect
# print('\nIntersection')
# print(seta & setb)					# Mutual elements of 'seta' and 'setb'
#
# # # Difference
# print('\nDifference')
# print(seta - setb)					# Shows remaining elements of 'seta' which are not mutual with 'setb'
# print(setb - seta)					# Shows remaining elements of 'setb' which are not mutual with 'seta'
#
# # # Symmetric Differencce
# print('\nSymmetric Difference')
# print(seta ^ setb)					# Removes all mutual elements

# # # Clearing
# myset1 = {1,2,3,4,5,6,7,8,9}
# print(myset1)
# print('Clearing')
# myset1.clear()
# print(myset1)
# print('Cleared')



'''
TUPLE:

()
Immutable
Can be ordered
Can keep duplicate values
'''
# tup1 = (1,2,3,4,5,5,6)					# len = 7
# print(tup1)
# print(len(tup1))
#
# # # Slicing
# print('\nSlicing')
# print(tup1[1:4])				# (2, 3, 4)
# print(tup1[::-1])				# (6, 5, 5, 4, 3, 2, 1)
#
# # # Concatenate
# print('\nConcatenate')
# contup1 = (1,2,3,4,5)
# contup2 = (4,5,6,7,8)
# con = contup1 + contup2
# print(con)						# (1, 2, 3, 4, 5, 4, 5, 6, 7, 8)
# print(tuple(sorted(con)))		# (1, 2, 3, 4, 4, 5, 5, 6, 7, 8)
#
# # # Iterating
# print('\nIterating')
# tupiter = ('a','b','c','d','e','f')
# for i in tupiter:
# 	print(i,end = ' ')			# a b c d e f
# print()
#
# # # Checking Element in tuple
# print('\nChecking Element in tuple')
# print(2 in tup1)				# True
# print(88 in tup1)				# False
#
# # # Checking Count
# print('\nChecking Count')
# tupcount = (1,1,1,2,2,3,4,4,5,5,5,5,6,7,8,9)
# print(tupcount.count(1))		# 3
# print(tupcount.count(5))		# 4
# print(tupcount.count(88))		# 0
#
# # # Finding Index
# print('\nFinding Index')
# tupind = (1,2,3,4,5,6,7,8)
# print(tupind.index(5))			# 4
# # print(tupind.index(88))			# ERROR
#
# # # Multiplying Tuple
# print('\nMultiplying Tuple')
# tupmul = (1,11,2,22)
# print(tupmul * 2)				# Duplicates the tuple --> (1, 11, 2, 22, 1, 11, 2, 22)




'''
Fill the sequence

Example 1:
Input:
numbers = ( 1 ,5, 9, 13, 17 )
Output: 
1 5 9 13 17 21 25 29
Explanation: It's an increasing sequence by 4. So, the next three numbers are 17+4= 21,  21+4=25, 25+4=29.

Example 2:
Input:
numbers = (3, 1 ,-1, -3 ,-5 ,-7 )
Output:
3  1  -1  -3  -5  -7  -9  -11  -13
Explanation:  It's an decreasing sequence by 2.  So, the next three numbers are  -7-2=-9, -9-2=11, -11-2=-13
'''

# def sequence(numbers):
# 	num = list(numbers)
# 	diff = num[1] - num[0]
# 	size = len(numbers)
# 	emptylist = []
# 	x = num[0]
# 	for i in range(size + 3):
# 		emptylist.append(x)
# 		x += diff
# 	return tuple(emptylist)
#
# numbers = (5, 6, 8, 7, 42)
# print(sequence(numbers))



'''
FUNCTIONS

'def' : Keyword used to define the function
'''

# def greet():						# greet ---> name of the function
# 	print(i,"Hey! Mayank. Your function is working")
# greet()								# Hey! Mayank. Your function is working

# for i in range(1,100 + 1):
	# print(i,greet())				# Gives None
	# print(i,end = ' ')
	# greet()						# Won't give None

# [greet() for i in range(10)]		# runs greet function 10 times


'''
In function if you use same fucntion again then the last function you've written will be executed
'''
# def updating():
# 	print('First Update')
# def updating():
# 	print('Second Update')
# def updating():
# 	print('Third Update')

# updating()
'''
In above all functions have same name 'updating()'.So, the last updated function will work
'''


# # Global variable & Local variable (Scope of the function)
# g_val = 10						# Global Variable
# def greet():
# 	l_val = 5					# Local Variable
# 	print(g_val,l_val)
# greet()							# 10 5
# print(g_val)					# 10
# # print(l_val)					# ERROR :- B'koz l_val is the local variable for the function.So, it can't be called/printed outside of the function



# # Multiple variable in function

# def greet(n):
# 	print('Hello!',n.upper())
# greet('Mayank')						# Hello! MAYANK
#
# def greet(n):
# 	print('Hello!',n.upper())
# greet()								# ERROR
#
# def greet(n = 'Nothing to pass'):		# Default parameter
# 	print('Hello!',n.upper())
# greet()								# Hello! NOTHING TO PASS


# def subm(a = 0,b = 0):
# 	print(a,b,a+b)
#
# subm(5,2)					# 5 2 7
# subm(9)						# 9 0 9
# # subm(,5)					# ERROR
# subm(a = 5,b = 10)			# 5 10 15
# subm(a = 10,b = 5)			# 10 5 15
# # subm(x = 2,y = 3)			# ERROR :- B'koz input in function is (a,b)
# subm()						# 0 0 0


# # RETURN
# def subm(a = 0,b = 0):
# 	return a,b,a + b			# If parameters are more than one than it return on the tuple
#
# var1 = subm(5,2)
# print(var1)						# (5, 2, 7)
# print(type(var1))				# <class 'tuple'>


# def subm(a = 0,b = 0):
# 	return (a + b)
#
# var1 = subm(5,2)
# print(var1)						# 7
# print(type(var1))				# <class 'int'>


# # Packing | Unpacking
# def fun1(a=0,b=0,c=0):
# 	sum1 = a + b + c
# 	mul1 = a * b * c
# 	return sum1,mul1
#
# s1,s2 = fun1(1,2,3)
# print(s1,s2)				# 6 6



# # Square of list in function
# l1 = [1,2,3,4,5]
# def square_list(mayank):
# 	return [i**2 for i in mayank]
#
# print(square_list(l1))			# [1, 4, 9, 16, 25]
#
#
# # Cube of list in function
# l2 = [1,2,3,4,5]
# def cube_list(mayank):
# 	return [i**3 for i in mayank]
#
# print(cube_list(l2))			# [1, 8, 27, 64, 125]
#
#
# def final(list1,list2):
# 	return square_list(list1) + cube_list(list2)		# adding both lists using above function
# print(final(l1,l2))				# [1, 4, 9, 16, 25, 1, 8, 27, 64, 125]


# list1 = [1,2,3,4,5]
# def one(list1):
# 	return [i*2 for i in list1]
# def two(list1):
# 	return [i*3 for i in list1]
# def last(list1):
# 	return f"{one( list1 ) , 'X X' , two( list1 )}"
# print(last(list1))




# # Program for repeating digit:
# l1 = []
# while True:
# 	take1 = int( input( 'Enter Number: ' ) )
# 	# l1.append(take1)
# 	if take1 in l1:
# 		l1.append( take1 )
# 		print('Yes')
# 	else:
# 		l1.append(take1)
# 	print(l1)



# # Program to check repeating digit:
# num1 = int(input('Enter Numebr: '))
# lambai = len(str(num1))
# khaali = []
# for i in range(lambai):
# 	if str(num1)[i] in khaali:
# 		khaali.append( str( num1 )[ i ] )
# 		print('Yes!','Repeated Number: ',str( num1 )[ i ])
# 	else:
# 		khaali.append( str( num1 )[ i ] )
# number = int(''.join(khaali))
# print('Output Number:', number)




# # Same as above by (Chat GPT 3.5)
# num1 = int(input('Enter Number: '))
# lambai = len(str(num1))
# khaali = []
#
# for i in range(lambai):
#     if str(num1)[i] not in khaali:
#         khaali.append(str(num1)[i])
#     else:
#         print('Yes')
#
# # Convert the list of unique digits back to a number
# result_number = int(''.join(khaali))
#
# print('Output Number:', result_number)



# a = [1,2,3]
# b = a.append(4)
# print(a)				# [1, 2, 3, 4]
# print(b)				# None


# Tuple = (64,65,'A')
# Max = max(Tuple)
# print(Tuple)			# Error


# s = 'Python Programming'
# result = s.split(" ")[-1]
# print(result)			# Programming




'''Doubly Linked List'''
# class Node:
#     def __init__(self, elem, next=None, prev=None):
#         self.elem = elem
#         self.next = next
#         self.prev = prev
#
#
# class DLL:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#
#     def insert(self, elem):
#         new_node = Node(elem)
#         if self.head is None:
#             self.head = new_node
#             self.tail = self.head
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#
#     def delete(self, val):
#         temp = self.head
#         while temp:
#             if temp.elem == val:
#                 if temp.prev:
#                     temp.prev.next = temp.next
#                 else:
#                     self.head = temp.next
#                 if temp.next:
#                     temp.next.prev = temp.prev
#                 else:
#                     self.tail = temp.prev
#                 self.length -= 1
#                 return True
#             temp = temp.next
#         return False
#
#
# class BrowserNavigation(DLL):
#     def __init__(self):
#         super(BrowserNavigation, self).__init__()
#         self.position = None
#
#     def backward(self):
#         if self.position and self.position.prev:
#             self.position = self.position.prev
#             print("Visiting {}".format(self.position.elem))
#         else:
#             print('Nothing to go backward to!')
#
#     def forward(self):
#         if self.position and self.position.next:
#             self.position = self.position.next
#             print("Visiting {}".format(self.position.elem))
#         else:
#             print("Nothing to go forward to!")
#
#     def visit(self, site):
#         self.insert(site)
#         self.position = self.tail
#         print('Visiting {}'.format(self.position.elem))
#
#
# # Example usage:
# browser = BrowserNavigation()
# browser.visit("google.com")
# browser.visit("example.com")
# browser.visit("openai.com")
# browser.backward()
# browser.forward()


# bn = BrowserNavigation()
# bn.forward()
# bn.backward()
# bn.visit( "www.youtube.com")



